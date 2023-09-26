print("Welcome to Tip Calculator!")
bill = float(input("What was the total bill? "))
tip = int(input("What the percentage would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = bill + tip / 100 * bill
total_by_person = bill_with_tip / people

print(f"Each person should pay: ${round(total_by_person, 2)}")
