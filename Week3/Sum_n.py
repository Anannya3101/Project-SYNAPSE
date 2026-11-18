
n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total = total + i

print("Sum using loop:", total)

formula = n * (n + 1) // 2
print("Sum using formula:", formula)
