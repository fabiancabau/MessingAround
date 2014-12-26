# -*- coding:utf-8 -*-
from gevent import monkey
from socketio.defaultjson import default_json_dumps
from Character import Character

monkey.patch_all()

import time
from threading import Thread
from flask import Flask, render_template, session, request, json
from flask.ext.socketio import SocketIO, emit, join_room, leave_room
from flask.ext.mysql import MySQL

app = Flask(__name__)
app.config.from_object('config')
app.debug = True
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
thread = None


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
    return render_template('index.html')


@socketio.on('new-hero', namespace='')
def new_hero(data):
    pass


@socketio.on('hero-move', namespace='')
def hero_move(data):
    pass



@socketio.on('disconnect', namespace='')
def test_disconnect():
    print('Client disconnected')


if __name__ == '__main__':
    socketio.run(app)
