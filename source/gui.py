import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import sv_ttk

class DishPlannerApp:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.selected_dishes = []
        self.current_frame = None
        self.draw_gui()

    def draw_gui(self):
        self.root.title("WeekEats")
        self.root.geometry("500x667")
        sv_ttk.set_theme("light")

        self.center_frame = ttk.Frame(self.root)
        self.center_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.sidebar = ttk.Frame(self.root, width=220, height=667)
        self.sidebar.place(x=0, y=50)  # Adjusted position to move it lower
        self.sidebar.grid_propagate(False)
        self.sidebar.grid_remove()  # Ensure sidebar starts hidden

        self.add_dish_button = ttk.Button(self.sidebar, text="Add New Dish", command=self.show_add_new_dish_screen)
        self.plan_menu_button = ttk.Button(self.sidebar, text="Plan Menu", command=self.show_plan_menu_screen)
        self.view_ingredients_button = ttk.Button(self.sidebar, text="View Ingredients List", command=self.show_ingredients_list_screen)
        self.view_shopping_list_button = ttk.Button(self.sidebar, text="View Shopping List", command=self.show_shopping_list_screen)

        # Initially hide the buttons
        self.add_dish_button.pack_forget()
        self.plan_menu_button.pack_forget()
        self.view_ingredients_button.pack_forget()
        self.view_shopping_list_button.pack_forget()

        nav_menu_icon = tk.PhotoImage(file="/home/lampros/Coding Projects/DishPlanner/icons/navigation.png")
        self.nav_menu_button = ttk.Button(self.root, image=nav_menu_icon, command=self.toggle_sidebar)
        self.nav_menu_button.place(x=10, y=10)
        self.nav_menu_button.image = nav_menu_icon

        self.show_home_screen()

    def toggle_sidebar(self):
        if self.sidebar.winfo_ismapped():
            self.sidebar.grid_remove()
            # Hide the buttons when sidebar is hidden
            self.add_dish_button.pack_forget()
            self.plan_menu_button.pack_forget()
            self.view_ingredients_button.pack_forget()
            self.view_shopping_list_button.pack_forget()
        else:
            self.sidebar.grid()
            self.sidebar.lift()  # Ensure sidebar is on top when shown
            # Show the buttons when sidebar is shown
            self.add_dish_button.pack(fill="x", pady=10)
            self.plan_menu_button.pack(fill="x", pady=10)
            self.view_ingredients_button.pack(fill="x", pady=10)
            self.view_shopping_list_button.pack(fill="x", pady=10)

    def show_home_screen(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = HomeScreen(self.center_frame, self)
        self.current_frame.pack(fill="both", expand=True)
        self.sidebar.grid_remove()  # Ensure sidebar is hidden when home screen is shown

    def show_add_new_dish_screen(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = AddNewDishScreen(self.root, self.controller)
        self.current_frame.pack(fill="both", expand=True)

    def show_plan_menu_screen(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = PlanMenuScreen(self.root, self.controller)
        self.current_frame.pack(fill="both", expand=True)

    def show_ingredients_list_screen(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = IngredientsListScreen(self.root, self.controller)
        self.current_frame.pack(fill="both", expand=True)

    def show_shopping_list_screen(self):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = ShoppingListScreen(self.root, self.controller)
        self.current_frame.pack(fill="both", expand=True)

class HomeScreen(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        nav_menu_icon = tk.PhotoImage(file="/home/lampros/Coding Projects/DishPlanner/icons/navigation.png")
        nav_menu_button = ttk.Button(self, image=nav_menu_icon, command=self.controller.toggle_sidebar)
        nav_menu_button.grid(row=0, column=0, padx=10)
        nav_menu_button.image = nav_menu_icon

class AddNewDishScreen(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.ingredients = []
        self.create_widgets()
        self.pack(fill="both", expand=True)

    def create_widgets(self):
        dish_name_entry = ttk.Entry(self)
        dish_name_entry.insert(0, "Dish Name")
        dish_name_entry.grid(row=0, column=1, pady=5)

        description_entry = ttk.Entry(self)
        description_entry.insert(0, "Description")
        description_entry.grid(row=1, column=1, pady=5)

        ttk.Separator(self).grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")

        add_ingredients_button = ttk.Button(self, text="Add Dish Ingredients", style="Accent.TButton", command=lambda: self.add_ingredients_form(dish_name_entry, description_entry))
        add_ingredients_button.grid(row=4, column=0, columnspan=2, pady=10)

        cancel_button = ttk.Button(self, text="Cancel", command=self.destroy)
        cancel_button.grid(row=5, column=0, columnspan=2, pady=10)
    
    def add_ingredients_form(self, dish_name_entry, description_entry):
        for widget in self.winfo_children():
            widget.grid_remove()

        top_frame = ttk.Frame(self, padding=15)
        top_frame.pack(fill="both", expand=True, side="top", pady=(50, 0))
        bottom_frame = ttk.Frame(self, padding=15)
        bottom_frame.pack(fill="both", expand=True, side="bottom")

        ttk.Label(top_frame, text=dish_name_entry.get(), font=("Segoe UI", 14, "bold")).pack(anchor="w", pady=5)
        ttk.Label(top_frame, text=description_entry.get(), font=("Segoe UI", 11)).pack(anchor="w", pady=5)

        ingredients_canvas = tk.Canvas(top_frame)
        ingredients_scrollbar = ttk.Scrollbar(top_frame, orient="vertical", command=ingredients_canvas.yview)
        ingredients_scrollable_frame = ttk.Frame(ingredients_canvas)

        ingredients_scrollable_frame.bind(
            "<Configure>",
            lambda e: ingredients_canvas.configure(
                scrollregion=ingredients_canvas.bbox("all")
            )
        )

        ingredients_canvas.create_window((0, 0), window=ingredients_scrollable_frame, anchor="nw")
        ingredients_canvas.configure(yscrollcommand=ingredients_scrollbar.set)

        ingredients_canvas.pack(side="left", fill="both", expand=True)
        ingredients_scrollbar.pack(side="right", fill="y")

        ingredient_name_entry = ttk.Entry(bottom_frame)
        ingredient_name_entry.insert(0, "Ingredient Name")
        ingredient_name_entry.pack(pady=5)

        quantity_entry = ttk.Entry(bottom_frame)
        quantity_entry.insert(0, "Quantity")
        quantity_entry.pack(pady=5)

        units_var = tk.StringVar()
        units_dropdown = ttk.Combobox(bottom_frame, width=16, textvariable=units_var)
        units_dropdown.set("Units")
        units_dropdown['values'] = ("g", "ml", "Table spoons", "Tea spoons", "Cups", "Pieces", "Cans", "Bundles", "Packages", "Bottles", "Bags")
        units_dropdown.pack(pady=5)

        def add_new_ingredient():
            ingredient_name = ingredient_name_entry.get()
            quantity = quantity_entry.get()
            units = units_var.get()
            self.ingredients.append((ingredient_name, quantity, units))
            ingredient_name_entry.delete(0, tk.END)
            ingredient_name_entry.insert(0, "Ingredient Name")
            quantity_entry.delete(0, tk.END)
            quantity_entry.insert(0, "Quantity")
            units_var.set("Units")

            for widget in ingredients_scrollable_frame.winfo_children():
                widget.destroy()
            for index, (name, qty, unit) in enumerate(self.ingredients):
                ttk.Label(ingredients_scrollable_frame, text=f"{name} - {qty} {unit}").pack(anchor="w", pady=5)

        def save_dish():
            dish_name = dish_name_entry.get()
            description = description_entry.get()

            self.controller.insert_dish(dish_name, description)

            dish_id_query = f"SELECT DishID FROM Dishes WHERE DishName = '{dish_name}'"
            dish_id = self.controller.execute_read_query(dish_id_query)[0][0]

            for ingredient_name, quantity, units in self.ingredients:
                self.controller.insert_ingredient(ingredient_name)
                ingredient_id_query = f"SELECT IngredientID FROM Ingredients WHERE IngredientName = '{ingredient_name}'"
                ingredient_id = self.controller.execute_read_query(ingredient_id_query)[0][0]
                self.controller.insert_dish_ingredient(dish_id, ingredient_id, quantity)

            messagebox.showinfo("Success", "Dish added successfully!")
            self.destroy()

        add_ingredient_button = ttk.Button(bottom_frame, text="Add New Ingredient", style="Accent.TButton", command=add_new_ingredient)
        add_ingredient_button.pack(pady=10)

        save_dish_button = ttk.Button(bottom_frame, text="Save Dish", command=save_dish)
        save_dish_button.pack(pady=10)

class PlanMenuScreen(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
        self.pack(fill="both", expand=True)

    def create_widgets(self):
        # Implementation of plan_menu method
        pass

class IngredientsListScreen(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
        self.pack(fill="both", expand=True)
    
    def create_widgets(self):
        # Implementation of view_ingredients method
        pass

class ShoppingListScreen(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.create_widgets()
        self.pack(fill="both", expand=True)
    
    def create_widgets(self):
        # Implementation of extract_shopping_list method
        pass