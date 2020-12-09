import sqlite3
import Auth


class Bundle:
    def __init__(self, platform=None, user_id=None, password=None, backup_codes=None):
        self.platform = platform
        self.user_id = user_id
        self.password = password
        self.backup_codes = backup_codes

