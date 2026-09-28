from datetime import datetime, date


def validate_quantity(quantity: str) -> float:
    try:
        return float(quantity)

    except ValueError:
        return f"validation failed: {quantity} is not a valid numerical quantity"
              
Products = []
Total = []
date_time = datetime.now()

def purchase_details():
        product = input("What product are you purchasing: ")
        Products.append(product)
        price = validate_quantity(input("Input price: "))
        quantity = validate_quantity(input("input quantity needed: "))
        total = price * quantity
        Total.append(total)
        add_purchase = input("Do you want to make another purchase (yes/no): ")
        
        

def generate_reciept():
        return f"""
        =======================
            RECIEPT
        =======================
        Date/time: {date_time}
        Product: {Products}
        Total Purchase: {sum(Total)}
        =======================
        """


while True:
    purchase_details()
    generate_reciept()