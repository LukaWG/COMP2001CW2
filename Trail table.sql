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