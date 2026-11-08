n = int(input("Enter a 4-digit number: "))

d1 = n // 1000
d2 = (n // 100) % 10
d3 = (n // 10) % 10
d4 = n % 10

print(d1)
print(d2)
print(d3)
print(d4)

print("Sum:", d1 + d2 + d3 + d4)