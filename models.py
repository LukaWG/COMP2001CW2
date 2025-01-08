from datetime import datetime
import pytz

from config import db, ma

#region USER
class User(db.Model):
    __tablename__ = "USERS"
    __table_args__ = {'schema': 'CW2'}
    
    userID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    emailAddress = db.Column(db.String(255))
    role = db.Column(db.String(255))

class UsersSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
#endregion

#region FEATURE
class Feature(db.Model):
    __tablename__ = "FEATURE"
    __table_args__ = {'schema': 'CW2'}

    trailFeatureID = db.Column(db.Integer, primary_key=True)
    trailFeature = db.Column(db.String(255))

class FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feature
        load_instance = True
        sqla_session = db.session

feature_schema = FeatureSchema()
features_schema = FeatureSchema(many=True)
#endregion

#region LOCATION_POINT
class Location_Point(db.Model):
    __tablename__ = "LOCATION_POINT"
    __table_args__ = {'schema': 'CW2'}
    
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
#endregion

#region TRAIL
class Trail(db.Model):
    __tablename__ = "TRAIL"
    __table_args__ = {'schema': 'CW2'}

    trailID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    trailName = db.Column(db.String(255))
    trailSummary = db.Column(db.Text)
    trailDescription = db.Column(db.Text)
    difficulty = db.Column(db.String(50))
    location = db.Column(db.String(255))
    length = db.Column(db.Numeric(10, 2))
    elevationGain = db.Column(db.Numeric(10, 2))
    routeType = db.Column(db.String(50))
    ownerID = db.Column(db.Integer, db.ForeignKey('CW2.USERS.userID'))

    owner = db.relationship('User', backref=db.backref('trails', lazy=True))
    
class TrailSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail
        load_instance = True
        sqla_session = db.session

    ownerID = ma.Integer()

trail_schema = TrailSchema()
trails_schema = TrailSchema(many=True)
#endregion

#region TRAIL_FEATURE
class Trail_Feature(db.Model):
    __tablename__ = "TRAIL_FEATURE"
    __table_args__ = {'schema': 'CW2'}
    
    trailID = db.Column(db.Integer, db.ForeignKey('CW2.TRAIL.trailID'), primary_key=True)
    trailFeatureID = db.Column(db.Integer, db.ForeignKey('CW2.FEATURE.trailFeatureID'), primary_key=True)

    trail = db.relationship('Trail', backref=db.backref('trail_features', lazy=True))
    feature = db.relationship('Feature', backref=db.backref('trail_features', lazy=True))

class Trail_FeatureSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail_Feature
        load_instance = True
        sqla_session = db.session

trail_feature_schema = Trail_FeatureSchema()
trail_features_schema = Trail_FeatureSchema(many=True)
#endregion

#region TRAIL_LOCATIONPT
class Trail_LocationPt(db.Model):
    __tablename__ = "TRAIL_LOCATIONPT"
    __table_args__ = {'schema': 'CW2'}
    
    trailID = db.Column(db.Integer, db.ForeignKey('CW2.TRAIL.trailID'), primary_key=True)
    locationPoint = db.Column(db.Integer, db.ForeignKey('CW2.LOCATION_POINT.locationPoint'), primary_key=True)
    orderNo = db.Column(db.Integer)

    trail = db.relationship('Trail', backref=db.backref('trail_locationpts', lazy=True))
    location_point = db.relationship('Location_Point', backref=db.backref('trail_locationpts', lazy=True))

class Trail_LocationPtSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Trail_LocationPt
        load_instance = True
        sqla_session = db.session

trail_locationpt_schema = Trail_LocationPtSchema()
trail_locationpts_schema = Trail_LocationPtSchema(many=True)
#endregion