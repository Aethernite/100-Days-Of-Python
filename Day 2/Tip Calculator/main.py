print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n$"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))

bill_per_person = (bill / people)
bill_per_person_with_tip = round(bill_per_person + bill_per_person * (percentage/100), 2)


print(f"Each person should pay ${bill_per_person_with_tip}")