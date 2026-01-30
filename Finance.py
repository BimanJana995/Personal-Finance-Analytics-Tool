import pandas as pd
import os

def add_expense(date, category, desc, amount):
    data = {'Date': [date], 'Category': [category], 'Description': [desc], 'Amount': [amount]}
    df = pd.DataFrame(data)
    
    # Agar file pehle se hai toh usme add karo, nahi toh nayi banao
    if not os.path.isfile('finance_data.csv'):
        df.to_csv('finance_data.csv', index=False)
    else:
        df.to_csv('finance_data.csv', mode='a', index=False, header=False)
    print("Kharcha save ho gaya!")

# User se input lena
date = input("Date (DD-MM-YYYY): ")
cat = input("Category: ")
desc = input("Description: ")
amt = float(input("Amount: "))

add_expense(date, cat, desc, amt)