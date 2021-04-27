# Create a class "Category" and instantiate it with a different categories such as Food, Clothing and Car expenses e.t.c (You can also add more) 
# and their amounts.

# Define the following methods in the class: Deposit, Withdraw, Transfer, Check Balance (Feel free to add any other method)

# Your solution must be dynamic and re-useable, it must support more budget in the future.



# What we'll look out for when grading are
#Coding Conventions
#Proper use of Data Structures

class Budget:

    def __init__(self, category, amount): 
        self.category = category
        self.amount = amount

    def deposit(self, amount):  
        self.amount += amount
        return 'You have deposited {} into the {} budget'.format(amount, self.category) # the brackets are pulling the self.category and self.format, when you 
        # add .format and the attributes, it pulls the data into the correct order
 
    def budget_balance(self):
        return 'The current balance for the {} category is {}'.format(self.category, self.amount) # remember htat using self means you're pulling data from the database

    def check_balance(self, amount): 
        if amount > self.amount: #if the amount you entered in the system is greater than the amount you have in the system then
            return False # call this method in the withdraw function 
        else:
            return True
        
    def withdraw(self, amount): 

        if self.check_balance(amount): 
            self.amount -= amount
            return 'You have withdrawn {} from the {} budget'.format(amount, self.category) 

        else:
            return 'You do not have sufficient funds'

    def transfer(self, amount, category):
        #self.amount -= amount
        #call the category
        # it will take in the amount i want to transfer and the category it will transfer to 
        self.amount -= amount
        category.amount += amount 
        return 'You have transferred {} from the {} budget to deposit in the food budget'.format(amount, self.category) 
        

clothing_category = Budget('clothing', 1000)
food_category = Budget('food', 2000)
entertainment_category = Budget('entertainment', 3000)


print(food_category.deposit(250)) 
print(food_category.budget_balance())

print(entertainment_category.withdraw(350)) 
print(entertainment_category.budget_balance())

print(clothing_category.transfer(550, food_category)) 
print(clothing_category.budget_balance())
print(food_category.budget_balance())

