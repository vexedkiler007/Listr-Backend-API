import sqlite3
from Sqlite_methods import addTo


def removeUserFromRoom(username: str):
    user_id = addTo._user_id_query(username)
    conn = sqlite3.connect('Listr.db', timeout=10)
    c = conn.cursor()
    sql_pivot = """DELETE FROM room_user WHERE user_id=?"""
    c.execute(sql_pivot, (user_id,))
    conn.commit()


def removeUser(username: str):
    conn = sqlite3.connect('Listr.db', timeout=10)
    c = conn.cursor()
    sql = """DELETE FROM User WHERE name=?"""
    c.execute(sql, (username,))
    conn.commit()


def removeUserAll(username: str):
    removeUserFromRoom(username)
    _removeOwner(username)
    removeUser(username)


def removeItemFromRoom(item_name: str):
    item_id = addTo._item_id_query(item_name)
    conn = sqlite3.connect('Listr.db', timeout=10)
    c = conn.cursor()
    sql = """DELETE FROM room_item WHERE item_id=?"""
    c.execute(sql, (item_id,))
    conn.commit()


def removeItem(item_name: str):
    conn = sqlite3.connect('Listr.db', timeout=10)
    c = conn.cursor()
    sql = """DELETE FROM Item WHERE name=?"""
    c.execute(sql, (item_name,))
    conn.commit()


def removeItemAll(item_name: str):
    removeItemFromRoom(item_name)
    removeItem(item_name)


# should only be called if room is deleted
def _removeOwner(username: str):
    user_id = addTo._user_id_query(username)
    conn = sqlite3.connect('Listr.db', timeout=10)
    c = conn.cursor()
    sql = """DELETE FROM room_owner WHERE user_id=?"""
    c.execute(sql, (user_id,))
    conn.commit()
