
age = int(input("Enter your age: "))
weekend = input("Is it weekend? (yes/no): ")

if age < 5:
    price = 0
elif age <= 17:
    price = 100
elif age <= 59:
    price = 200
else:
    price = 120

if price > 0 and weekend == "yes":
    price = price + 50

print("Ticket price: Rs", price)
