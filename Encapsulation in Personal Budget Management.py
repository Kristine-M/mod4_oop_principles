# task 1

class BudgetCategory:
    # Constructor and private attributes
    remaining_budget = "N/A"
    
    def __init__(self, name, budget):
        self.name = name
        self.__budget = budget
        
    # Getters and setters for category name and budget
    
    def set_name(self, new_name):
        self.name = new_name
        
    def get_name(self):
        return self.name
    
    def set_budegt(self, new_budget):
        
        if new_budget >= 0:
            self.__budget = new_budget
        else:
            print("Invalid budget value")
    
    def get_budget(self):
        return self.__budget

    def add_expense(self, amount):
        # Method to add an expense to the category
        if self.__budget - amount == 0:
            self.remaining_budget = 0
            print("Budget is capped. No more expenses")
            
        elif self.__budget - amount <= -1:
            print("Off Budget, can't pay this expense")
        else:
            self.remaining_budget = self.__budget - amount
            

    def display_category_summary(self):
        # Method to display the budget category details
        print("Catergory: ", self.name, "\nAllocated Budget: ", self.__budget, "\nRemaing Budget: ", self.remaining_budget)

# Example usage
food_category = BudgetCategory("Food", 500)
new_cat = BudgetCategory("Electricity", 800)
food_category.add_expense(100)
new_cat.display_category_summary()
food_category.display_category_summary()