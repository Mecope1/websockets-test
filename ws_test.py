from eventlet import wsgi, websocket, listen


@websocket.WebSocketWSGI
def hello_world(ws):
    wat = True
    while wat:
        wat = ws.wait()
        ws.send("Echo: {0}".format(wat))


if __name__ == "__main__":
    wsgi.server(listen(('', 8090)), hello_world)