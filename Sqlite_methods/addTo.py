import sqlite3


def addUser(username: str):
    conn = sqlite3.connect('Listr.db', timeout= 10)
    c = conn.cursor()
    sql = """
    INSERT INTO User (name) VALUES (?)
    """
    c.execute(sql, (username,))
    conn.commit()
    conn.close()


def addRoom(roomname: str):
    conn = sqlite3.connect('Listr.db', timeout= 10)
    c = conn.cursor()
    sql = """INSERT INTO Room (name) VALUES (?)"""
    c.execute(sql, (roomname,))
    conn.commit()
    conn.close()


def addItem(name: str, price: str):
    conn = sqlite3.connect('Listr.db', timeout= 10)
    c = conn.cursor()
    sql = """ INSERT INTO item (name, price) VALUES (?,?)"""
    try:
        c.execute(sql, (name, price,))
    except sqlite3.IntegrityError as e:
        print(e)
    conn.commit()
    conn.close()


def addItemToRoom(item: str, roomname: str):
    conn = sqlite3.connect('Listr.db', timeout= 10)
    c = conn.cursor()
    item_id = _item_id_query(item)
    room_id = _room_id_query(roomname)

    if item_id is not None and room_id is not None:
        sql = """INSERT INTO room_item (room_id, item_id) VALUES (?,?)"""
        c.execute(sql, (room_id, item_id,))
        conn.commit()
    conn.close()


def _item_id_query(itemname: str) -> int:
    conn = sqlite3.connect('Listr.db', timeout= 10)
    c = conn.cursor()
    sql = """SELECT id FROM Item WHERE name=?"""
    c.execute(sql, (itemname,))
    item_id = c.fetchone()
    if item_id is not None:
        item_id = item_id[0]
    conn.close()
    return item_id


def _room_id_query(testingroom: str) -> int:
    conn = sqlite3.connect('Listr.db', timeout= 10)
    c = conn.cursor()
    sql = """SELECT id From Room WHERE name=?"""
    c.execute(sql, (testingroom,))
    room_id = c.fetchone()
    if room_id != None:
        room_id = room_id[0]
    conn.close()
    return room_id


def _user_id_query(username: str) -> int:
    conn = sqlite3.connect('Listr.db', timeout= 10)
    c = conn.cursor()
    sql = "SELECT id FROM User WHERE name=?"
    c.execute(sql, (username,))
    user_id = c.fetchone()
    if user_id != None:
        user_id = user_id[0]
    conn.close()
    return user_id


def addUserToRoom(username: str, roomname: str):
    conn = sqlite3.connect('Listr.db', timeout= 10)
    c = conn.cursor()
    room_id = _room_id_query(roomname)
    user_id = _user_id_query(username)
    if user_id is not None and room_id is not None:
        sql = """INSERT INTO room_user (room_id, user_id) VALUES (?,?)"""
        c.execute(sql, (room_id, user_id,))
        conn.commit()
    conn.close()

def addOwnerToRoom(username: str, roomname: str):
    conn = sqlite3.connect('Listr.db', timeout= 10)
    c = conn.cursor()
    room_id = _room_id_query(roomname)
    user_id = _user_id_query(username)
    if user_id is not None and room_id is not None:
        sql = """INSERT INTO room_owner (room_id, user_id) VALUES (?,?)"""
        c.execute(sql, (room_id, user_id,))
        conn.commit()
    conn.close()