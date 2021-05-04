# MIT License

# Copyright (c) 2020 Nehal Gowrish (Alias: Alanthiel)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import json
import requests
import hashlib
import fileinput
from json import JSONDecodeError
from requests.exceptions import ConnectionError


class Errors:
    Con_Fail = ConnectionError
    VersionError = "<Files of different Versions together>"
    FileError = "<File-Non-existent/Corrupted>"


content = ["Auth.py", "DBMan.py", "LICENSE", "README", "Meta.json", "Manager.py"]


def get_remote_version():
    try:
        return \
            requests.get("https://raw.githubusercontent.com/Alanthiel/Encr_Pass_Repo/master/Meta.json").json()[
                "Versions"][
                -1]
    except ConnectionError:
        return Errors.Con_Fail


def get_local_version(rectify=False):
    try:
        with open("Meta.json", 'r') as fi:
            return json.load(fi)['Current_Version']
    except (FileNotFoundError, JSONDecodeError):
        if rectify is True:
            _ = update(portion=['Meta.json'])
            if _ is True:
                return get_local_version()
            else:
                return Errors.Con_Fail
        else:
            return Errors.FileError


def update(portion=None, output=False):
    if portion != ["Meta.json"]:
        verify_meta_data(rectify=True)
    if portion is None:
        portion = content
    try:
        for file in portion:
            if output is True:
                print("\nUpdating {} Module..... ".format(file), end='')
            code = requests.get("https://raw.githubusercontent.com/Alanthiel/Encr_Pass_Repo/master/{}".format(file))
            if code.status_code != 200:
                return Errors.FileError
            with open(file, 'w') as fi:
                fi.write(code.text)
                fi.close()
            if output is True:
                print("\033[1;32;49m ✓", end='')
    except ConnectionError:
        return Errors.Con_Fail
    except KeyboardInterrupt:
        return KeyboardInterrupt
    return True


def get_remote_hashtable():
    try:
        remote_hash = \
            requests.get("https://raw.githubusercontent.com/Alanthiel/Encr_Pass_Repo/master/Meta.json").json()[
                "Hashes"]
        return remote_hash
    except ConnectionError:
        return Errors.Con_Fail


def get_local_hashtable():
    try:
        with open("Meta.json", 'r') as fi:
            return json.load(fi)['Hashes']
    except (FileNotFoundError, JSONDecodeError):
        return Errors.FileError


def verify_meta_data(rectify=False):
    try:
        remote_hash = \
            requests.get("https://raw.githubusercontent.com/Alanthiel/Encr_Pass_Repo/master/Meta.json").json()
    except ConnectionError:
        return Errors.Con_Fail
    try:
        with open("Meta.json", 'r') as file:
            local_hash = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        if rectify is True:
            update(portion=['Meta.json'])
        else:
            return Errors.FileError

    for i in local_hash["Hashes"]:
        if i not in remote_hash["Hashes"] or local_hash['Hashes'][i] != remote_hash['Hashes'][i]:
            if rectify is True:
                update(portion=['Meta.json'])
                return True
            return False
    return True


def verify_integrity(remote_priority=True, fallback=True, rescue_by_update=False):
    if remote_priority is True:
        hashtable = get_remote_hashtable()
        if hashtable == Errors.Con_Fail:
            if fallback is True:
                hashtable = get_local_hashtable()
                if hashtable == Errors.FileError:
                    return Errors.Con_Fail
            else:
                return Errors.Con_Fail
    else:
        hashtable = get_local_hashtable()
        if hashtable == Errors.FileError:
            if fallback is True:
                hashtable = get_remote_hashtable()
                if hashtable == Errors.Con_Fail:
                    return Errors.FileError
            else:
                return Errors.FileError

    current_version = get_local_version()
    apparent_version = ''
    sha256 = hashlib.sha256()
    for file in content:
        with open(file, 'rb') as fi:
            for byte_block in iter(lambda: fi.read(4096), b''):
                sha256.update(byte_block)
            hexcode = sha256.hexdigest()

        if hashtable[current_version][file] == hexcode:  # noqa
            if not apparent_version:
                continue
        if apparent_version:
            if hashtable[apparent_version][file] == hexcode:  # noqa
                continue
        else:
            for version in hashtable:
                if hashtable[version][file] == hexcode:  # noqa
                    apparent_version = version  # noqa
                    continue
        if rescue_by_update is True:
            return update()
        else:
            return False
    if apparent_version:
        with fileinput.FileInput("Meta.json", inplace=True) as file:
            for line in file:
                print(line.replace(current_version, apparent_version), end='')
    return True


if __name__ == "__main__":
    pass
