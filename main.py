from expense_manager import add_expense, delete_expense, read_expenses
from utils import clear_scr
from logo import logo

def main():

    clear_scr()
    print(logo)

    while True:
        print("\n" + "="*20)
        print("    MENU    ")
        print("="*20)
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expenses")
        print("4. Exit")
        print("="*20)

        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            print("\nAdding expenses...")
            add_expense()
        elif choice == 2:
            print("\nReading expenses...")
            read_expenses()
        elif choice == 3:
            print("\nDeleting expenses...")
            try:
                delete_expense()
            except Exception as e:
                print("ERROR:", e)
                input("Press Enter to return to the menu...")

        elif choice == 4:
            clear_scr()
            break
        else:
            print('\nInvalid choice. Please choose an option.')
            continue

if __name__ == "__main__":
    main()
