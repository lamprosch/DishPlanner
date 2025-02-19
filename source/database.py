import sqlite3
from sqlite3 import Error

# Database class to connect to the database and execute queries
class Database:
    def __init__(self, db_file):
        self.connection = self.create_connection(db_file)

    # Function to connect to the database
    def create_connection(self, db_file):
        connection = None
        try:
            connection = sqlite3.connect(db_file)
            print("Connection to SQLite DB successful")
        except Error as e:
            print(f"The error '{e}' occurred")
        return connection
    
    # Function to execute a query
    def execute_query(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"The error '{e}' occurred")

    # Function to execute read queries
    def execute_read_query(self, query):
        cursor = self.connection.cursor()
        result = None
        try:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        except Error as e:
            print(f"The error '{e}' occurred")

    # Function to close the connection
    def close_connection(self):
        if self.connection:
            self.connection.close()
            print("Connection to Database has been closed")

    # Function to add a new dish to the database
    def insert_dish(self, dish_name, description):
        query = f"""
        INSERT INTO Dishes(DishName, Description)
        VALUES('{dish_name}', '{description}');
        """
        self.execute_query(query)

    # Function to add a new ingredient to the database
    def insert_ingredient(self, ingredient_name):
        query = f"""
        INSERT INTO Ingredients(IngredientName)
        VALUES('{ingredient_name}');
        """
        self.execute_query(query)

    # Function to add a dish ingredient to the database
    def insert_dish_ingredient(self, dish_id, ingredient_id, quantity_per_person):
        query = f"""
        INSERT INTO DishIngredients(DishID, IngredientID, QuantityPerPerson)
        VALUES({dish_id}, {ingredient_id}, {quantity_per_person});
        """
        self.execute_query(query)