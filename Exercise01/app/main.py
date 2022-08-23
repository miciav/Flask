from flask import Flask, jsonify
from model import db, User
from schemas import ma, UserSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = db.init_app(app)
ma = ma.init_app(app)


@app.route('/')
def index():
    users = User.query.all()
    user_schema = UserSchema(many=True)
    output = user_schema.dump(users)
    return jsonify({'user': output})


if __name__ == '__main__':
    app.run()
