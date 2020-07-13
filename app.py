from flask import Flask, request, jsonify
import api_communication.api_handler
from Sqlite_methods import requestTo, addTo, remove
import sqlite3

app = Flask(__name__)


# @app.route vs @app.endpoint
# authenticates end points
@app.route('/')
def welcome():
    headers = request.headers
    auth = headers.get("X-Api-key")
    if auth == 'password':
        return "<h3>Welcome<h3>"
    else:
        return "Error 401"


@app.route('/search')
def search():
    search_term = request.args.get('search_term')
    api = request.args.get('api')
    return jsonify(api_communication.api_handler.handle_request(search_term=search_term, api=api))


# Searches wanted api and return of a json of item, price
@app.route('/additem')
def addItem():
    item_name = request.args.get("item_name")
    item_price = request.args.get("item_price")
    addTo.addItem(item_name, item_price)
    return jsonify({'No Error': 'Item successfully added to database'})


@app.route('/adduser')
def addUser():
    nickname = request.args.get("username")
    try:
        addTo.addUser(nickname)
    except sqlite3.IntegrityError as e:
        return jsonify({'Error': str(e)})
    return jsonify({'No Error': 'User successfully added to database'})


@app.route('/makeroom')
def makeRoom():
    room_name = request.args.get('room_name')
    addTo.addRoom(room_name)
    return jsonify({'No Error': 'Room successfully added to database'})


@app.route('/additemtoroom')
def addItemToRoom():
    item = request.args.get('item')
    roomname = request.args.get('roomname')
    addTo.addItemToRoom(item, roomname)
    return jsonify({'No Error': 'Item successfully added to database'})


@app.route('/addusertoroom')
def addUserToRoom():
    username = request.args.get('username')
    roomname = request.args.get('roomname')
    addTo.addUserToRoom(username, roomname)
    return jsonify({'No Error': 'User successfully added to database'})


@app.route('/requestroominfo')
def requestRoomInfo():
    roomname = request.args.get('roomname')
    return jsonify(requestTo.requestRoomData(roomname))


# May not be added
@app.route('/requestid')
def requestId():
    id = request.args.get('id')
    return ""


@app.route('/removeuser')
def removeUser():
    username = request.args.get('username')
    remove.removeUser(username)
    return jsonify({'No Error': 'Item successfully deleted from database'})


@app.route('/removeuserfromroom')
def removeUserFromRoom():
    username = request.args.get('username')
    remove.removeUserFromRoom(username)
    return jsonify({'No Error': 'User successfully deleted from database'})


@app.route('/removeuserall')
def removeUserAll():
    username = request.args.get('username')
    remove.removeUserAll(username)
    return jsonify({'No Error': 'Item successfully deleted from all databases'})


@app.route('/removeitem')
def removeItem():
    item_name = request.args.get('item_name')
    remove.removeItem(item_name)
    return jsonify({'No Error': 'Item successfully deleted from database'})


@app.route('/removeitemfromroom')
def removeItemFromRoom():
    item_name = request.args.get('item_name')
    remove.removeItemFromRoom(item_name)
    return jsonify({'No Error': 'Item successfully deleted from database'})


@app.route('/removeitemall')
def removeItemAll():
    item_name = request.args.get('item_name')
    remove.removeItemAll(item_name)
    return jsonify({'No Error': 'Item successfully deleted from all databases'})


@app.route('/addowner')
def addOwnertoRoom():
    owner_name = request.args.get('owner_name')
    addTo.addOwnerToRoom(owner_name)
    return jsonify({'No Error': 'Owner successfully added to database'})


if __name__ == '__main__':
    app.run()

"""

Google Shopping (SerpApi) # https://serpapi.com/
Walmart    # closed beta
Amazon     # need 3 qualifying sales and approved associate account
Target     # error
Best Buy
Home Depot # error: http://developer.homedepot.com/
Macy's     # private API
Facebook   # head scratcher
Google Shopping # dead? https://developers.google.com/shopping-search/

"""
