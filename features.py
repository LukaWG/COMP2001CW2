from flask import abort, request

from config import db, accountInformation
from models import Feature, feature_schema, features_schema

def read_all():
    features = db.session.query(Feature).all()
    return features_schema.dump(features)

def read_one(trailFeatureID):
    feature = db.session.query(Feature).filter(Feature.trailFeatureID == trailFeatureID).one_or_none()
    if feature is not None:
        return feature_schema.dump(feature)
    else:
        abort(404, f"Feature not found for Id: {trailFeatureID}")

def create():
    # Check if user is an admin
    if not accountInformation.is_admin():
        return "Unauthorized", 403
    
    feature = request.get_json()
    trailFeature = feature.get("featureName")
    existing_feature = (
        db.session.query(Feature).filter(Feature.trailFeature == trailFeature).one_or_none()
    )

    if existing_feature is None:
        new_feature = feature_schema.load(feature, session=db.session)
        db.session.add(new_feature)
        db.session.commit()
        return feature_schema.dump(new_feature), 201
    else:
        abort(409, f"Feature {trailFeature} exists already")

def update(trailFeatureID):
    # Check if user is an admin
    if not accountInformation.is_admin():
        return "Unauthorized", 403
    
    feature = request.get_json()

    update_feature = Feature.query.filter(Feature.trailFeatureID == trailFeatureID).one_or_none()

    if update_feature is not None:
        update = feature_schema.load(feature, session=db.session)
        update.trailFeatureID = update_feature.trailFeatureID
        db.session.merge(update)
        db.session.commit()
        return feature_schema.dump(update_feature), 200
    else:
        abort(404, f"Feature not found for Id: {trailFeatureID}")

def delete(trailFeatureID):
    # Check if user is an admin
    if not accountInformation.is_admin():
        return "Unauthorized", 403

    feature = Feature.query.filter(Feature.trailFeatureID == trailFeatureID).one_or_none()

    if feature is not None:
        db.session.delete(feature)
        db.session.commit()
        return "Feature successfully deleted", 204
    else:
        abort(404, f"Feature not found for Id: {trailFeatureID}")