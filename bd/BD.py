import mysql.connector
from dotenv import load_dotenv
import os


class BD:
    def __init__(self):
        self.db_host = os.getenv("DB_HOST")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_name = os.getenv("DB_NAME")

        self.db_config = {
            "host": self.db_host,
            "user": self.db_user,
            "password": self.db_password,
            "database": self.db_name,
        }

    def get_connection(self):
        return mysql.connector.connect(**self.db_config)


