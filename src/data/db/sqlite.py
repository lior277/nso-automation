import sqlite3
from contextlib import closing

def open_mem() -> sqlite3.Connection:
    con = sqlite3.connect(":memory:")
    with closing(con.cursor()) as cur:
        cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT, first TEXT, last TEXT)")
        con.commit()
    return con
