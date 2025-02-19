import sqlite3

connection = sqlite3.connect("database.sqlite")

tables = ["Users", "Dishes", "Ingredients", "DishIngredients", "UserSelections"]
cursor = connection.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sqlite_sequence'")
sequense_table_exists = cursor.fetchone()

for table in tables:
    cursor.execute(f"DELETE FROM {table}")
    if sequense_table_exists:
        cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table}'") # Reset auto-increment

connection.commit()
print("Database emptied successfully")

connection.close()