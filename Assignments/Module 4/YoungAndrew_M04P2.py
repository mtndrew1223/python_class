print("Andrew Young's Tip Calculator")

meal_cost = float(input(" Cost of Meal " ))
print()

percentages = [15, 20, 25]

for percent in percentages:
    print(str(percent) + "%")

    tip_percent = percent / 100
    tip_amount = round(meal_cost * tip_percent,2)
    total_cost = round(meal_cost + tip_amount,2)

    print("Tip amount: $" + str(tip_amount))

    print("Total Meal Cost: $" + str(total_cost))

    print()