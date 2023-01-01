print("Welcome to the tip calculator")
hotel_bill = input("What was the total bill? $")
percentage_tip = input("What percentage tip you like to give ? 10, 12, or 15?")
bill_division = input("How many people to split the bill ?")
a = ((int(hotel_bill) * int(percentage_tip) * 0.01) + int(hotel_bill))
b = str(a /int(bill_division))
final_bill = f"Each person should pay:${b}"
print(final_bill)
