# Personal Expense Tracker 💰

A simple, lightweight command-line application built in Python to track daily expenses. It features persistent data storage using JSON and robust exception handling.

## Features
* **Add Expenses:** Record transactions by entering an amount, category, and description.
* **View Expenses:** Display all your recorded expenses directly in the terminal.
* **Data Persistence:** Automatically saves your data to a local `expenses.json` file so nothing is lost when you close the program.
* **Error Handling:** Uses `try-except` blocks to gracefully handle missing files on first-time runs.

## Prerequisites
* Python 3.x installed on your machine.
* No external libraries or pip installations are required (uses Python built-in `json` module).

## How to Run
1. Clone the repository or download the source code.
2. Open your terminal or command prompt in the project directory.
3. Run the script using the following command:
   ```bash
   python miniproject1.py