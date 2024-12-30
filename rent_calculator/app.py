# Input we need from the user
# Total rent
# Total food orderfor snacking
# Electricity units spend
# Charge per unit
# Person living in room/flat
# Ouput
# Total amount you have to pay is

rent = int(input("Enter your hostel/ flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spend = int(input("Enter the total electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
person = int(input("Enter the number of persons living in room/flat = "))

total_bill = electricity_spend * charge_per_unit
output = (food + rent + total_bill)

print("Each person will pay = ", output)