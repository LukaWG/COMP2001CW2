CREATE TABLE CW2.TRAIL_LOCATIONPT (
    trailID INT,
    locationPointID INT,
    orderNo INT,
    PRIMARY KEY (trailID, locationPointID),
    FOREIGN KEY (trailID) REFERENCES CW2.TRAIL(trailID),
    FOREIGN KEY (locationPointID) REFERENCES CW2.LOCATION_POINT(locationPointID)
);