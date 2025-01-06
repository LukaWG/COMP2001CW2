CREATE TABLE CW2.TRAIL_FEATURE (
    trailID INT,
    trailFeatureID INT,
    PRIMARY KEY (trailID, trailFeatureID),
    FOREIGN KEY (trailID) REFERENCES CW2.TRAIL(trailID),
    FOREIGN KEY (trailFeatureID) REFERENCES CW2.FEATURE(trailFeatureID)
);