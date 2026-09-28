sales_amounts = [150, 200, 260, 120, 175]
total = sum(sales_amounts[0:])
largest_amt = 0
count = 0
for amount in sales_amounts:
    if amount > largest_amt:
        largest_amt = amount
for item in sales_amounts[2:]:
    count += 1
print(total)
print(largest_amt)
print(count)

    