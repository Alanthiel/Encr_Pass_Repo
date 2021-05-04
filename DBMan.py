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

from dataclasses import dataclass, asdict, astuple
import Auth


# TODO: Deploy JSON based Encrypted Store using Auth module
# TODO: Deploy sqlcipher based Encrypted Store


@dataclass(repr=False, unsafe_hash=True)
class Bundle:
    dbid: str = None
    platform: str = None
    userid: str = None
    password: str = None
    backup_codes: list = None
    serectkey: str = None

    def __repr__(self):
        return "Credentials (Platform: {}, User Id: {}".format(self.platform, self.userid)

    def check_codes(self):
        if self.backup_codes is None:
            return False



class DataBase:
    def __init__(self, db_path="store.sql"):
        return NotImplemented

