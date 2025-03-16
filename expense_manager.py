from utils import clear_scr, get_category, get_description, get_amount, get_date
from csv_handler import write_csv, read_csv, update_csv

def add_expense():
    
    while True:
        clear_scr()
        category = get_category()
        description = get_description(category)
        amount = get_amount()
        date = get_date()

        expense = {
            "category": category,
            "expense": description,
            "amount": amount,
            "date": date
        }

        write_csv(expense)
        print('\nExpense successfully added!')

        while True:
            add_another = input("\n\nWould you like to add another expense? (y/n): ").lower()
            if add_another in ['y', 'yes']:
                break  
            elif add_another in ['n', 'no']:
                return  
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")

def delete_expense():
    clear_scr()
    rows = read_csv()

    if not rows:
        print("\nNo expenses to delete.")
        return

    while True:

        print("\n\n" + "-" * 64)  
        print("-" * 64 + "\n")

        for i, row in enumerate(rows, start=1):  # `start=1` starts indexing from 1
            short_desc = row['Expense'][:12] + '...' if len(row['Expense']) > 15 else row['Expense']
            print(f"{i}. {row['Category'].ljust(15)} {short_desc.ljust(15)} {row['Amount'].ljust(15)} {row['Date'].ljust(15)}")
        
        print("\n" + "-" * 64)
        
        del_row = input("\n\nEnter row for deletion (or q to cancel): ").strip()

        if del_row == 'q':
            print("\nNo changes made.")
            return  # Exit without modifying the CSV
            
        try:
            del_row = int(del_row)
            if 1 <= del_row <= len(rows):
                del rows[del_row - 1]  # Remove the selected row
                update_csv(rows)  # Update the CSV only after a deletion
                print("\nRow successfully deleted.")

                # Ask if they want to delete another
                if input("Delete another? (y/n): ").strip().lower() not in ['y', 'yes']:
                    return  
            else:
                print("\nInvalid row number. Try again.")

        except ValueError:
            print("\nInvalid input. Please enter a valid number.")


def read_expenses():
    
    clear_scr()
    rows = read_csv()

    print("\nExpenses:\n")
    print("Category".ljust(15) + "Expense".ljust(15) + "Amount".ljust(15) + "Date".ljust(15))
    print("-" * 65)

    for row in rows:
        short_desc = row['Expense'][:12] + '...' if len(row['Expense']) > 15 else row['Expense']
        print(f"{row['Category'].ljust(15)} {short_desc.ljust(15)} {row['Amount'].ljust(15)} {row['Date'].ljust(15)}")

    print("\n")