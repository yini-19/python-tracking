import string

def calculate_total(nums: int) -> int:
    total_nums = sum(nums)

    print(f"Total is: {total_nums}")

numbers = [1, 2, 3, 4, 5]
calculate_total(numbers)

def validate_quantity(quantity: str) -> float:
    try:
        return float(quantity)

    except ValueError:
        return f"validation failed: {quantity} is not a valid numerical quantity"
              
print(validate_quantity("10"))

new_product = {
    "id": "good123",
    "name": "AI noodles",
    "unit_price": 5000,
    "quantity_in_stock": 100,
    "quantity_ordered": 0,
    "total_purchase": 0
}
def calculate_stock(product: dict) -> dict:
    try:
        order = input("Quantity of goods purchased: ")
        product["quantity_ordered"] = int(order)
        product["quantity_in_stock"] = product["quantity_in_stock"] - product["quantity_ordered"]
        product["total_purchase"] = product["quantity_ordered"] * product["unit_price"]
        return product
    except ValueError:
        return f"❌input validation failed: {order} is not a numerical value"

print(calculate_stock(new_product))