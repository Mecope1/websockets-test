from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO

import os

STATIC_FILES_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'N03zX2S0iVlAj9'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/static/<path:path>")
def static_file_handler(path):
    return send_from_directory(STATIC_FILES_DIR, path)


def message_recieved(*args, **kwargs):
    print(args, kwargs)
    print("message received")


@socketio.on('my event')
def handle_custom_event(json):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=message_recieved)


if __name__ == '__main__':
    socketio.run(app, debug=True)