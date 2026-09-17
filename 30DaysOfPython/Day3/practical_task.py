budget = 20000.0
total_purchase = 15000.50
difference = budget - total_purchase

if difference < 0:
    print(f"{total_purchase} worth of purchase is above budget")
else:
    print(f"{total_purchase} is within budget. Approved!")