from flask import make_response, abort, request

from config import db, accountInformation
from models import Location_Point, location_point_schema, location_points_schema

def read_all():
    features = db.session.query(Location_Point).all()
    return location_points_schema.dump(features)

def read_one(locationPointID):
    location = db.session.query(Location_Point).filter(Location_Point.locationPointID == locationPointID).one_or_none()
    if location is not None:
        return location_point_schema.dump(location)
    else:
        abort(404, f"Location not found for Id: {locationPointID}")

def create():
    # Check if user is an admin
    if not accountInformation.is_admin():
        return "Unauthorised", 403
    
    location = request.get_json()
    lat = location.get("latitude")
    long = location.get("longitude")
    existing_location = (db.session.query(Location_Point).filter(Location_Point.latitude == lat, Location_Point.longitude == long).one_or_none())

    if existing_location is None:
        new_location = location_point_schema.load(location, session=db.session)
        db.session.add(new_location)
        db.session.commit()
        return location_point_schema.dump(new_location), 201
    else:
        abort(409, f"Location {lat}, {long} exists already")

def update(locationPointID):
    # Check if user is an admin
    if not accountInformation.is_admin():
        return "Unauthorised", 403
    
    location = request.get_json()

    update_location = Location_Point.query.filter(Location_Point.locationPointID == locationPointID).one_or_none()

    if update_location is not None:
        update = location_point_schema.load(location, session=db.session)
        update.locationPointID = update_location.locationPointID
        db.session.merge(update)
        db.session.commit()
        return location_point_schema.dump(update_location), 200
    else:
        abort(404, f"Location not found for Id: {locationPointID}")

def delete(locationPointID):
    # Check if user is an admin
    if not accountInformation.is_admin():
        return "Unauthorised", 403

    location = Location_Point.query.filter(Location_Point.locationPointID == locationPointID).one_or_none()
    if location is not None:
        db.session.delete(location)
        db.session.commit()
        return make_response(f"Location {locationPointID} deleted", 200)
    else:
        abort(404, f"Location not found for Id: {locationPointID}")