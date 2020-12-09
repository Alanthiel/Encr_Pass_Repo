import sqlite3
import Auth
from sqlite3 import Error


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
        if self.backup_codes is not dict:
            raise TypeError("Error: Backup Code format incorrect, Format should be of type <dict>")
        for i in self.backup_codes:
            if i is not str:
                raise TypeError("Error: Code format incorrect, <{}> is not of type <string>".format(i))

    def return_dict(self):
        self.check_codes()
        return {"Platform": self.platform, "User ID": self.user_id, "Password": self.password,
                "2FA Codes": self.backup_codes}


class DataBase:
    def __init__(self, db_path="store.sql"):
        source = sqlite3.connect(db_path)
        self.store = sqlite3.connect(":memory:")
        source.backup(self.store)
