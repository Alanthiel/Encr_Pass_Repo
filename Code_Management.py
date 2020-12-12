#!/usr/bin/python3
import requests
import hashlib
import fileinput
import json
from json.decoder import JSONDecodeError
from requests.exceptions import ConnectionError


def get_hash():
    try:
        return requests.get("https://raw.githubusercontent.com/Alux-Alpha/Encr_Pass_Repo/master/Meta.json").json()[
            "Hashes"]
    except ConnectionError:
        print("Connection To GitHub Failed.... Falling back to Local Backup, as a security measure perform this check "
              "after you have connected to te Internet ")
        try:
            with open("Meta.json", 'r') as fi:
                return json.load(fi)['Hashes']
        except (FileNotFoundError, JSONDecodeError):
            print("Local Meta Error: Either Corrupted or Does Not Exist Please Retry after connecting to the Internet.")
            exit()


def get_version():
    try:
        with open("Meta.json", 'r') as fi:
            return json.load(fi)['Current_Version']
    except (FileNotFoundError, JSONDecodeError):
        print("Meta corrupted or does not exist, downloading latest edition of Meta")
        try:
            lines = requests.get("https://raw.githubusercontent.com/Alux-Alpha/Encr_Pass_Repo/master/Meta.json")
        except ConnectionError:
            print("Connection Error, Please Retry after connecting to the Internet.....  Exiting")
            exit()
        with open("Meta.json", 'w') as fi:
            fi.write(lines.text)
            fi.close()
        return get_version()


def verify(hash_table: dict, version=None):
    sha256 = hashlib.sha256()
    with open("Auth.py", 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b''):
            sha256.update(byte_block)
        authpy = sha256.hexdigest()

    del sha256

    sha256 = hashlib.sha256()
    with open("DBMan.py", 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b''):
            sha256.update(byte_block)
        dbmanpy = sha256.hexdigest()

    auth_chk, dbman_chk = '', ''
    try:
        auth_chk = hash_table[version]["Auth.py"] == authpy
        dbman_chk = hash_table[version]["DBMan.py"] == dbmanpy
    except KeyError:
        print("\nVersion Number from Meta does not exist, attempting to validate from Hash...")

    if auth_chk and dbman_chk:
        return True
    else:
        auth_ver, dbman_ver = '', ''
        for key, value in hash_table.items():
            if not auth_chk:
                if value["Auth.py"] == authpy:
                    auth_ver = key
            if not dbman_chk:
                if value["DBMan.py"] == dbmanpy:
                    dbman_ver = key
            if dbman_chk:
                dbman_ver = version
            if auth_chk:
                auth_ver = version

    if auth_ver == dbman_ver and auth_ver:
        print("\nVersioning Error Found, Hash Indicated Version = {}, Rectifying Record.....   ".format(auth_ver),
              end='')
        with fileinput.FileInput("Meta.json", inplace=True) as file:
            for line in file:
                print(line.replace(version, auth_ver), end='')
        print("✓")
        return True

    corrupted = ""
    if not auth_chk:
        corrupted += "Authentication Module "
    if not dbman_chk:
        corrupted += "Database Management Module"
    print("\nFollowing Modules Corrupted: {}".format(corrupted))
    if input("Rectify with Latest Version? (y)? ") == 'y':
        if update():
            return True
    return "Un-Rectified"


def update():
    try:
        print("\nUpdating Authentication Module.....   ", end='')
        lines = requests.get("https://raw.githubusercontent.com/Alux-Alpha/Encr_Pass_Repo/master/Auth.py")
        with open("Auth.py", 'w') as fi:
            fi.write(lines.text)
            fi.close()
        print("✓\nUpdating Database Management Module.....  ", end='')
        lines = requests.get("https://raw.githubusercontent.com/Alux-Alpha/Encr_Pass_Repo/master/DBMan.py")
        with open("DBMan.py", 'w') as fi:
            fi.write(lines.text)
            fi.close()
        print("✓\nUpdating License File..... ", end='')
        lines = requests.get("https://raw.githubusercontent.com/Alux-Alpha/Encr_Pass_Repo/master/LICENSE")
        with open("LICENSE", 'w') as fi:
            fi.write(lines.text)
            fi.close()
        print("✓\nUpdating README File.....   ", end='')
        lines = requests.get("https://raw.githubusercontent.com/Alux-Alpha/Encr_Pass_Repo/master/README.md")
        with open("README.md", 'w') as fi:
            fi.write(lines.text)
            fi.close()
        print("✓\nUpdating Meta Data....   ", end='')
        lines = requests.get("https://raw.githubusercontent.com/Alux-Alpha/Encr_Pass_Repo/master/Meta.json")
        with open("README.md", 'w') as fi:
            fi.write(lines.text)
            fi.close()
        print("✓")
        return True
    except ConnectionError:
        print("\nConnection Error, Unable To Update, Please ensure you are connected to the Internet.... Exiting")
        return None


def get_remote_version():
    try:
        return \
            requests.get("https://raw.githubusercontent.com/Alux-Alpha/Encr_Pass_Repo/master/Meta.json").json()[
                "Versions"][
                -1]
    except ConnectionError:
        return None


def main():
    if get_version() != get_remote_version() and get_remote_version() is not None:
        if input("Newer Version Found, Please update for Security Update? (y)? ").lower() == 'y':
            update()
    case = verify(get_hash(), get_version())
    if case is True:
        print("\nSoftware Integrity Verified.....Running Version: {}".format(get_version()))
    elif case == "Un-Rectified":
        print("\nManagement Module Completed; Exiting....")


if __name__ == "__main__":
    main()
