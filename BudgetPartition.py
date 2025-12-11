'''
Budgeting Tool Final Project Class 1/2
By Clark Barrett
12/11/2025
'''

class BudgetPartition:

    def __init__(self, name):
        self.name = name #partition name
        self.allocated_amount = 0.0 #category spending limit
        self.actual_spending = 0.0 #how much has been spent

    #--------GETTERS---------
        
    #returns budget partition category name
    def get_name(self):
        return self.name

    #returns budget partition limit
    def get_allocated_amount(self):
        return self.allocated_amount

    #returns current spending
    def get_actual_spending(self):
        return self.actual_spending
    
    #returns remaining amount for spending
    def get_remaining_amount(self):
        return self.allocated_amount - self.actual_spending

    #--------SETTERS---------

    #sets existing spending, used for CSV file loading
    def set_actual_spending(self, amount):
        self.actual_spending = amount

    #sets budget partition limit
    def set_allocated_amount(self, amount):
        self.allocated_amount = amount
        
    #------ADD SPENDING------

    #add a completed transaction/expense
    def add_spending(self, amount):
        self.actual_spending = self.actual_spending + amount

    #------LIMIT CHECK-------

    #determines whether user is over spending limit
    def is_over_limit(self):
        return self.actual_spending > self.allocated_amount

    #------PRINTABLE SUMMARY MAGIC METHOD------

    #returns a formatted string for a budget category (limit, spent, remaining)
    def __str__(self):
        return (self.name + ' - Limit: $' + str(round(self.allocated_amount, 2))
                + ', Spent: $' + str(round(self.actual_spending, 2))
                + ', Remaining: $' + str(round(self.get_remaining_amount(), 2)))
