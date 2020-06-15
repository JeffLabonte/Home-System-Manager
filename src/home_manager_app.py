from handlers.routes import configure_routes
from flask import Flask


app = Flask(__name__)
configure_routes(app=app)


if __name__ == "__main__":
    app.run()
