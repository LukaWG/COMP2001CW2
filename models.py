from datetime import datetime
import pytz

from config import db, ma

class Feature(db.Model):
    __tablename__ = "CW2.FEATURE"
    trailFeatureID = db.Column(db.Integer, primary_key=True)
    trailFeature = db.Column(db.String(255))

class FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feature
        load_instance = True
        sqla_session = db.session

feature_schema = FeatureSchema()
features_schema = FeatureSchema(many=True)


class Location_Point(db.Model):
    __tablename__ = "CW2.LOCATION_POINT"
    locationPoint = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Numeric(9, 6))
    longitude = db.Column(db.Numeric(9, 6))
    description = db.Column(db.Text)

class Location_PointSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Location_Point
        load_instance = True
        sqla_session = db.session

location_point_schema = Location_PointSchema()
location_points_schema = Location_PointSchema(many=True)


class Trail(db.Model):
    __tablename__ = "CW2.TRAIL"
    trailID = db.Column(db.Integer, primary_key=True)
    trailName = db.Column(db.String(255))
    trailSummary = db.Column(db.Text)
    trailDescription = db.Column(db.Text)
    difficulty = db.Column(db.String(50))
    location = db.Column(db.String(255))
    length = db.Column(db.Numeric(10, 2))
    elevationGain = db.Column(db.Numeric(10, 2))
    routeType = db.Column(db.String(50))
    ownerID = db.Column(db.Integer, db.ForeignKey('CW2.USERS.userID'))
    
class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session

trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)


class Trail_Feature(db.Model):
    __tablename__ = "CW2.TRAIL_FEATURE"
    trailID = db.Column(db.Integer, db.ForeignKey('CW2.TRAIL.trailID'), primary_key=True)
    trailFeatureID = db.Column(db.Integer, db.ForeignKey('CW2.FEATURE.trailFeatureID'), primary_key=True)

class Trail_FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail_Feature
        load_instance = True
        sqla_session = db.session

trail_feature_schema = Trail_FeatureSchema()
trail_features_schema = Trail_FeatureSchema(many=True)


class Trail_LocationPt(db.Model):
    __tablename__ = "CW2.TRAIL_LOCATIONPT"
    trailID = db.Column(db.Integer, db.ForeignKey('CW2.TRAIL.trailID'), primary_key=True)
    locationPoint = db.Column(db.Integer, db.ForeignKey('CW2.LOCATION_POINT.locationPoint'), primary_key=True)
    orderNo = db.Column(db.Integer)

class Trail_LocationPtSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail_LocationPt
        load_instance = True
        sqla_session = db.session

trail_locationpt_schema = Trail_LocationPtSchema()
trail_locationpts_schema = Trail_LocationPtSchema(many=True)


class Users(db.Model):
    __tablename__ = "CW2.USERS"
    userID = db.Column(db.Integer, primary_key=True)
    emailAddress = db.Column(db.String(255))
    role = db.Column(db.String(255))

class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        load_instance = True
        sqla_session = db.session

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)