from flask import abort, request

from config import db
from models import User, user_schema

# def read_all():
#     people = db.session.query(User).all()
#     return users_schema.dump(people)

# def read_one(userID):
#     user = db.session.query(User).filter(User.userID == userID).one_or_none()
#     # user = User.query.filter(User.userID == userID).one_or_none()
#     if user is not None:
#         return user_schema.dump(user)
#     else:
#         abort(404, f"User not found for Id: {userID}")

def create():
    user = request.get_json()
    emailAddress = user.get("emailAddress")
    existing_user = (
        db.session.query(User).filter(User.emailAddress == emailAddress).one_or_none()
    )

    if existing_user is None:
        new_user = user_schema.load(user, session=db.session)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user), 201
    else:
        abort(409, f"User {emailAddress} exists already")