# Question 5 Make stock reservation reliable
# Hardest  |  16 minutes  |  30 marks
# stock maps item names to available quantities. 
# order is a list of (item, quantity) pairs. 
# Stock values are non-negative integers; order quantities are integers, not booleans. 
# Keys are strings. These shapes and types are guaranteed.
def reserve_stock(stock, order):
    remaining = stock.copy()
    for item, quantity in order:
        if item not in remaining:
            raise ValueError("unknown item")
        if quantity <= 0:
            raise ValueError("quantity cannot be negative")
        if quantity > stock[item]:
            raise ValueError("Insufficient stock")
        remaining[item] -= quantity
    return remaining
# Required behaviour
# Return a new dictionary containing every stock key with its remaining quantity. 
# Never modify stock or order, including when a request fails.
# An item may occur more than once in order. Its combined requested quantity must be reserved. 
# Never allow a negative remaining quantity.
# Raise ValueError for an unknown item, a quantity of zero or less, or insufficient stock. 
# Error message wording is your choice. An empty order returns an equal but separate dictionary.
# You may use try/except with an assertion that fails if ValueError is not raised. 
# Tests must call the function and check a result or failure, not just print it.
# Q5 Part B
# Repair the function to meet all requirements. Use only in-memory Python; 
# no database or concurrency implementation is needed. [14 marks]
# Q5 Part A
# With stock = {"pen": 5}, trace order = [("pen", 3), ("pen", 3)]. 
# Explain why the supplied code incorrectly succeeds, and identify the other validation gaps. [6 marks]
# Q5 Part C
# Write four tests: successful repeated items, repeated items exceeding stock, 
# an unknown item, and zero quantity. In the overselling test, make at least one earlier line valid, 
# then assert the original stock is unchanged after the exception. 
# Explain why editing a local copy protects the caller when a later line fails. [10 marks]