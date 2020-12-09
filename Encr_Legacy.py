# MIT License

# Copyright (c) 2020 Nehal Gowrish (Alias: Alux-Alpha)

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
import mmap
import scrypt
import random
import string
import getpass


def read_file(path="store.cr"):
    with open(path, mode="r") as pass_raw:
        with mmap.mmap(pass_raw.fileno(), length=0, flags=mmap.MAP_PRIVATE) as data:
            read_info = data.read()
            data.close()
            return read_info


def write_file(file_obj, path="store.cr"):
    with open(path, 'w') as pass_out_raw:
        pass_out_raw.write(file_obj)
        pass_out_raw.close()


def gen_salt(size=6):
    if type(size) is not int:
        raise ValueError("Salt Size should be an Int")
    choices = string.ascii_letters + string.digits + string.punctuation.replace('$', '')
    salt = ''.join(random.choices(choices, k=size))
    return salt


def gen_hash(key, salt=gen_salt()):
    out_hash = scrypt.hash(key, salt)
    return salt + "$" + out_hash.hex() + '\n'


def authenticate(in_stream=read_file()):
    in_stream = in_stream.decode('utf-8')
    salt, auth_hash = in_stream.split('\n')[0].split('$')
    passwd = getpass.getpass("Enter Password >>>")
    new_hash = scrypt.hash(passwd, salt).hex()
    if new_hash == auth_hash:
        return True
    else:
        return False


def gen_ini_file():
    passwd = input("Enter the Password: ")
    pass_out = gen_hash(passwd)
    print(pass_out)
    test_data = """This is a testfile\nHopefully it Goes Well"""
    out_stream = pass_out + test_data
    write_file(out_stream)


def main():
    auth = authenticate()
    if auth:
        print("Welcome")
    else:
        print("Who the fuck are you")


if __name__ == "__main__":
    main()