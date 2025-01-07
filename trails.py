from flask import make_response, abort

from config import db
from models import Trail, trail_schema, trails_schema

def read_all():
    people = Trail.query.all()
    return trails_schema.dump(people)

def read_one(trailID):
    trail = Trail.query.filter(Trail.trailID == trailID).one_or_none()
    if trail is not None:
        return trail_schema.dump(trail)
    else:
        abort(404, f"Trail not found for Id: {trailID}")

def create(trail):
    trailName = trail.get("trailName")
    existing_trail = (
        Trail.query.filter(Trail.trailName == trailName)
        .one_or_none()
    )

    if existing_trail is None:
        schema = TrailSchema()
        new_trail = schema.load(trail, session=db.session)
        db.session.add(new_trail)
        db.session.commit()
        return trail_schema.dump(new_trail), 201
    else:
        abort(409, f"Trail {trailName} exists already")

def update(trailID, trail):
    update_trail = Trail.query.filter(
        Trail.trailID == trailID
    ).one_or_none()

    if update_trail is not None:
        schema = TrailSchema()
        update = schema.load(trail, session=db.session)
        update.trailID = update_trail.trailID
        db.session.merge(update)
        db.session.commit()
        return trail_schema.dump(update_trail), 200
    else:
        abort(404, f"Trail not found for Id: {trailID}")

def delete(trailID):
    trail = Trail.query.filter(Trail.trailID == trailID).one_or_none()
    if trail is not None:
        db.session.delete(trail)
        db.session.commit()
        return make_response(f"Trail {trailID} deleted", 200)
    else:
        abort(404, f"Trail not found for Id: {trailID}")