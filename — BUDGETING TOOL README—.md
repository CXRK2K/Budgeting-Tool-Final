— BUDGETING TOOL – README—

BUDGETING TOOL

This is a simple monthly budgeting system that allows users to determine their budget categories. A more standard example would be 50% Needs, 30% Wants, 20% Savings. However, the user can create and name additional categories and determine the percentage allocation to each category as desired. They could create a 25% x 4 categories, or 20% x 5 categories, etc…

SCRIPT FILES INCLUDED:

- BudgetPartition.py  
- FifThirTwentyManager.py  
- main.py

SCRIPT FILE DESCRIPTIONS:

- **BudgetPartition.py** represents a single budget category. Each partition stores the following information: Category name, allocated monthly limit, actual spending, and remaining amount. BudgetPartition also includes getters and setters, as well as a \_\_str\_\_ magic method for clean summary printing at the end.

- **FifThirTwentyManager.py** controls the entire budgeting system. It stores the monthly income provided for the CSV file, creates and loads user-determined budget partitions, and calculates the allocations determined by the user. It also adds expenses to the correct category, raises the OverBudgetError when the spending limit is surpassed (see below). It saves and loads all data from a CSV file. The CSV file stores the following information: partition, allocated\_amount, and actual\_spending.

- **main.py** is the program the user runs. It loads any available data from FifThirTwenty manager and its corresponding CSV file. It will create a new budget if no corresponding CSV file is found. It prompts the user for their income, prints the current budget summary, allows the user to enter expenses, and saves all changes back to the CSV file.

HOW TO RUN THE PROGRAM

- Ensure ALL three script files are in the same folder.  
- If a CSV exists, ensure it is also in this folder.  
- Run main.py  
- Follow the on-screen prompts.

ERROR HANDLING

- The custom exception OverBudgetError is raised when you attempt to spend more than a category allows for. It will warn the user to enter an appropriate amount that equals what has already been spent for the specified category (e.g., Category Limit of 400, 200 spent; adding 300 will repeat the loop unless a number between 0 and 200 is entered to max out at the Category Limit of 400).

IMPORTANT THINGS TO KNOW

- If you do NOT have a CSV yet, the program will create one.  
- If you do not input the accurate filename for an existing CSV (excluding the .csv end), then the program will create a NEW file for the inputted CSV filename.