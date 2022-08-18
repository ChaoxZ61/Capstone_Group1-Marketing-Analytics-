

DROP TABLE IF EXISTS [State]

CREATE TABLE [State](

    StateAbbreviation VARCHAR(2) NOT NULL PRIMARY KEY,
    StateName VARCHAR(50) NOT NULL,

    CONSTRAINT UQ_State_States
        UNIQUE(StateName,StateAbbreviation)

);



DROP TABLE IF EXISTS ZipCodeTable

CREATE TABLE ZipCodeTable(

    ZipCode INT NOT NULL PRIMARY KEY,
    StateAbbreviation VARCHAR(2) NOT NULL,
    MedianIncome INT,
    DegreePercentage FLOAT,

    CONSTRAINT fk_ZipTable_StateAbb
        FOREIGN KEY (StateAbbreviation)
        REFERENCES [State] (StateAbbreviation),
);



DROP TABLE IF EXISTS Unemployment

CREATE TABLE Unemployment(

    UnemploymentID INT NOT NULL PRIMARY KEY,
    StateAbbreviation VARCHAR(2) NOT NULL, 
    [Year] INT NOT NULL,
    [Month] INT NOT NULL,

    CONSTRAINT fk_Unemployment_StateAbb
        FOREIGN KEY (StateAbbreviation)
        REFERENCES [State] (StateAbbreviation),
);



DROP TABLE IF EXISTS CensusFood

CREATE TABLE CensusFood(
  
    CensusFoodID INT NOT NULL PRIMARY KEY,
    StateAbbreviation VARCHAR(2) NOT NULL,
    EstablishmentCount INT NOT NULL,
    Sales INT NOT NULL,
    FoodService VARCHAR(255) NOT NULL,

    CONSTRAINT fk_CensusFoodTable_StateID
        FOREIGN KEY (StateAbbreviation)
        REFERENCES [State] (StateAbbreviation),

);



DROP TABLE IF EXISTS Business

CREATE TABLE Business (

    BusinessID VARCHAR(255) PRIMARY KEY NOT NULL,
    Stars FLOAT NOT NULL,
    [Name] VARCHAR(255),
    ZipCode INT NOT NULL,  

    CONSTRAINT fk_ZipCodeTable_ZipCode
        FOREIGN KEY (ZipCode)
        REFERENCES ZipCodeTable (ZipCode),
);


DROP TABLE IF EXISTS [User]

CREATE TABLE [User](
    
    UserID VARCHAR(255) PRIMARY KEY NOT NULL,
    [Name] VARCHAR(255) NOT NULL,
    ReviewCount INT NOT NULL,
    YelpingSince DATE NOT NULL,
    Useful INT NOT NULL,
    Funny INT NOT NULL,
    Cool INT NOT NULL,
    Fans INT NOT NULL,
    AvgStars FLOAT NOT NULL,
    CompHot INT NOT NULL,
    CompMore INT NOT NULL,
    CompProfile INT NOT NULL,
    CompCute INT NOT NULL,
    CompList INT NOT NULL,
    CompNote INT NOT NULL,
    CompPlain INT NOT NULL,
    CompCool INT NOT NULL,
    CompFunny INT NOT NULL,
    CompWriter INT NOT NULL,
    CompPhotos INT NOT NULL,
);


DROP TABLE IF EXISTS Review

CREATE TABLE Review (

    ReviewID VARCHAR(255) PRIMARY KEY NOT NULL,
    UserID VARCHAR(255) NOT NULL,
    BusinessID VARCHAR(255) NOT NULL,
    Stars INT NOT NULL,
    [Date] Date NOT NULL,
    [Text] TEXT,
    Useful INT,
    Funny INT,
    Cool INT,

    CONSTRAINT fk_User_UserID
        FOREIGN KEY (UserID)
        REFERENCES [User] (UserID),

    CONSTRAINT fk_Review_BusinessID
        FOREIGN KEY (BusinessID)
        REFERENCES Business (BusinessID),
);



DROP TABLE IF EXISTS Attributes

CREATE TABLE Attributes (

    AttributesID INT PRIMARY KEY NOT NULL,
    AttributesName VARCHAR(255) NOT NULL,
);


DROP TABLE IF EXISTS AttributesValues 

CREATE TABLE AttributesValues(
    
    AttributesValuesID INT PRIMARY KEY NOT NULL,
    ValueName VARCHAR(255),
);



DROP TABLE IF EXISTS BusinessAttributes

CREATE TABLE BusinessAttributes (

    BusinessAttributesID INT PRIMARY KEY NOT NULL,
    BusinessID VARCHAR(255) NOT NULL,
    AttributesID INT NOT NULL,
    AttributesValuesID INT NOT NULL,

    CONSTRAINT fk_BusinessAttributes_BusinessID
        FOREIGN KEY (BusinessID)
        REFERENCES Business (BusinessID),

    CONSTRAINT fk_BusinessAttributes_AttributesID
        FOREIGN  KEY (AttributesID)
        REFERENCES Attributes (AttributesID),

    CONSTRAINT fk_BusinessAttributes_AttributesValuesID
        FOREIGN KEY (AttributesValuesID)
        REFERENCES  AttributesValues (AttributesValuesID)
);

DROP TABLE IF EXISTS Keywords

CREATE TABLE Keywords(
    best FLOAT NOT NULL,
    food FLOAT NOT NULL,
    ordered FLOAT NOT NULL,
    [did't] FLOAT NOT NULL,
    [order] FLOAT NOT NULL,
    [never] FLOAT NOT NULL,
    place FLOAT NOT NULL,
    [time] FLOAT NOT NULL,
    good FLOAT NOT NULL,
    great FLOAT NOT NULL,
    [service] FLOAT NOT NULL,
    [index] INT NOT NULL
)


-- If NEED TO DROP ALL TABLES

-- DROP TABLE IF EXISTS BusinessAttributes
-- DROP TABLE IF EXISTS Review
-- DROP TABLE IF EXISTS CensusFood
-- DROP TABLE IF EXISTS Unemployment
-- DROP TABLE IF EXISTS [State]
-- DROP TABLE IF EXISTS [User]
-- DROP TABLE IF EXISTS Business
-- DROP TABLE IF EXISTS ZipCode
-- DROP TABLE IF EXISTS Attributes
-- DROP TABLE IF EXISTS AttributesValues
-- DROP TABLE IF EXISTS ZipCodeTable