-- Description: This file contains the schema for the database

-- Create Users table
CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY,
    Username TEXT,
    Email TEXT,
    PasswordHash TEXT
);


-- Create Dishes table
CREATE TABLE Dishes (
    DishID INTEGER PRIMARY KEY,
    DishName TEXT,
    Description TEXT
);

-- Create Ingredients table
CREATE TABLE Ingredients (
    IngredientID INTEGER PRIMARY KEY,
    IngredientName TEXT
);

-- Create DishIngredients table
CREATE TABLE DishIngredients (
    DishIngredientID INTEGER PRIMARY KEY,
    DishID INTEGER,
    IngredientID INTEGER,
    QuantityPerPerson REAL,
    FOREIGN KEY (DishID) REFERENCES Dishes(DishID),
    FOREIGN KEY (IngredientID) REFERENCES Ingredients(IngredientID)
);

-- Create UserSelections table
CREATE TABLE UserSelections (
    SelectionID INTEGER PRIMARY KEY,
    UserID INTEGER,
    DishID INTEGER,
    SelectionDate DATE,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (DishID) REFERENCES Dishes(DishID)
);
