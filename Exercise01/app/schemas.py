from flask_marshmallow import Marshmallow
from model import User, Reward

ma = Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True


class RewardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reward
        load_instance = True
