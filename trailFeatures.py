from flask import make_response, abort, request

from config import db, accountInformation
from models import Trail_Feature, trail_feature_schema, trail_features_schema

def read_features_for_trail(trailID):
    # Get trail -> trailfeature link
    trailFeatures = db.session.query(Trail_Feature).filter(Trail_Feature.trailID == trailID).all()

    # Get trailfeature -> feature link
    featureNames = []
    for trailFeature in trailFeatures:
        featureNames.append(trailFeature.feature.featureName)

    return featureNames

def create():
    # Check if user is an admin
    if not accountInformation.is_admin():
        return "Unauthorised", 403
    
    trailFeature = request.get_json()
    trailId = trailFeature.get("trailId")
    trailFeatureId = trailFeature.get("trailFeatureId")
    existing_trail_feature = (
        db.session.query(Trail_Feature).filter(Trail_Feature.trailId == trailId, Trail_Feature.trailFeatureID == trailFeatureId).one_or_none()
    )

    if existing_trail_feature is None:
        new_trail = trail_feature_schema.load(trailFeature, session=db.session)
        db.session.add(new_trail)
        db.session.commit()
        return trail_feature_schema.dump(new_trail), 201
    else:
        abort(409, f"Trail feature link already exists")

def delete(trailID, trailFeatureID):
    # Check if user is an admin
    if not accountInformation.is_admin():
        return "Unauthorised", 403
    
    trailFeature = Trail_Feature.query.filter(Trail_Feature.trailID == trailID, Trail_Feature.trailFeatureID == trailFeatureID).one_or_none()
    if trailFeature is not None:
        db.session.delete(trailFeature)
        db.session.commit()
        return make_response(f"Trail Feature {trailID} deleted", 200)
    else:
        abort(404, f"Trail Feature not found for Id: {trailID}")