from flask import Flask, jsonify

def config_app(app: Flask, base_url: str):
    app.config["BASE_URL"] = base_url

    @app.route("/")
    def index():
        return jsonify({"greet": "Hello from Colab!"})
