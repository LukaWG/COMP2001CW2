from flask import make_response, abort, request

from config import db, accountInformation
from models import (Trail_LocationPt, trail_locationpt_schema, trail_locationpts_schema,
                    Location_Point, location_point_schema, location_points_schema)

def read_locations_for_trail(trailID):
    # Get trail -> trailLocation link
    trailLocations = db.session.query(Trail_LocationPt).filter(Trail_LocationPt.trailID == trailID).all()

    # Get trailLocation -> Location link
    locations = []
    for trailLocation in trailLocations:
        location = db.session.query(Location_Point).filter(Location_Point.locationPointID == trailLocation.locationPointID).one_or_none()
        locations.append(location_point_schema.dump(location))

    return locations

def create():
    # Check if user is an admin
    if not accountInformation.is_admin():
        return "Unauthorized", 403
    
    
    trailLocation = request.get_json()
    trailId = trailLocation.get("trailID")
    trailLocationId = trailLocation.get("locationPointID")
    existing_trail_location = (
        db.session.query(Trail_LocationPt).filter(Trail_LocationPt.trailID == trailId, Trail_LocationPt.locationPointID == trailLocationId).one_or_none()
    )

    if existing_trail_location is None:
        new_trail_location = trail_locationpt_schema.load(trailLocation, session=db.session)
        db.session.add(new_trail_location)
        db.session.commit()
        return trail_locationpt_schema.dump(new_trail_location), 201
    else:
        abort(409, f"Trail Location link already exists")

def delete(trailID, locationPointID):
    # Check if user is an admin
    if not accountInformation.is_admin():
        return "Unauthorized", 403
    
    trailLocation = Trail_LocationPt.query.filter(Trail_LocationPt.trailID == trailID, Trail_LocationPt.locationPointID == locationPointID).one_or_none()
    if trailLocation is not None:
        db.session.delete(trailLocation)
        db.session.commit()
        return make_response(f"Trail Location deleted", 200)
    else:
        abort(404, f"Trail Location not found")