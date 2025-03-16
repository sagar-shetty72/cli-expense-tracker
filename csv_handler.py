import csv
import os

headers = ['Category', 'Expense', 'Amount', 'Date']
filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'expenses.csv')

def write_csv(row):

    try:
        file_exists = os.path.isfile(filename)
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)

            if not file_exists:
                writer.writeheader()
            
            writer.writerow({'Category': row['category'], 
                             'Expense': row['expense'], 
                             'Amount': row['amount'], 
                             'Date': row['date']})
        
    
    except Exception as e:
        print(f"Error writing CSV: {e}")

def read_csv():

    try:
        with open(filename, newline='') as csvfile:
            return list(csv.DictReader(csvfile))
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []
    
def update_csv(rows):
    try:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(rows)

        print("\nChanges successfully saved to CSV.\n")

    except Exception as e:
        print(f"\n\nError writing to CSV: {e}")