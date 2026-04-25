
import sqlite3
import re

def regex_matching(x, pattern):
    return bool(re.match(pattern, x))

def create_connection():
    conn = sqlite3.connect("yourdatabase.db")
    conn.create_function("REGEXP", 2, regex_matching)
    return conn
