CREATE TABLE CW2.FEATURE (
    trailFeatureID INT IDENTITY(1,1) PRIMARY KEY,
    trailFeature VARCHAR(255)
);

CREATE TABLE CW2.LOCATION_POINT (
    locationPoint INT PRIMARY KEY,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    description TEXT
);

CREATE TABLE CW2.USERS (
    userID INT IDENTITY(1,1) PRIMARY KEY,
    emailAddress VARCHAR(255) UNIQUE NOT NULL,
    role VARCHAR(255)
);

CREATE TABLE CW2.TRAIL (
    trailID INT IDENTITY(1,1) PRIMARY KEY,
    trailName VARCHAR(255),
    trailSummary TEXT,
    trailDescription TEXT,
    difficulty VARCHAR(50),
    location VARCHAR(255),
    length DECIMAL(10,2),
    elevationGain DECIMAL(10,2),
    routeType VARCHAR(50),
    ownerID INT,
    FOREIGN KEY (ownerID) REFERENCES CW2.USERS(userID)
);

CREATE TABLE CW2.TRAIL_FEATURE (
    trailID INT,
    trailFeatureID INT,
    PRIMARY KEY (trailID, trailFeatureID),
    FOREIGN KEY (trailID) REFERENCES CW2.TRAIL(trailID),
    FOREIGN KEY (trailFeatureID) REFERENCES CW2.FEATURE(trailFeatureID)
);

CREATE TABLE CW2.TRAIL_LOCATIONPT (
    trailID INT,
    locationPoint INT,
    orderNo INT,
    PRIMARY KEY (trailID, locationPoint),
    FOREIGN KEY (trailID) REFERENCES CW2.TRAIL(trailID),
    FOREIGN KEY (locationPoint) REFERENCES CW2.LOCATION_POINT(locationPoint)
);