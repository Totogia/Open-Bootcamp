import sqlite3 as SQL

def createDB ():
    conn = SQL.connect ("streamers.db")
    conn.commit ()
    conn.close ()


if __name__ == "__main__":
    createDB ()

