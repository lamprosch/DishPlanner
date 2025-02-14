import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import simpledialog, messagebox

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
    # Create a new window
    input_window = tk.Toplevel()
    input_window.title("Add Dish")

    # Dish name
    tk.Label(input_window, text="Dish Name:").grid(row=0, column=0)
    dish_name_entry = tk.Entry(input_window)
    dish_name_entry.grid(row=0, column=1)

    # Description
    tk.Label(input_window, text="Description:").grid(row=1, column=0)
    description_entry = tk.Entry(input_window)
    description_entry.grid(row=1, column=1)

    # Ingredients
    tk.Label(input_window, text="Ingredients (comma-seperated):").grid(row=2, column=0)
    ingredients_entry = tk.Entry(input_window)
    ingredients_entry.grid(row=2, column=1)

    def submit_data():
        dish_name = dish_name_entry.get()
        description = description_entry.get()
        ingredients = ingredients_entry.get().split(",")

        # Insert the dish and its ingredients
        insert_dish(connection, dish_name, description)

        # Get the dish ID of the newly inserted dish
        dish_id_query = f"SELECT DishID FROM Dishes WHERE DishName = '{dish_name}'"
        dish_id = execute_read_query(connection, dish_id_query)[0][0]

        # Insert ingredients and dish ingredients
        for ingredient in ingredients:
            ingredient = ingredient.strip()
            insert_ingredient(connection, ingredient)
            ingredient_id_query = f"""
            SELECT IngredientID FROM Ingredients WHERE IngredientName = '{ingredient}';
            """
            ingredient_id = execute_read_query(connection, ingredient_id_query)[0][0]
            quantity_per_person = simpledialog.askfloat("Input", f"Enter the quantity per person for {ingredient}:")
            insert_dish_ingredient(connection, dish_id, ingredient_id, quantity_per_person)

        messagebox.showinfo("Success", "Dish added successfully!")
        input_window.destroy()

    # Submit button
    submit_button = tk.Button(input_window, text="Submit", command=submit_data)
    submit_button.grid(row=3, column=0,columnspan=2)

def view_dishes(connection):
    # Create a new window
    show_window = tk.Toplevel()
    show_window.title("View Dishes")

    # Get the dishes
    query = "SELECT DishID, DishName FROM Dishes"
    dishes = execute_read_query(connection, query)
    
    # Create a frame to hold the labels
    frame = tk.Frame(show_window)
    frame.pack(padx=10, pady=10)

    for dish in dishes:
        dish_id, dish_name = dish
        tk.Label(frame, text=f"{dish_id}", width=10, anchor='w').grid(row=dish_id, column=0, sticky='w')
        tk.Label(frame, text=f"{dish_name}", width=30, anchor='w').grid(row=dish_id, column=1, sticky='w')

def view_ingredients(connection):
    # Create a new window
    show_window = tk.Toplevel()
    show_window.title("View Ingredients")

    # Get the ingredients
    query = "SELECT IngredientID, IngredientName FROM Ingredients"
    ingredients = execute_read_query(connection, query)

    #Create a frame to hold the labels
    frame = tk.Frame(show_window)
    frame.pack(padx=10, pady=10)


    for ingredient in ingredients:
        ingredient_id, ingredient_name = ingredient
        tk.Label(frame, text=f"{ingredient_id}", width=10, anchor='w').grid(row=ingredient_id, column=0, sticky='w')
        tk.Label(frame, text=f"{ingredient_name}", width=30, anchor='w').grid(row=ingredient_id, column=1, sticky='w')
        
############################################################################################################
############################################## MAIN ########################################################
############################################################################################################

# Connect to the database
connection = create_connection(database)

# Create the main window
root = tk.Tk()
root.title("Dish Planner")
root.geometry("400x300") # Set the window size

# Add Dish button
add_dish_button = tk.Button(root, text="Add Dish", command=lambda: input_dish_data(connection)) # Lambda (?)
add_dish_button.pack(pady=20)

# Add View Dishes button
view_dishes_button = tk.Button(root, text="View Dishes", command=lambda: view_dishes(connection))
view_dishes_button.pack(pady=20)

# Add View Ingredients button
view_ingredients_button = tk.Button(root, text="View Ingredients", command=lambda: view_ingredients(connection))
view_ingredients_button.pack(pady=20)

# Run the application
root.mainloop()

# Close the connection
if connection:
    connection.close()
    print("The connection to the database has been closed.")
