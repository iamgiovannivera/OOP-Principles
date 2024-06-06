# class BudgetCategory:
#     def __init__(self, category_name, allocated_budget):
#         self.__category_name = category_name
#         self.__allocated_budget = allocated_budget
#         self.__remaining_budget = allocated_budget

#     # Getter for category name
#     @property
#     def category_name(self):
#         return self.__category_name

#     # Setter for category name
#     @category_name.setter
#     def category_name(self, name):
#         if isinstance(name, str) and name:
#             self.__category_name = name
#         else:
#             raise ValueError("Category name must be a non-empty string.")

#     # Getter for allocated budget
#     @property
#     def allocated_budget(self):
#         return self.__allocated_budget

#     # Setter for allocated budget
#     @allocated_budget.setter
#     def allocated_budget(self, budget):
#         if budget > 0:
#             self.__remaining_budget += (budget - self.__allocated_budget)
#             self.__allocated_budget = budget
#         else:
#             raise ValueError("Budget must be a positive number.")
            
            


# Task 3: Add Budget Functionality



#     def add_expense(self, amount):
#         if amount > 0 and amount <= self.__remaining_budget:
#             self.__remaining_budget -= amount
#         else:
#             raise ValueError("Expense amount must be positive and within the remaining budget.")

#     def display_category_summary(self):
#         print(f"Category: {self.__category_name}")
#         print(f"Allocated Budget: ${self.__allocated_budget}")
#         print(f"Remaining Budget: ${self.__remaining_budget}")



# Task 1: Create Base Product Class



# class Product:
#     def __init__(self, product_id, name, price):
#         self.product_id = product_id
#         self.name = name
#         self.price = price

#     def display_info(self):
#         print(f"Product ID: {self.product_id}")
#         print(f"Name: {self.name}")
#         print(f"Price: ${self.price}")
        
        
        
# Task 2: Implement Subclasses for Specific Products



# class Book(Product):
#     def __init__(self, product_id, name, price, author):
#         super().__init__(product_id, name, price)
#         self.author = author

#     def display_info(self):
#         super().display_info()
#         print(f"Author: {self.author}")

# class Electronic(Product):
#     def __init__(self, product_id, name, price, specs):
#         super().__init__(product_id, name, price)
#         self.specs = specs

#     def display_info(self):
#         super().display_info()
#         print(f"Specifications: {self.specs}")

# class Clothing(Product):
#     def __init__(self, product_id, name, price, size):
#         super().__init__(product_id, name, price)
#         self.size = size

#     def display_info(self):
#         super().display_info()
#         print(f"Size: {self.size}")
        
        
# Task 3: Override Display Method in Subclasses


#     # The display_info methods 
    
# Task 4: Test Product Catalog Functionality



# # Example usage
# my_book = Book("123", "Python Essentials", 29.99, "J. Doe")
# my_book.display_info()

# my_electronic = Electronic("456", "Smartphone", 999.99, "64GB, 4GB RAM")
# my_electronic.display_info()

# my_clothing = Clothing("789", "T-Shirt", 19.99, "L")
# my_clothing.display_info()