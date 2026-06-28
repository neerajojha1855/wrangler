from flask import Flask
from flask_cors import CORS
from api.routes import api_bp
from database import init_db

def create_app():
    app = Flask(__name__)
    CORS(app)

    init_db()

    app.register_blueprint(api_bp, url_prefix='/api')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=8000)