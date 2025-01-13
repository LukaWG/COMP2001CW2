CREATE TABLE CW2.LOCATION_POINT (
    locationPointID INT IDENTITY(1,1) PRIMARY KEY,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    description TEXT
);