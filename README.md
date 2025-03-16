# CLI Expense Tracker

A lightweight, command-line-based expense tracker for quickly logging and managing daily expenses. This tool allows users to add, view, and delete expenses while keeping records in a CSV file.

## Features
- Add expenses with categories, descriptions, amounts, and dates.
- View a formatted list of all recorded expenses.
- Delete specific expenses by selecting from a list.
- Data is stored in a CSV file for easy access and modification.

## Future Improvements
- **Search & Filter**: Find specific expenses based on keywords, categories, or date ranges.
- **Sorting**: Sort expenses by date, amount, or category for better insights.
- **Enhanced Data Manipulation**: Edit and update existing expenses instead of just deleting them.
- **SQLite Integration**: Move from CSV storage to a structured SQLite database for better scalability and querying.

## Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. Follow the menu prompts to add, view, or delete expenses.

## Requirements
- Python 3.x
- `csv` (built-in module)
- `os` (built-in module)

## Contributing
Feel free to fork this repository and submit pull requests for new features or improvements.
