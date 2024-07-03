from flask import Flask # type: ignore # ignore the error, it's a bug in the linter
from flask_sqlalchemy import SQLAlchemy # type: ignore # ignore the error, it's a bug in the linter
server = Flask(__name__)
server.config.from_object('project.config.Config')
db = SQLAlchemy(server)

class User(db.Model):
    __table_name__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    
@server.route('/')
def hello():
    return 'Hello Wdddorld!'

if __name__ == '__main__':
    server.run(host='0.0.0.0')