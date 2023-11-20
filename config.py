import os

from flask import Flask, jsonify

from sqlalchemy import create_engine
from sqlalchemy.sql import text

def config_app(app: Flask, base_url: str):
    app.config["BASE_URL"] = base_url

    @app.route("/")
    def index():
        return jsonify({"greet": "Hello from Colab!"})

    @app.route("/books")
    def get_books():
        engine = create_engine(os.environ["DATABASE_CONNECTION_STRING"])
        with engine.connect() as conn:
            books = conn.execute(text("select * from book")).all()
            return jsonify(books)
