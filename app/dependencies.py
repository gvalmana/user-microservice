"""
    Dependencies which can be used for DI
"""
from functools import lru_cache
from app.config import Settings


@lru_cache()
def get_settings():
    return Settings(db_host="localhost",db_port=3306, db_user="root",db_pass="root",db_name="users_database")
