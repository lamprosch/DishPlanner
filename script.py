import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import sv_ttk

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
    input_window.title("Add New Dish")
    input_window.geometry("375x667")
    sv_ttk.set_theme("light")

    # Create a frame to center the elements
    center_frame = ttk.Frame(input_window, padding=15, style="Card.TFrame")
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Dish name
    dish_name_entry = ttk.Entry(center_frame)
    dish_name_entry.insert(0, "Dish Name")
    dish_name_entry.grid(row=0, column=1, pady=5)

    # Description
    description_entry = ttk.Entry(center_frame)
    description_entry.insert(0, "Description")
    description_entry.grid(row=1, column=1, pady=5)

    # Seperator
    ttk.Separator(center_frame).grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

    def add_ingredients_form():
        # Hide initial form
        for widget in center_frame.winfo_children():
            widget.grid_remove()

        # Frame for dish name and description
        top_frame = ttk.Frame(input_window, padding=15)
        top_frame.place(x=10, y=10, anchor="nw")
        # Show dish name and description at the top left corner
        ttk.Label(top_frame, text=dish_name_entry.get(), font=("Segoe UI", 14, "bold")).grid(row=0, column=0, pady=5, sticky="w")
        ttk.Label(top_frame, text=description_entry.get(), font=("Segoe UI", 11)).grid(row=1, column=0, pady=5, sticky="w")

        # Frame for ingredients
        ingredients_frame = ttk.Frame(center_frame)
        ingredients_frame.grid(row=3, column=0, columnspan=2, pady=10)

        # Ingredient name
        ingredient_name_entry = ttk.Entry(center_frame)
        ingredient_name_entry.insert(0, "Ingredient Name")
        ingredient_name_entry.grid(row=4, column=0, pady=5)

        # Quantity
        quantity_entry = ttk.Entry(center_frame)
        quantity_entry.insert(0, "Quantity")
        quantity_entry.grid(row=5, column=0, pady=5)

        # Units dropdown
        units_var = tk.StringVar()
        units_dropdown = ttk.Combobox(center_frame, textvariable=units_var, width=max(ingredient_name_entry.cget("width"), quantity_entry.cget("width")))
        units_dropdown.set("Units")
        units_dropdown['values'] = ("g", "ml", "Table spoons", "Tea spoons", "Cups", "Pieces", "Cans", "Bundles", "Packages")
        units_dropdown.grid(row=6, column=0, pady=5)

        ingredients = []

        def add_new_ingredient():
            ingredient_name = ingredient_name_entry.get()
            quantity = quantity_entry.get()
            units = units_var.get()
            ingredients.append((ingredient_name, quantity, units))
            ingredient_name_entry.delete(0, tk.END)
            quantity_entry.delete(0, tk.END)
            units_var.set("")

            # Display added ingredients in real time
            for widget in ingredients_frame.winfo_children():
                widget.destroy()
            for index, (name, qty, unit) in enumerate(ingredients):
                ttk.Label(ingredients_frame, text=f"{name} - {qty} {unit}").grid(row=index, column=0, columnspan=2, pady=5)

        def save_dish():
            dish_name = dish_name_entry.get()
            description = description_entry.get()

            # Insert the dish
            insert_dish(connection, dish_name, description)

            # Get the dish ID of the newly inserted dish
            dish_id_query = f"SELECT DishID FROM Dishes WHERE DishName = '{dish_name}'"
            dish_id = execute_read_query(connection, dish_id_query)[0][0]

            # Insert ingredients and dish ingredients
            for ingredient_name, quantity, units in ingredients:
                insert_ingredient(connection, ingredient_name)
                ingredient_id_query = f"""
                SELECT IngredientID FROM Ingredients WHERE IngredientName = '{ingredient_name}';
                """
                ingredient_id = execute_read_query(connection, ingredient_id_query)[0][0]
                insert_dish_ingredient(connection, dish_id, ingredient_id, quantity)

            messagebox.showinfo("Success", "Dish added successfully!")
            input_window.destroy()

        # Add new ingredient button
        add_ingredient_button = ttk.Button(center_frame, text="Add New Ingredient", style="Accent.TButton", command=add_new_ingredient)
        add_ingredient_button.grid(row=7, column=0, columnspan=2, pady=10)

        # Save dish button
        save_dish_button = ttk.Button(center_frame, text="Save Dish", command=save_dish)
        save_dish_button.grid(row=8, column=0, columnspan=2, pady=10)

    # Add dish ingredients button
    add_ingredients_button = ttk.Button(center_frame, text="Add Dish Ingredients", style="Accent.TButton", command=add_ingredients_form)
    add_ingredients_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Cancel button
    cancel_button = ttk.Button(center_frame, text="Cancel", command=input_window.destroy)
    cancel_button.grid(row=5, column=0, columnspan=2, pady=10)

selected_dishes = []

