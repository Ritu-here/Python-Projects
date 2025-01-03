#Hotel Management System
#Define the menu of restaurant

menu={
    "pizza":40,
    "Pasta":50,
    "Burger":60,
    "Salad":70,
    "Coffee":80
}

print("Welcome to our RR Foods")
print("Pizza:40\npasta:50\nBurger:60\nSalad:70\nCoffee:80")

order_total =0

item1 = input("Enter the name of item you want to order = ")
if item1 in menu:
    order_total += menu[item1]
    print(f"Your item {item1} has been added to your order")
else:
    print(f"Ordered item {item1} is not available yet!")

another_order = input("Do you want to add another item?(yes/no)")
if another_order == "yes":
    item2 = input("Enter the name of second item=")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Your item {item2} has been added to your order")
    else:
        print(f"Ordered item {item2} is not available!")

print(f"The total amount of items to pay is {order_total} ")

