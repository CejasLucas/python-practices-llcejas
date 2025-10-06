from src.main.WebApp import create_app, socketio
from src.main.WebApp import socketio_handlers
app = create_app()

if __name__ == "__main__":
    socketio.run(
        app,
        host="0.0.0.0",
        port=5000,
        debug=False,
        use_reloader=False,
        allow_unsafe_werkzeug=True
    )