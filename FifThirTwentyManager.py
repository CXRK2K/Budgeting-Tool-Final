'''
Final Project Budgeting Tool Class 2/2
By Clark Barrett
12/11/2025
'''

#import BudgetPartition class
from BudgetPartition import BudgetPartition

#custom exception for category overspending
class OverBudgetError(Exception):
    pass

#Money/numbers managing class
class FifThirTwentyManager:

    def __init__(self):
        #stores income
        self.income = 0.0
        #holds budget categories
        self.partitions = {}

    #------GETTERS------

    #returns monthly income
    def get_income(self):
        return self.income

    #returns all BudgetPartition categories
    def get_partitions(self):
        return self.partitions

    #------SETTERS------

    #sets monthly income
    def set_income(self, amount):
        self.income = amount

    #creates partitions going up to 100%
    def create_custom_partitions(self):
        #user determines amt of categories
        num_parts = int(input('How many budget categories do you want? '))

        #uses loop and input to create amount and name of categories
        for i in range(num_parts):
            name = input('Enter the name of the partition ' + str(i+1) + ': ')

            #checks percentage
            valid = False
            while not valid:
                try:
                    #gets category percentage
                    percent = float(input(f'Enter the allocation percentage for {name}: '))
                    valid = True
                except:
                    #if not a number/float for percentage this error runs
                    print('Please enter a number.')

            #creates new budgetpartition object
            bp = BudgetPartition(name)

            #stores partition in dictionary
            self.partitions[name] = {
                'object': bp,
                'percentage': percent
            }

        #holds sum of all percentages to total 100% for categories
        total = 0

        #loops through partition names
        for name in self.partitions:
            #add to total percentage
            total = total + self.partitions[name]['percentage']

        #makes sure total of categories is 100% or else retry
        if total != 100:
            print('\n Error: Percentages must add up to exactly 100%.')
            print(f'You entered a total of: {total}.')
            print('Restarting partition setup...')

            #clears all partitions created to retry
            self.partitions = {}
            return self.create_custom_partitions()

    #------CALCULATE INCOME-BASED ALLOCATIONS------

    #calculates how much money each category gets
    def calculate_allocations(self):
        #loops through partitions dictionary
        for name in self.partitions:
            #get % for partition
            percent = self.partitions[name]['percentage']
            #calculates $ amount by income x %
            allocated = (percent/100)*self.income
            #stores $ allocation
            self.partitions[name]['object'].set_allocated_amount(allocated)

    #------ADDING CATEGORICAL EXPENSES------

    #add an expense to tracker/category
    def add_expense(self, partition_name, amount):
        #makes sure correct partition name is used or error
        if partition_name not in self.partitions:
            print('Category does not exist.')
            return

        #gets partition object for chosen category
        part = self.partitions[partition_name]['object']

        #checks to make sure spending is not over budget
        if part.get_actual_spending() + amount > part.get_allocated_amount():
            raise OverBudgetError(f'{partition_name} is over budget! Please try again.')

        #if within budget then add to actual_spending
        part.add_spending(amount)

    #------SAVE/LOAD CSV------

    #saves all to CSV file
    def save_to_csv(self, filename):

        #open file for writing/overwriting
        file = open(filename, 'w')

        #4 columns line for CSV file
        file.write('name,percent,allocated,spent\n')

        #store income permanently for whole CSV file
        file.write('INCOME,' + str(self.income) + ',0,0\n')

        # loops to write in one line per partition
        for name in self.partitions:
            #gets partition object for name
            part = self.partitions[name]['object']
            #gets percentage from partition
            percent = self.partitions[name]['percentage']

            #save name % and spent, builds csv line string and new line
            line = name + ',' + str(percent) + ',' + str(part.get_allocated_amount()) + ',' + str(part.get_actual_spending()) + '\n'
            #writes line to CSV file
            file.write(line)

        #saves data
        file.close()

        
    #loads all from CSV file
    def load_from_csv(self, filename):
        #open filename in read mode
        try:
            file = open(filename, 'r')
        #if file not found, this runs
        except:
            return False

        #reads and moves past header first line
        header = file.readline()

        #loop each line in file
        for line in file:
            #remove whitespace and split comma separated lines
            cols = line.strip().split(',')
            #first column, partition name or income
            name = cols[0]
            #income value or percentage
            percent = float(cols[1])
            #allocated amount
            allocated = float(cols[2])
            #actual spending amount
            spent = float(cols[3])

            #checks if line is income row
            if name == 'INCOME':
                #set manager income from % column
                try:
                    self.income = float(percent)
                #if conversion fails then fall back
                except:
                    self.income = 0.0
                #skip loop because not partition
                continue
            
            #create budgetpartition w given name
            bp = BudgetPartition(name)
            #set allocated amt based on CSV
            bp.set_allocated_amount(allocated)
            #set current spending based on CSV
            bp.set_actual_spending(spent)

            #store partition and % in partition dictionary
            self.partitions[name] = {
                'object': bp,
                'percentage': percent
            }

        #close after reading all lines
        file.close()

        #if dictionary is empty, error
        if len(self.partitions) == 0:
            return False

        #if have in dictionary, success
        return True
