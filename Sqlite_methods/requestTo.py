from Sqlite_methods import addTo
import sqlite3
from typing import List, Dict
"""
Data structure:
    item = (id, itemname, price)
    user = (id, name)
"""
def requestRoomData(roomname: str) -> Dict:
    room_id = addTo._room_id_query(roomname)
    room_item_data = requestRoomItems(room_id)
    room_user_data = requestRoomUsers(room_id)
    return {'room_item_data': room_item_data, 'room_user_data': room_user_data}


def requestRoomUsers(room_id: int) -> List:
    conn = sqlite3.connect('Listr.db', timeout=10)
    c = conn.cursor()
    sql = """
    SELECT User.*
    FROM User
        INNER JOIN room_user AS RU ON RU.user_id = User.Id
    WHERE RU.room_id = ?
    """
    c.execute(sql, (room_id,))
    users = c.fetchall()
    if users is not None:
        print(users)
    conn.close()
    return users


def requestRoomItems(room_id: int) -> List:
    conn = sqlite3.connect('Listr.db', timeout=10)
    c = conn.cursor()
    sql = """
        SELECT Item.*
        FROM Item
            INNER JOIN room_item AS RI ON RI.item_id = Item.Id
        WHERE RI.room_id = ?
        """
    c.execute(sql, (room_id,))
    items = c.fetchall()
    if items is not None:
        print(items)
    conn.close()
    return items