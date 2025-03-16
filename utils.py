import os
import datetime
import re

def clear_scr():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_category():

    categories = {
        1: "Food",
        2: "Travel",
        3: "Entertainment",
        4: "Utilities",
        5: "Shopping",
        6: "Miscellaneous"
    }

    print("\n\nEnter Category:", "\n1. Food", "\n2. Travel", 
              "\n3. Entertainment", "\n4. Utilities", "\n5. Shopping", "\n6. Miscellaneous")
        
    while True:
        try:
            choice = int(input("\n\nEnter your choice (1-6): "))

            if choice in categories:
                category = categories[choice]
                break
            else:
                print("Invalid choice. Please try again.")   
        except ValueError:
           print("Invalid Entry. Try a number. ")
    
    return category

def get_description(category):
    category_prompts = {
    "Food": "e.g., McDonald's, groceries, coffee, snacks",
    "Travel": "e.g., bus fare, flight ticket, Uber ride",
    "Entertainment": "e.g., movie ticket, concert, gaming, streaming",
    "Utilities": "e.g., electricity, water, gas, internet, phone bill",
    "Shopping": "e.g., clothing, electronics, furniture, books",
    "Miscellaneous": "e.g., gifts, donation, subscription, random purchases"
    }
    desc = input(f"Enter description ({category_prompts[category]}): ")
    desc = desc.strip().title()
    desc = re.sub(r'\s+', ' ', desc)
    return desc

def get_amount():

    while True:
        amount = input("Enter amount (in $): ")
        amount = amount.replace(",","")

        try:
            amount = float(amount)

            if amount < 0:
                print("Error - Negative amount. Please enter a positive amount.")
                continue
            else:
                break

        except ValueError:
            print("Invalid Amount. Try again. ")
    
    return round(amount,2)

def get_date():

    while True:
        date = input("Enter date mm-dd-yyyy (press Enter for today's date): ")

        if not date:
            return datetime.date.today().strftime('%m-%d-%Y')
        try: 
            return datetime.datetime.strptime(date, '%m-%d-%Y').strftime('%m-%d-%Y')
        
        except ValueError:
            print("Invalid Date. Try again. ")