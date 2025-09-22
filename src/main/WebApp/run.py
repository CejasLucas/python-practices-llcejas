from WebApp import create_app, socketio
import WebApp.socketio_handlers

app = create_app()

if __name__ == '__main__':
    socketio.run(app, debug=True)