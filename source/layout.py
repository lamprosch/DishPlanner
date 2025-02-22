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
        self.currentFrame = None # Create a variable to store the current frame

    def createLayout(self):
        # Create the menu placeholder
        self.menuFrame = tk.Frame(self.master)
        self.menuFrame.place(x=0, y=0, relwidth=0.3, relheight=1)
        # Create the page placeholder
        self.pageFrame = tk.Frame(self.master)
        self.pageFrame.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        # Create the menu buttons placeholder
        self.menuButtonsFrame = ttk.Frame(self.menuFrame, style='Card.TFrame')
        self.menuButtonsFrame.place(x=8, y=6, relwidth=0.97, relheight=0.987)
        # Create the page content placeholder
        self.pageContentFrame = ttk.Frame(self.pageFrame, style='Card.TFrame')
        self.pageContentFrame.place(x=6, y=6, relwidth=0.985, relheight=0.987)

        # Configure the menu frame
        self.menuButtonsFrame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15), weight=1, uniform='a')
        self.menuButtonsFrame.columnconfigure((0), weight=1, uniform='a')


    # Draw the menu buttons
    def addWidgets(self):
        button_font = ('Segoe UI Semibold', 12)
        accent_color = '#F8F0C0'
        
        # Load icons
        self.myPlanButtonIcon = tk.PhotoImage(file='/home/lampros/Coding Projects/DishPlanner/icons/my_plan.png')
        self.myDishesButtonIcon = tk.PhotoImage(file='/home/lampros/Coding Projects/DishPlanner/icons/my_dishes.png')
        self.ingredientsButtonIcon = tk.PhotoImage(file='/home/lampros/Coding Projects/DishPlanner/icons/ingredients.png')
        self.shoppingListButtonIcon = tk.PhotoImage(file='/home/lampros/Coding Projects/DishPlanner/icons/shopping_list.png')
        self.settingsButtonIcon = tk.PhotoImage(file='/home/lampros/Coding Projects/DishPlanner/icons/settings.png')
        self.userProfileButtonIcon = tk.PhotoImage(file='/home/lampros/Coding Projects/DishPlanner/icons/user.png')

        # Create the "My Plan" button
        self.myPlanButton = tk.Button(self.menuButtonsFrame, activebackground=accent_color, activeforeground='#1e1e1e', text='My Plan', anchor='w', font=button_font, image=self.myPlanButtonIcon, compound='left', command=self.myPlanButtonClicked)
        self.myPlanButton.configure(borderwidth=0)
        self.myPlanButton.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        # Create the "My Dishes" button
        self.myDishes = tk.Button(self.menuButtonsFrame, activebackground=accent_color, activeforeground='#1e1e1e', text='My Dishes', anchor='w', font=button_font, image=self.myDishesButtonIcon, compound='left', command=self.myDishesButtonClicked)
        self.myDishes.configure(borderwidth=0)
        self.myDishes.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')

        # Create the "Ingredients" button
        self.ingredients = tk.Button(self.menuButtonsFrame, activebackground=accent_color, activeforeground='#1e1e1e', text='Ingredients', anchor='w', font=button_font, image=self.ingredientsButtonIcon, compound='left', command=self.ingredientsButtonClicked)
        self.ingredients.configure(borderwidth=0)
        self.ingredients.grid(row=2, column=0, padx=5, pady=5, sticky='nsew')

        # Create the "Shopping List" button
        self.shoppingList = tk.Button(self.menuButtonsFrame, activebackground=accent_color, activeforeground='#1e1e1e', text='Shopping List', anchor='w', font=button_font, image=self.shoppingListButtonIcon, compound='left', command=self.shoppingListButtonClicked)
        self.shoppingList.configure(borderwidth=0)
        self.shoppingList.grid(row=3, column=0, padx=5, pady=5, sticky='nsew')

        # Create the "Settings" button
        self.settings = tk.Button(self.menuButtonsFrame, activebackground=accent_color, activeforeground='#1e1e1e', text='Settings', anchor='w', font=button_font, image=self.settingsButtonIcon, compound='left', command=self.settingsButtonClicked)
        self.settings.configure(borderwidth=0)
        self.settings.grid(row=14, column=0, padx=5, pady=5, sticky='nsew')

        # Create the "User Profile" button
        self.userProfile = tk.Button(self.menuButtonsFrame, activebackground=accent_color, activeforeground='#1e1e1e', text='User Profile', anchor='w', font=button_font, image=self.userProfileButtonIcon, compound='left', command=self.userProfileButtonClicked)
        self.userProfile.configure(borderwidth=0)
        self.userProfile.grid(row=15, column=0, padx=5, pady=5, sticky='nsew')

        self.menuButtonsList = [self.myPlanButton, self.myDishes, self.ingredients, self.shoppingList, self.settings, self.userProfile]

    # Configure menu buttons behavior
    def myPlanButtonClicked(self):
        for button in self.menuButtonsList:
            button.configure(bg='#ffffff')
        self.myPlanButton.configure(bg='#F8F0C0')

    def myDishesButtonClicked(self):
        for button in self.menuButtonsList:
            button.configure(bg='#ffffff')
        self.myDishes.configure(bg='#F8F0C0')

    def ingredientsButtonClicked(self):
        for button in self.menuButtonsList:
            button.configure(bg='#ffffff')
        self.ingredients.configure(bg='#F8F0C0')

    def shoppingListButtonClicked(self):
        for button in self.menuButtonsList:
            button.configure(bg='#ffffff')
        self.shoppingList.configure(bg='#F8F0C0')

    def settingsButtonClicked(self):
        for button in self.menuButtonsList:
            button.configure(bg='#ffffff')
        self.settings.configure(bg='#F8F0C0')

    def userProfileButtonClicked(self):
        for button in self.menuButtonsList:
            button.configure(bg='#ffffff')
        self.userProfile.configure(bg='#F8F0C0')

# class addNewDishScreen():

# class addNewIngredientScreen():

# class addNewMealPlanScreen():

# class viewIngredientsListScreen():

# class shoppingListScreen():

if __name__ == '__main__':
    root = tk.Tk()
    app = appWindow(root, None)
    root.mainloop()