def plan_menu(connection):
    # Create a new window
    show_window = tk.Toplevel()
    show_window.title("Plan Menu")
    show_window.geometry("375x667")
    sv_ttk.set_theme("light")

    # Create a frame to center the elements
    center_frame = ttk.Frame(show_window)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Get the dishes
    query = "SELECT DishID, DishName FROM Dishes"
    dishes = execute_read_query(connection, query)

    checkboxes = {}
    comboboxes = {}
    for dish in dishes:
        dish_id, dish_name = dish
        var = tk.IntVar()
        checkbox = ttk.Checkbutton(center_frame, text=f"{dish_id}. {dish_name}", variable=var)
        checkbox.grid(row=dish_id, column=0, sticky='w', pady=5)
        checkboxes[dish_id] = var
        
        # Get the ingredients for the dish
        ingredient_query = f"""
        SELECT Ingredients.IngredientName
        FROM DishIngredients
        JOIN Ingredients ON Ingredients.IngredientID
        WHERE DishIngredients.DishID = {dish_id};
        """
        ingredients = execute_read_query(connection, ingredient_query)
        ingredient_names = [ingredient[0] for ingredient in ingredients]

        # Create a combobox
        combobox = ttk.Combobox(center_frame, values=ingredient_names)
        combobox.grid(row=dish_id, column=1, pady=5)
        comboboxes[dish_id] = combobox

    def submit_selection():
        global selected_dishes
        selected_dishes = [dish_id for dish_id, var in checkboxes.items() if var.get() == 1]
        sv_ttk.set_theme("light")
        messagebox.showinfo("Selection", f"Selected Dishes: {selected_dishes}")
        show_window.destroy()

    # Submit button
    submit_button = ttk.Button(center_frame, text="Save meal plan", command=submit_selection)
    submit_button.grid(row=len(dishes) + 1, column=0, columnspan=2, pady=10)

def view_ingredients(connection):
    # Create a new window
    show_window = tk.Toplevel()
    show_window.title("View Ingredients")
    show_window.geometry("375x667")
    sv_ttk.set_theme("light")

    # Create a frame to center the elements
    center_frame = ttk.Frame(show_window)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Get the ingredients
    query = "SELECT IngredientID, IngredientName FROM Ingredients"
    ingredients = execute_read_query(connection, query)

    # Eliminate duplicates and ensure case-sansitive
    unique_ingredients = {}
    for ingredient_id, ingredient_name in ingredients:
        if ingredient_name not in unique_ingredients:
            unique_ingredients[ingredient_name] = ingredient_id

    for ingredient_name, ingredient_id in unique_ingredients.items():
        ttk.Label(center_frame, text=f"{ingredient_id}", width=10, anchor='w').pack(anchor="w", pady=5)
        ttk.Label(center_frame, text=f"{ingredient_name.capitalize()}", width=30, anchor='w').pack(anchor="w", pady=5)

# Function to extract the shopping list
def extract_shopping_list(connection):
    # Create a new window
    show_window = tk.Toplevel()
    show_window.title("Shopping List")
    show_window.geometry("375x667")
    sv_ttk.set_theme("light")

    # Create a frame to center the elements
    center_frame = ttk.Frame(show_window)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Get the ingredients for the selected dishes
    ingredients = []
    for dish_id in selected_dishes:
        query = f"""
        SELECT Ingredients.IngredientName, DishIngredients.QuantityPerPerson
        FROM DishIngredients
        JOIN Ingredients ON Ingredients.IngredientID = DishIngredients.IngredientID
        WHERE DishIngredients.DishID = {dish_id};
        """
        ingredients += execute_read_query(connection, query)

    for index, ingredient in enumerate(ingredients):
        ingredient_name, quantity = ingredient
        ttk.Label(center_frame, text=f"{index+1}. {ingredient_name} - {quantity}").pack(anchor="w", pady=5)

############################################################################################################
############################################## GUI #########################################################
############################################################################################################

# Draw GUI
def draw_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Dish Planner")
    root.geometry("375x667") # Set the window size
    sv_ttk.set_theme("light")

    # Create a frame to center the elements
    center_frame = ttk.Frame(root)
    center_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Create a sidebar
    sidebar = ttk.Frame(root, width=200, height=667)
    sidebar.grid(row=0, column=0, sticky="ns")
    sidebar.grid_propagate(False)
    sidebar.grid_remove()

    # Add buttons to the sidebar
    ttk.Button(sidebar, text="Button 1").pack(fill="x", pady=10)
    ttk.Button(sidebar, text="Button 2").pack(fill="x", pady=10)
    ttk.Button(sidebar, text="Button 3").pack(fill="x", pady=10)
    ttk.Button(sidebar, text="Button 4").pack(fill="x", pady=10)

    def toggle_sidebar():
        if sidebar.winfo_ismapped():
            sidebar.grid_remove()
        else:
            sidebar.grid()

    # Add burger icon
    burger_icon = tk.PhotoImage(file="icons/navigation.png")  # Ensure you have a burger_icon.png file in the same directory
    burger_button = ttk.Button(root, image=burger_icon, command=toggle_sidebar)
    burger_button.place(x=10, y=10)

    # Add Dish button
    add_dish_button = ttk.Button(center_frame, text="Add Dish", command=lambda: input_dish_data(connection)) # Lambda (?)
    add_dish_button.pack(fill="x", pady=10)

    # Add Plan Menu button
    plan_menu_button = ttk.Button(center_frame, text="Plan Menu", command=lambda: plan_menu(connection))
    plan_menu_button.pack(fill="x", pady=10)

    # Add View Ingredients button
    view_ingredients_button = ttk.Button(center_frame, text="View Ingredients", command=lambda: view_ingredients(connection))
    view_ingredients_button.pack(fill="x", pady=10)

    # Add Extract Shopping List button
    extract_shopping_list_button = ttk.Button(center_frame, text="View Shopping List", command=lambda: extract_shopping_list(connection))
    extract_shopping_list_button.pack(fill="x", pady=10)

    # Run the application
    root.mainloop()

############################################################################################################
############################################## MAIN ########################################################
############################################################################################################

# Connect to the database
connection = create_connection(database)

draw_gui()
# Close the connection
if connection:
    connection.close()
    print("The connection to the database has been closed.")
