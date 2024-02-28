import sqlite3
import datetime

conn = sqlite3.connect("expenses.db")
cur = conn.cursor()

while True:
    print("Select an option:")
    print("1. Enter a new expense")
    print("2. View expenses summary")
    
    choice = int(input())
    
    if choice == 1:
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        description = input("Enter the description of expense: ")
        
        cur.execute("SELECT DISTINCT category FROM expenses")
    elif choice == 2:
        pass
    else:
        exit()
        