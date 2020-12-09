
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