#Rent Calculator 
#Some inputs are required from the user
#Total rent 
#Total ordered food
#Total electricity units spend
#charge per unit
#persons living in room/flat


rent = int(input("Enter your Hostel/flat rent ="))
food = int(input("Enter the amount of food ordered="))
electricity_spend = int(input("Enter the total of electricity spend="))
charge_per_unit = int(input("Enter the charge per unit="))
persons =int(input("Enter the number of person in a room/flat"))

total_electricity_bill =electricity_spend*charge_per_unit

output = (food+rent+total_electricity_bill)//persons
print("Each person will pay =", output)
