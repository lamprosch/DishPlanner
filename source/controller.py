from database import Database

class Controller:
    def __init__(self, db_file):
        self.database = Database(db_file)

    def close_connection(self):
        self.database.close_connection()

    def insert_dish(self, dish_name, description):
        self.database.insert_dish(dish_name, description)

    def insert_ingredient(self, ingredient_name):
        self.database.insert_ingredient(ingredient_name)

    def insert_dish_ingredient(self, dish_id, ingredient_id, quantity_per_person):
        self.database.insert_dish_ingredient(dish_id, ingredient_id, quantity_per_person)

    def execute_read_query(self, query):
        return self.database.execute_read_query(query)