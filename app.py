# -*- coding:utf-8 -*-
from gevent import monkey
from socketio.defaultjson import default_json_dumps
monkey.patch_all()

import time
#from threading import Thread
from flask import Flask, render_template, session, request, json
from flask.ext.socketio import SocketIO, emit, join_room, leave_room
from flask.ext.mysql import MySQL
from Characters.Human import Human
from Shops.GeneralStore import GeneralStore
from ServerInstance import ServerInstance
from Characters.Inventory import Inventory
from Items.Swords import StarterSword


app = Flask(__name__)
app.config.from_object('config')
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None


si = ServerInstance()
si.list_server_cities()


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        time.sleep(10)
        count += 1
        socketio.emit('my response',
                      {'data': 'Server generated event', 'count': count},
                      namespace='/test')


@app.route('/')
def index():
    #global thread
    #if thread is None:
        #thread = Thread(target=background_thread)
        #thread.start()
    return render_template('city.html')

@socketio.on('connecting', namespace='')
def connecting(data):
    print 'Client connected: %s' % data
    char = Human('AAA1', 'linkzao')
    char.equip_item(StarterSword())
    #print char.inventory.get_backpack_items(json=True)

    session['character'] = char
    session['inventory'] = char.inventory
    si.add_character(session['character'])

    socketio.emit('test-json', {'character_list': si.list_server_characters(json=True)})
    socketio.emit('ack-connected', {'character': session['character'].to_JSON(), 'inventory': session['inventory'].to_JSON()})
    #print data



@socketio.on('hero-move', namespace='')
def hero_move(data):
    pass



@socketio.on('disconnect', namespace='')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
