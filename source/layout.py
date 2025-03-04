import tkinter as tk
from tkinter import ttk
from win32mica import ApplyMica, MicaTheme, MicaStyle
import sv_ttk
import pywinstyles, sys
import ctypes

# Set DPI awareness for better appearance on Windows
try: ctypes.windll.shcore.SetProcessDpiAwareness(True)
except Exception as e:
    print(f"Failed to set DPI awareness: {e}")

class appWindow(ttk.Frame):
    def __init__(self, master, controller):
        self.master = master
        self.master.geometry('1200x800') # Set window size
        self.master.minsize(600, 300) # Set minimum size
        self.master.title('WeekEats') # Set window title
        sv_ttk.set_theme('light') # Set theme
        self.apply_theme_to_titlebar() # Apply theme to title bar
        self.button_font = ('Segoe UI', 17, )
        self.accent_color = '#eaeaea'

        # Apply Mica theme
        hwnd = self.master.winfo_id()
        ApplyMica(HWND=hwnd, Theme=MicaTheme.LIGHT, Style=MicaStyle.DEFAULT)

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
        self.menuButtonsFrame.place(x=6, y=6, relwidth=0.97, relheight=0.98)
        # Create the page content placeholder
        self.pageContentFrame = ttk.Frame(self.pageFrame, style='Card.TFrame')
        self.pageContentFrame.place(x=6, y=6, relwidth=0.98, relheight=0.98)

        # Configure the menu frame
        self.menuButtonsFrame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12,13), weight=1, uniform='a')
        self.menuButtonsFrame.columnconfigure((0), weight=1, uniform='a')


    # Draw the menu buttons
    def addWidgets(self):
        # Load icons
        self.myPlanButtonIcon = tk.PhotoImage(file='/DishPlanner/icons/my_plan.png')
        self.myDishesButtonIcon = tk.PhotoImage(file='/DishPlanner/icons/my_dishes.png')
        self.ingredientsButtonIcon = tk.PhotoImage(file='/DishPlanner/icons/ingredients.png')
        self.shoppingListButtonIcon = tk.PhotoImage(file='/DishPlanner/icons/shopping_list.png')
        self.settingsButtonIcon = tk.PhotoImage(file='/DishPlanner/icons/settings.png')
        self.userProfileButtonIcon = tk.PhotoImage(file='/DishPlanner/icons/user.png')

        # Create the "My Plan" button
        self.myPlanButton = tk.Button(self.menuButtonsFrame, activebackground=self.accent_color, activeforeground='#1e1e1e', text='  My Plan', anchor='w', font=self.button_font, image=self.myPlanButtonIcon, compound='left', command=self.myPlanButtonClicked)
        self.myPlanButton.configure(borderwidth=0)
        self.myPlanButton.grid(row=0, column=0, padx=5, pady=5, sticky='nsew')

        # Create the "My Dishes" button
        self.myDishes = tk.Button(self.menuButtonsFrame, activebackground=self.accent_color, activeforeground='#1e1e1e', text='  My Dishes', anchor='w', font=self.button_font, image=self.myDishesButtonIcon, compound='left', command=self.myDishesButtonClicked)
        self.myDishes.configure(borderwidth=0)
        self.myDishes.grid(row=1, column=0, padx=3, pady=3, sticky='nsew')

        # Create the "Ingredients" button
        self.ingredients = tk.Button(self.menuButtonsFrame, activebackground=self.accent_color, activeforeground='#1e1e1e', text='  Ingredients', anchor='w', font=self.button_font, image=self.ingredientsButtonIcon, compound='left', command=self.ingredientsButtonClicked)
        self.ingredients.configure(borderwidth=0)
        self.ingredients.grid(row=2, column=0, padx=3, pady=3, sticky='nsew')

        # Create the "Shopping List" button
        self.shoppingList = tk.Button(self.menuButtonsFrame, activebackground=self.accent_color, activeforeground='#1e1e1e', text='  Shopping List', anchor='w', font=self.button_font, image=self.shoppingListButtonIcon, compound='left', command=self.shoppingListButtonClicked)
        self.shoppingList.configure(borderwidth=0)
        self.shoppingList.grid(row=3, column=0, padx=3, pady=3, sticky='nsew')

        # Create the "Settings" button
        self.settings = tk.Button(self.menuButtonsFrame, activebackground=self.accent_color, activeforeground='#1e1e1e', text='  Settings', anchor='w', font=self.button_font, image=self.settingsButtonIcon, compound='left', command=self.settingsButtonClicked)
        self.settings.configure(borderwidth=0)
        self.settings.grid(row=12, column=0, padx=3, pady=3, sticky='nsew')

        # Create the "User Profile" button
        self.userProfile = tk.Button(self.menuButtonsFrame, activebackground=self.accent_color, activeforeground='#1e1e1e', text='  User Profile', anchor='w', font=self.button_font, image=self.userProfileButtonIcon, compound='left', command=self.userProfileButtonClicked)
        self.userProfile.configure(borderwidth=0)
        self.userProfile.grid(row=13, column=0, padx=3, pady=3, sticky='nsew')

        self.menuButtonsList = [self.myPlanButton, self.myDishes, self.ingredients, self.shoppingList, self.settings, self.userProfile]

        # Bind hover effect to menu buttons
        for button in self.menuButtonsList:
            button.bind("<Enter>", lambda e: e.widget.configure(bg=self.accent_color))
            button.bind("<Leave>", lambda e: e.widget.configure(bg='#fafafa'))

    # Destroy the current frame
    def emptyContentFrame(self, pageContentFrame):
        for widget in pageContentFrame.winfo_children():
            widget.destroy()

    # Configure menu buttons behavior
    def myPlanButtonClicked(self):
        self.emptyContentFrame(self.pageContentFrame)
        for button in self.menuButtonsList:
            button.configure(bg='#fafafa')
        self.myPlanButton.configure(bg=self.accent_color)
        self.currentFrame = myPlanScreen(self.pageContentFrame)

    def myDishesButtonClicked(self):
        self.emptyContentFrame(self.pageContentFrame)
        for button in self.menuButtonsList:
            button.configure(bg='#fafafa')
        self.myDishes.configure(bg=self.accent_color)
        self.currentFrame = myDishesScreen(self.pageContentFrame)

    def ingredientsButtonClicked(self):
        self.emptyContentFrame(self.pageContentFrame)
        for button in self.menuButtonsList:
            button.configure(bg='#fafafa')
        self.ingredients.configure(bg=self.accent_color)
        self.currentFrame = ingredientsScreen(self.pageContentFrame)

    def shoppingListButtonClicked(self):
        self.emptyContentFrame(self.pageContentFrame)
        for button in self.menuButtonsList:
            button.configure(bg='#fafafa')
        self.shoppingList.configure(bg=self.accent_color)
        self.currentFrame = shoppingListScreen(self.pageContentFrame)

    def settingsButtonClicked(self):
        self.emptyContentFrame(self.pageContentFrame)
        for button in self.menuButtonsList:
            button.configure(bg='#fafafa')
        self.settings.configure(bg=self.accent_color)
        self.currentFrame = settingsScreen(self.pageContentFrame)

    def userProfileButtonClicked(self):
        self.emptyContentFrame(self.pageContentFrame)
        for button in self.menuButtonsList:
            button.configure(bg='#fafafa')
        self.userProfile.configure(bg=self.accent_color)
        self.currentFrame = userProfileScreen(self.pageContentFrame)

    def apply_theme_to_titlebar(self):
        version = sys.getwindowsversion()

        if version.major == 10 and version.build >= 22000:
            # Set the title bar color to the background color on Windows 11 for better appearance
            if sv_ttk.get_theme() == "dark":
                pywinstyles.change_header_color(self.master, color="#1c1c1c")
                sv_ttk.set_theme('dark')

