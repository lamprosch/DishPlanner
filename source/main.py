import tkinter as tk
from controller import Controller
from gui import DishPlannerApp

def main():
    controller = Controller("/home/lampros/Coding Projects/DishPlanner/database.sqlite")
    root = tk.Tk()
    app = DishPlannerApp(root, controller)
    root.mainloop()
    controller.close_connection()

if __name__ == "__main__":
    main()