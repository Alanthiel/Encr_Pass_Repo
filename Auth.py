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


import getpass
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import scrypt
from Crypto.Random import get_random_bytes

MODE_RAW = "RAW PASSWORD IS STORED IN THE CREDENTIALS INSTANCE"  # Password Gen
MODE_KEY = "CREDENTIALS INSTANCE IS PROBABLY FULL"  # Post Encryption / Decryption
MODE_AUTH = "EVERYTHING BUT THE KEY IS KNOWN, USED FOR AUTHENTICATION"  # Authentication of Database

# TODO: Redesign Read / Write Operations around Virtual Memory, with either mmap or io.BytesIO, preferably  <BytesIO>


class Credentials:
    def __init__(self, key=None, nonce=None, salt=None, tag=None):
        if nonce is None:
            self.nonce = get_random_bytes(12)
            self.__mode = MODE_RAW
        else:
            self.nonce = nonce

        if salt is None:
            self.salt = get_random_bytes(16)
            self.__mode = MODE_RAW
        else:
            self.salt = salt

        if key is None:
            self.__mode = MODE_AUTH
        else:
            self.key = key

        if self.__mode is MODE_RAW:
            self.key = self.gen_key(self.key, self.salt)
            self.__mode = MODE_KEY

        self.tag = tag

    def gen_key(self, passwd=None, salt=None):
        if passwd is None:
            if self.__mode is MODE_AUTH:
                raise ValueError('Key value not Set, Please Provide Key')
            else:
                passwd = self.key
        if salt is None:
            passwd = self.salt
        return scrypt(password=passwd, salt=salt, key_len=32, N=1048576, r=8, p=1)

    def set_key(self, passwd, mode=MODE_RAW):
        if mode is MODE_KEY:
            self.key = passwd
        elif mode is MODE_RAW:
            self.key = self.gen_key(passwd=passwd)
        else:
            raise ValueError("Invalid Mode Parameter")
        if self.__mode is MODE_AUTH:
            self.__mode = MODE_KEY


def decipher_and_read(path='store.cr'):
    with open(file=path, mode='rb') as instream:
        content = instream.read()
        instream.close()
    cipher = Credentials(key=None, salt=content[:16], nonce=content[32:44], tag=content[16:32])
    content = content[44:]
    cipher.set_key(getpass.getpass('Enter Password: '))
    encr = AES.new(key=cipher.key, mode=AES.MODE_GCM, nonce=cipher.nonce)
    try:
        content = encr.decrypt_and_verify(content, cipher.tag)
    except ValueError:
        try:
            cipher = encr.decrypt(content).decode('utf-8')
        except UnicodeDecodeError:
            print('Password incorrectly entered')
            return False
        else:
            if input("MAC Check Failure.......File Tampered With / Corrupted, Proceed? (y?) ").lower() != 'y':
                return False
    return content, cipher
    # TODO: Design Virtual Memory Processing -> Load to Virtual Memory, Convert Content to BytesIO fed into return
    #       Returns BytesIO to <class Database> from <DBMan.py>


# def lock_file(context, cred=None, path='store.sql'):
#    with open


def write_file(context, cred=None, path='store.cr'):
    if cred is None:
        print('No existing Credentials found: Generating New Cipher...')
        cred = Credentials()
        cred.set_key(passwd=getpass.getpass('Enter Encryption Password: '))
    cipher = AES.new(key=cred.key, mode=AES.MODE_GCM, nonce=cred.nonce)
    auth, cred.tag = cipher.encrypt_and_digest(context)
    with open(path, 'wb') as out_stream:
        out_stream.write(cred.salt)
        out_stream.write(cred.tag)
        out_stream.write(cred.nonce)
        out_stream.write(auth)
        out_stream.close()
    return cred

    # TODO: Design Virtual Memory Processing -> read connection virtual database i.e. <class DataBase :: source >
    #       file i.e. virtual memory file and transfer it to context and write as postscript to output .db file


if __name__ == "__main__":
    ciphertext = decipher_and_read()
