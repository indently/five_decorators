import atexit
import sqlite3

cxn = sqlite3.connect("db.sqlite3")


def init_db():
    cxn.execute("CREATE TABLE IF NOT EXISTS memes (id INTEGER PRIMARY KEY, meme TEXT)")
    print("Database initialised!")


@atexit.register
def exit_handler():
    cxn.commit()
    cxn.close()
    print("Closed database!")


if __name__ == "__main__":
    init_db()
    1 / 0
    ...
