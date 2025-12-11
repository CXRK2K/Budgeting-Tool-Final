'''
Final Project: Budgeting Tool interface
By Clark Barrett
12/11/2025
'''

#import class functions and special error exception
from FifThirTwentyManager import FifThirTwentyManager, OverBudgetError

#to run the program
def main():
    #pretty cosmetic line
    print('Budgeting Tool!\n-------------------')

    #object to handle all logic and data
    manager = FifThirTwentyManager()

    # ------ LOAD CSV or NEW FILE ------

    #ask for existing or new CSV filename
    filename = input('Enter budget CSV filename: ')

    #tries to use filename to load or create
    loaded = manager.load_from_csv(filename)

    #if filename doesn't exist, use filename for new CSV
    if not loaded:
        print('No CSV found. Creating new budget.\n')
        #calls function to create custom categories
        manager.create_custom_partitions()
    #if have existing CSV, use it
    else:
        print('Budget loaded from file.\n')

    #------ SET MONTHLY INCOME ------

    #if income not saved, need to set it
    if manager.get_income() == 0.0:
        #to check if valid income or not
        income_valid = False
        #repeats loop until valid income
        while not income_valid:
            #asks for monthly income and ends loop if True and valid
            try:
                income = float(input('Enter monthly income: '))
                income_valid = True
            #if input not valid, try again
            except ValueError:
                print('Please enter a numeric income.')

        #store valid income
        manager.set_income(income)
        
    #if already have valid saved income, use it
    else:
        print('Using saved monthly income: $' + str(manager.get_income()))
    
    #use method to calculate $ for each category
    manager.calculate_allocations()

    #prints budget overview
    print('\nCurrent Budget:')
    #use str method to show formatted string and info
    for name in manager.get_partitions():
        print(manager.get_partitions()[name]['object'])

    #------ ADD EXPENSES ------

    #for loop limiting
    more = 'yes'

    #if user says yes, continue loop. a no ends loop.
    while more.lower() == 'yes':
        #asks for expense category name to add to
        print('\nEnter a category to add an expense to.')
        cat = input('Category name: ')
        
        #check if numeric amt entered
        valid_amount = False
        while not valid_amount:
            #asks for amount spent
            try:
                amt = float(input('Enter amount spent: '))

                #add expense to category
                try:
                    manager.add_expense(cat, amt)
                    valid_amount = True

                #if over spending limit, raise custom error
                except OverBudgetError as e:
                    print(str(e))
                    print('Please enter a different amount.')

            #if numeric not entered, error and asks for number
            except ValueError:
                print('Please enter a numeric amount.')

        #asks if need to add more expenses
        more = input('Add another expense? (yes/no): ').lower()
        #if input is not yes or no, forces correct input
        while more != 'yes' and more != 'no':
            print('Please enter yes or no.')
            #continues to check if more or not
            more = input('Add another expense? (yes/no): ').lower()

    #------ FINAL SUMMARY ------

    #header for final summary
    print('\n--- Final Budget Summary ---')
    #loop and print each object/category, shows limit, spent, remaining
    for name in manager.get_partitions():
        print(manager.get_partitions()[name]['object'])

    #------ SAVE TO CSV ------

    #save_to_csv function to write data into file
    manager.save_to_csv(filename)
    print('\nBudget saved. Goodbye.')

#run main function
main()
