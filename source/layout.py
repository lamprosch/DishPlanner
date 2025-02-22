import tkinter as tk
from tkinter import ttk
# from win32mica import ApplyMica, MicaTheme, MicaStyle
import sv_ttk

class appWindow(ttk.Frame):
    def __init__(self, master, controller):
        self.master = master
        self.master.geometry('1200x900') # Set window size
        self.master.minsize(600, 300) # Set minimum size
        self.master.title('WeekEats') # Set window title
        sv_ttk.set_theme('light') # Set theme

        self.createLayout() # Call the createLayout method 
        self.addWidgets() # Call the addWidgets method

    def createLayout(self):
        # Create the menu placeholder
        self.menuFrame = ttk.Frame(self.master)
        self.menuFrame.place(x=0, y=0, relwidth=0.3, relheight=1)
        # Create the page placeholder
        self.pageFrame = ttk.Frame(self.master)
        self.pageFrame.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        # Create the menu buttons placeholder
        self.menuButtonsFrame = ttk.Frame(self.menuFrame, style='Card.TFrame')
        self.menuButtonsFrame.place(x=8, y=10, relwidth=0.95, relheight=0.98)
        # # Create the page content placeholder
        # self.pageContentFrame = ttk.Frame(self.pageFrame, style='Card.TFrame')
        # self.pageContentFrame.place(x=0.3, y=5, relwidth=0.95, relheight=0.95)
        self.menuButtonsFrame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15), weight=1, uniform='a')
        self.menuButtonsFrame.columnconfigure((0), weight=1, uniform='a')



    def addWidgets(self):
        button_font = ('Segoe UI Semibold', 12)
        
        # Load icons
        self.myPlanButtonIcon = tk.PhotoImage(file='/home/lampros/Coding Projects/DishPlanner/icons/my_plan.png')
        self.myDishesButtonIcon = tk.PhotoImage(file='/home/lampros/Coding Projects/DishPlanner/icons/my_dishes.png')
        self.ingredientsButtonIcon = tk.PhotoImage(file='/home/lampros/Coding Projects/DishPlanner/icons/ingredients.png')
        self.shoppingListButtonIcon = tk.PhotoImage(file='/home/lampros/Coding Projects/DishPlanner/icons/shopping_list.png')

        # Create the menu buttons
        self.myPlanButton = tk.Button(self.menuButtonsFrame, activebackground='#EBEDF3', activeforeground='#1e1e1e', text='My Plan', anchor='w', font=button_font, image=self.myPlanButtonIcon, compound='left')
        self.myPlanButton.configure(borderwidth=0)
        self.myPlanButton.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        self.myDishes = tk.Button(self.menuButtonsFrame, activebackground='#EBEDF3', activeforeground='#1e1e1e', text='My Dishes', anchor='w', font=button_font, image=self.myDishesButtonIcon, compound='left')
        self.myDishes.configure(borderwidth=0)
        self.myDishes.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

        self.ingredients = tk.Button(self.menuButtonsFrame, activebackground='#EBEDF3', activeforeground='#1e1e1e', text='Ingredients', anchor='w', font=button_font, image=self.ingredientsButtonIcon, compound='left')
        self.ingredients.configure(borderwidth=0)
        self.ingredients.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')

        self.shoppingList = tk.Button(self.menuButtonsFrame, activebackground='#EBEDF3', activeforeground='#1e1e1e', text='Shopping List', anchor='w', font=button_font, image=self.shoppingListButtonIcon, compound='left')
        self.shoppingList.configure(borderwidth=0)
        self.shoppingList.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')
        # self.label = ttk.Label(self.menuFrame, background= 'green')
        # self.label.pack(expand=True, fill='both')
        # self.label = ttk.Label(self.pageFrame, background= 'red')
        # self.label.pack(expand=True, fill='both')
        # self.label = ttk.Label(self.menuButtonsFrame, background= 'yellow')
        # self.label.pack(expand=True, fill='both')
        # self.label = ttk.Label(self.pageContentFrame, background= 'yellow')
        # self.label.pack(expand=True, fill='both')

# class addNewDishScreen():

# class addNewIngredientScreen():

# class addNewMealPlanScreen():

# class viewIngredientsListScreen():

# class shoppingListScreen():

if __name__ == '__main__':
    root = tk.Tk()
    app = appWindow(root, None)
    root.mainloop()