CREATE TABLE houses(
    Suburb varchar,
    Address varchar,
    Rooms int,
    Type varchar,
    Price int,
    Method varchar,
    SellerG varchar,
    Date date,
    Distance float,
    Postcode varchar,
    Bedroom2 int,
    Bathroom int,
    Car int,
    Landsize float,
    BuildingArea float,
    YearBuilt int,
    CouncilArea varchar,
    Lattitude float,
    Longtitude float,
    Regionname varchar,
    Propertycount int
);

\COPY houses(Suburb,Address,Rooms,Type,Price,Method,SellerG,Date,Distance,Postcode,Bedroom2,Bathroom,Car,Landsize,BuildingArea,YearBuilt,CouncilArea,Lattitude,Longtitude,Regionname,Propertycount) FROM 'Melbourne_housing_FULL.csv' DELIMITER ',' CSV HEADER;
