CREATE TABLE CW2.TRAIL_LOCATIONPT (
    trailID INT,
    locationPoint INT,
    orderNo INT,
    PRIMARY KEY (trailID, locationPoint),
    FOREIGN KEY (trailID) REFERENCES CW2.TRAIL(trailID),
    FOREIGN KEY (locationPoint) REFERENCES CW2.LOCATION_POINT(locationPoint)
);