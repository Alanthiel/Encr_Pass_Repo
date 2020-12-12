import requests
import hashlib


def get_hash():
    return requests.get("https://raw.githubusercontent.com/Alux-Alpha/Encr_Pass_Repo/master/Hash_Table.json").json()


def auth(hash_table: dict):
    sha256 = hashlib.sha256()
    with open("Auth.py", 'rb') as f:
        for byte_block in iter(lambda: f.read(4096), b''):
            sha256.update(byte_block)
        print(sha256.hexdigest())


def main():
    auth(get_hash())


if "__name__" == "__main__":
    main()
