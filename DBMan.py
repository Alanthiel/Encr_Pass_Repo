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

import sqlite3
import Auth
from sqlite3 import Error


# TODO: Develop System to Read sqlite3 and handle storage of Data:
#       To try : A JSon instance containing all data from db
#                A List / Dict instance containing <Platform - User_ID> Pairs, with Passwords / 2FA codes queried on
#                   request

# TODO: Design System around two Live connections:
#           -> In Memory virtual db - i.e. <Class Database :: self.store>
#           -> Physical db connected by source -> Virtual File -> saved to Physical File by Auth.write_file


class Bundle:
    def __init__(self, platform=None, user_id=None, password=None, backup_codes=None, db_id=None):
        self.db_id = db_id
        self.platform = platform
        self.user_id = user_id
        self.password = password
        self.backup_codes = backup_codes
        self.check_codes()

    def check_codes(self):
        if self.backup_codes is None:
            return True
        if self.backup_codes is not list:
            raise TypeError("Error: Backup Code format incorrect, Format should be of type <list>")
        for i in self.backup_codes:
            if i is not str:
                raise TypeError("Error: Code format incorrect, [{}] is not of type <string>".format(i))

    def return_dict(self):
        self.check_codes()
        return {"Platform": self.platform, "User ID": self.user_id, "Password": self.password,
                "2FA Codes": self.backup_codes}


class DataBase:
    def __init__(self, db_path="store.sql"):
        source = sqlite3.connect(db_path)
        self.store = sqlite3.connect(":memory:")
        source.backup(self.store)
        # TODO: Create Database connections
        #       from -> Load to Virtual Memory, Decrypt and Convert to sqlite3 connection instance
