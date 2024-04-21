from flask import Flask
from flask_cors import CORS  # Import the CORS module
from flask_sqlalchemy import SQLAlchemy
from security.config import DB_URI

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI  # Correct SQLite URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


from api.router import router

app.register_blueprint(router, url_prefix='/api/v1/')

if __name__ == '__main__':
    app.run(debug=True)
