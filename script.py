import sqlite3
from sqlite3 import Error

############################################################################################################
############################################## CONNECTION ##################################################
############################################################################################################

# Path to the database file
database = "database.sqlite"
database = "/home/lampros/Coding Projects/DishPlanner/database.sqlite"

# Function to establish connection to the database
def create_connection(database):
    connection = None
    try:
        connection = sqlite3.connect(database)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

# Function to execute a query
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# Function to execute read queries
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

############################################################################################################
############################################## QUERIES #####################################################
############################################################################################################

# Function to insert a new dish
def insert_dish(connection, dish_name, description):
    query = f"""
    INSERT INTO Dishes(DishName, Description)
    VALUES('{dish_name}', '{description}');
    """
    execute_query(connection, query)

# Function to insert a new ingredient
def insert_ingredient(connection, ingredient_name):
    query = f"""
    INSERT INTO Ingredients(IngredientName)
    VALUES('{ingredient_name}');
    """
    execute_query(connection, query)

# Function to insert a new dish ingredient
def insert_dish_ingredient(connection, dish_id, ingredient_id, quantity_per_person):
    query = f"""
    INSERT INTO DishIngredients(DishID, IngredientID, QuantityPerPerson)
    VALUES({dish_id}, {ingredient_id}, {quantity_per_person});
    """
    execute_query(connection, query)

############################################################################################################
############################################## INPUT #######################################################
############################################################################################################

def input_dish_data(connection):
    # Prompt user for dish details
    dish_name = input("Enter the name of the dish: ")
    description = input("Enter the description of the dish: ")

    # Insert a new dish
    insert_dish(connection, dish_name, description)

    # Get the dish ID of the newly inserted dish (?)
    dish_id_query = f"""
    SELECT DishID FROM Dishes WHERE DishName = '{dish_name}';
    """
    dish_id = execute_read_query(connection, dish_id_query)[0][0] # [0][0] to get the first element of the first tuple

    # Prompt user for ingredients
    ingredients = input("Enter the ingredients of the dish (separated by commas): ").split(", ")

    # Insert ingredients and dish ingredients
    for ingredient in ingredients:
        ingredient = ingredient.strip() # Remove leading/trailing whitespaces
        insert_ingredient(connection, ingredient)
        ingredient_id_query = f"""
        SELECT IngredientID FROM Ingredients WHERE IngredientName = '{ingredient}';
        """
        ingredient_id = execute_read_query(connection, ingredient_id_query)[0][0]
        quantity_per_person = float(input(f"Enter the quantity of {ingredient} per person: "))
        insert_dish_ingredient(connection, dish_id, ingredient_id, quantity_per_person)


############################################################################################################
############################################## MAIN ########################################################
############################################################################################################

# Connect to the database
connection = create_connection(database)

# Input data
input_dish_data(connection)

# Close the connection
if connection:
    connection.close()
    print("The connection to the database has been closed.")
