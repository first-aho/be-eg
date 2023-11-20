import os

from flask import Flask, jsonify

from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer
from sqlalchemy.sql import text

def config_app(app: Flask, base_url: str):
    metadata = MetaData()
    books = Table("book", metadata,
                  Column("name", String),
                  Column("price", Integer))
    engine = create_engine(os.environ["DATABASE_CONNECTION_STRING"])
    metadata.create_all(engine)
    
    app.config["BASE_URL"] = base_url

    @app.route("/")
    def index():
        return jsonify({"greet": "Hello from Colab!"})

    @app.route("/books")
    def get_books():
        with engine.connect() as conn:
            books = conn.execute(text("select * from book")).all()
            books = [{"name": book[0], "price": book[1]} for book in books]
            return jsonify(books)