class myPlanScreen():
    def __init__(self, parent):
        self.parent = parent
        self.createLayout()

    def createLayout(self):
        # Create header frame
        self.headerFrame = tk.Frame(self.parent)
        self.headerFrame.place(x=0, y=0, relwidth=1, relheight=0.07)
        # Create header title
        self.titleLabel = ttk.Label(self.headerFrame, text="My Plan", font=('Segoe UI', 24, 'bold'))
        self.titleLabel.place(x=7, rely=0.5, anchor='w')

class myDishesScreen:
    def __init__(self, parent):
        self.parent = parent
        self.createLayout()

    def createLayout(self):
        # Create header frame
        self.headerFrame = tk.Frame(self.parent)
        self.headerFrame.place(x=0, y=0, relwidth=1, relheight=0.07)
        # Create header title
        self.titleLabel = ttk.Label(self.headerFrame, text="My Dishes", font=('Segoe UI', 24, 'bold'))
        self.titleLabel.place(x=7, rely=0.5, anchor='w')

        # Create content frame
        self.contentFrame = tk.Frame(self.parent)
        self.contentFrame.place(x=0, rely=0.07, relwidth=1, relheight=0.86)
        # Create scrollable canvas
        self.canvas = tk.Canvas(self.contentFrame)
        self.canvas.pack(fill='both', expand=True)
        # Create scrollbar
        self.scrollbar = ttk.Scrollbar(self.canvas, orient='vertical',command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y')
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        #Create ingredients frame
        self.dishesFrame = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.dishesFrame, anchor='nw', width=self.parent.winfo_width() - 25)
        
        # Create ingredients list
        self.fillDishesList()
            
        # Bind mouse wheel to scroll
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(-1 * (e.delta // 120), "units"))


        # Create footer frame
        self.footerFrame = tk.Frame(self.parent)
        self.footerFrame.place(x=0, rely=0.93, relwidth=1, relheight=0.07)
        # Create add new dish button
        self.addNewDishButtonIcon = tk.PhotoImage(file='/DishPlanner/icons/plus.png')
        self.addNewDishButton = ttk.Button(self.footerFrame, image=self.addNewDishButtonIcon, style='TButton')
        self.addNewDishButton.place(relx=0.993, rely=0.5, anchor='e', width=90, height=45)

    def fillDishesList(self):
        self.editDishButtonIcon = tk.PhotoImage(file='/DishPlanner/icons/edit.png')
        self.deleteDishButtonIcon = tk.PhotoImage(file='/DishPlanner/icons/delete.png')

        for i in range(12):
            self.dishItem = ttk.Label(self.dishesFrame, text=f'Dish {i+1}', font=('Segoe UI', 17), background= "#f8f7f9", padding=(22, 22))
            self.editButton = ttk.Button(self.dishItem, image=self.editDishButtonIcon, style='TButton')
            self.deleteButton = ttk.Button(self.dishItem, image=self.deleteDishButtonIcon, style='TButton', command=lambda item=self.dishItem: self.deleteButtonClicked(item))
            self.editButton.place(relx=0.91, rely=0.5, anchor='e', width=45, height=40)
            self.deleteButton.place(relx=0.99, rely=0.5, anchor='e', width=45, height=40)
            self.dishItem.pack(padx=3, pady=2, fill='x')  
             # Bind hover effect to menu buttons
            self.dishItem.bind("<Enter>", lambda e: e.widget.configure(background="#eaeaea"))
            self.dishItem.bind("<Leave>", lambda e: e.widget.configure(background='#f8f7f9'))

        # Update scrollbar visibility
        updateScrollbarVisibility(self.scrollbar, self.dishesFrame)

    def deleteButtonClicked(self, item):
        # Remove dish from database
        item.destroy()
        updateScrollbarVisibility(self.scrollbar, self.dishesFrame)

class ingredientsScreen():
    def __init__(self, parent):
        self.parent = parent
        self.createLayout()

    def createLayout(self):
        # Create header frame
        self.headerFrame = tk.Frame(self.parent)
        self.headerFrame.place(x=0, y=0, relwidth=1, relheight=0.07)
        # Create header title
        self.titleLabel = ttk.Label(self.headerFrame, text="Ingredients", font=('Segoe UI', 24, 'bold'))
        self.titleLabel.place(x=7, rely=0.5, anchor='w')

        # Create content frame
        self.contentFrame = tk.Frame(self.parent)
        self.contentFrame.place(x=0, rely=0.07, relwidth=1, relheight=0.86)
        # Create scrollable canvas
        self.canvas = tk.Canvas(self.contentFrame)
        self.canvas.pack(fill='both', expand=True)
        # Create scrollbar
        self.scrollbar = ttk.Scrollbar(self.canvas, orient='vertical',command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y')
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        #Create ingredients frame
        self.ingredientsFrame = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.ingredientsFrame, anchor='nw', width=self.parent.winfo_width() - 25)
        
        # Create ingredients list
        self.fillIngredientsList()
            
        # Bind mouse wheel to scroll
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(-1 * (e.delta // 120), "units"))

        # Create footer frame
        self.footerFrame = tk.Frame(self.parent)
        self.footerFrame.place(x=0, rely=0.93, relwidth=1, relheight=0.07)
        # Create add new ingredient button
        self.addNewIngredientButtonIcon = tk.PhotoImage(file='/DishPlanner/icons/plus.png')
        self.addNewIngredientButton = ttk.Button(self.footerFrame, style='TButton', image=self.addNewIngredientButtonIcon)
        self.addNewIngredientButton.place(relx=0.96, rely=0.6, anchor='e', width=110, height=40)

    def fillIngredientsList(self):
        self.editIngredientButtonIcon = tk.PhotoImage(file='/DishPlanner/icons/edit.png')
        self.deleteIngredientButtonIcon = tk.PhotoImage(file='/DishPlanner/icons/delete.png')

        for i in range(7):
            self.ingredientItem = ttk.Label(self.ingredientsFrame, text=f'Ingredient {i+1}', font=('Segoe UI', 17), background= "#f8f7f9", padding=(22, 22))
            self.editButton = ttk.Button(self.ingredientItem, image=self.editIngredientButtonIcon, style='TButton')
            self.deleteButton = ttk.Button(self.ingredientItem, image=self.deleteIngredientButtonIcon, style='TButton', command=lambda item=self.ingredientItem: self.deleteButtonClicked(item))
            self.editButton.place(relx=0.91, rely=0.5, anchor='e', width=45, height=40)
            self.deleteButton.place(relx=0.99, rely=0.5, anchor='e', width=45, height=40)
            self.ingredientItem.pack(padx=3, pady=2, fill='x')
            # Bind hover effect to menu buttons
            self.ingredientItem.bind("<Enter>", lambda e: e.widget.configure(background="#eaeaea"))
            self.ingredientItem.bind("<Leave>", lambda e: e.widget.configure(background='#f8f7f9'))

        # Update scrollbar visibility
        updateScrollbarVisibility(self.scrollbar, self.ingredientsFrame)

    def deleteButtonClicked(self, item):
        item.destroy()

class shoppingListScreen():
    def __init__(self, parent):
        self.parent = parent
        self.createLayout()

    def createLayout(self):
        # Create header frame
        self.headerFrame = tk.Frame(self.parent)
        self.headerFrame.place(x=0, y=0, relwidth=1, relheight=0.07)
        # Create header title
        self.titleLabel = ttk.Label(self.headerFrame, text="Shopping List", font=('Segoe UI', 24, 'bold'))
        self.titleLabel.place(x=7, rely=0.5, anchor='w')

        # Create content frame
        self.contentFrame = tk.Frame(self.parent)
        self.contentFrame.place(x=0, rely=0.07, relwidth=1, relheight=0.86)
        # Create scrollable canvas
        self.canvas = tk.Canvas(self.contentFrame)
        self.canvas.pack(fill='both', expand=True)
        # Create scrollbar
        self.scrollbar = ttk.Scrollbar(self.canvas, orient='vertical',command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side='right', fill='y')
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        #Create shopping list frame
        self.shoppingListFrame = tk.Frame(self.canvas)
        self.canvas.create_window((0,0), window=self.shoppingListFrame, anchor='nw', width=self.parent.winfo_width() - 25)
        
        # Create shopping list
        self.fillShoppingList()
            
        # Bind mouse wheel to scroll
        self.canvas.bind_all("<MouseWheel>", lambda e: self.canvas.yview_scroll(-1 * (e.delta // 120), "units"))

        # Create footer frame
        self.footerFrame = tk.Frame(self.parent)
        self.footerFrame.place(x=0, rely=0.93, relwidth=1, relheight=0.07)
        # Create add new shopping item button
        self.addNewShoppingItemButtonIcon = tk.PhotoImage(file='/DishPlanner/icons/plus.png')
        self.addNewShoppingItemButton = ttk.Button(self.footerFrame, style='TButton', image=self.addNewShoppingItemButtonIcon)
        self.addNewShoppingItemButton.place(relx=0.96, rely=0.6, anchor='e', width=110, height=40)


    def fillShoppingList(self):
        self.editShoppingItemButtonIcon = tk.PhotoImage(file='/DishPlanner/icons/edit.png')
        self.deleteShoppingItemButtonIcon = tk.PhotoImage(file='/DishPlanner/icons/delete.png')

        for i in range(6):
            self.shoppingItem = ttk.Label(self.shoppingListFrame, text=f'Shopping Item {i+1}', font=('Segoe UI', 17), background= "#f8f7f9", padding=(22, 22))
            self.editButton = ttk.Button(self.shoppingItem, image=self.editShoppingItemButtonIcon, style='TButton')
            self.deleteButton = ttk.Button(self.shoppingItem, image=self.deleteShoppingItemButtonIcon, style='TButton', command=lambda item=self.shoppingItem: self.deleButtonClicked(item))
            self.editButton.place(relx=0.91, rely=0.5, anchor='e', width=45, height=40)
            self.deleteButton.place(relx=0.99, rely=0.5, anchor='e', width=45, height=40)
            self.shoppingItem.pack(padx=3, pady=2, fill='x')
            # Bind hover effect to menu buttons
            self.shoppingItem.bind("<Enter>", lambda e: e.widget.configure(background="#eaeaea"))
            self.shoppingItem.bind("<Leave>", lambda e: e.widget.configure(background='#f8f7f9'))

        # Update scrollbar visibility
        updateScrollbarVisibility(self.scrollbar, self.shoppingListFrame)

    def deleButtonClicked(self, item):
        item.destroy()

class settingsScreen():
    def __init__(self, parent):
        self.parent = parent
        self.createLayout()

    def createLayout(self):
        # Create header frame
        self.headerFrame = tk.Frame(self.parent)
        self.headerFrame.place(x=0, y=0, relwidth=1, relheight=0.07)
        # Create header title
        self.titleLabel = ttk.Label(self.headerFrame, text="Settings", font=('Segoe UI', 24, 'bold'))
        self.titleLabel.place(x=7, rely=0.5, anchor='w')

class userProfileScreen():
    def __init__(self, parent):
        self.parent = parent
        self.createLayout()

    def createLayout(self):
        # Create header frame
        self.headerFrame = tk.Frame(self.parent)
        self.headerFrame.place(x=0, y=0, relwidth=1, relheight=0.07)
        # Create header title
        self.titleLabel = ttk.Label(self.headerFrame, text="User Profile", font=('Segoe UI', 24, 'bold'))
        self.titleLabel.place(x=7, rely=0.5, anchor='w')

# Utility functions
        
# Update scrollbar visibility based on the number of items in a frame
def updateScrollbarVisibility(scrollbar, frame, threshold=10):
    num_items = len(frame.winfo_children())
    if num_items < threshold:
        scrollbar.pack_forget()
    else:
        scrollbar.pack(side='right', fill='y')
    
if __name__ == '__main__':
    root = tk.Tk()
    root.tk.call('tk', 'scaling', 1.0)
    app = appWindow(root, None)
    root.mainloop()