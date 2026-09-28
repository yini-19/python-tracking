# -----------------
#     Exercise 1
# -----------------
price_per_good = 200.0
qty_of_goods = 50
total_price = price_per_good*qty_of_goods
discount = (10/100)*total_price
final_price = total_price-discount
print(f"Total Price: {total_price}")
print(f"Discount: {discount}")
print(f"Final Price: {final_price}")

# -----------------
#     Exercise 2
# -----------------
score = 80
if score >=50 and score <= 100:
    print("course passed!")
else:
    print("failed course!")

# -----------------
#     Exercise 3
# -----------------
user_age = 17
if user_age < 18:
    print("user is underage and can't have an ID")
else:
    print("User is an adult and can have an ID")