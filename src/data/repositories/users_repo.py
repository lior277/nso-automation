from contextlib import closing
import sqlite3

class UsersRepo:
    def __init__(self, con: sqlite3.Connection):
        self.con = con

    def upsert_many(self, rows: list[tuple[int, str, str, str]]) -> None:
        with closing(self.con.cursor()) as cur:
            cur.executemany(
                "INSERT INTO users(id,email,first,last) VALUES(?,?,?,?) "
                "ON CONFLICT(id) DO UPDATE SET email=excluded.email, first=excluded.first, last=excluded.last",
                rows
            )
            self.con.commit()

    def count(self) -> int:
        return self.con.execute("SELECT COUNT(*) FROM users").fetchone()[0]
