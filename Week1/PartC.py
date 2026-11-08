
# Part C - Debugging

a = float(input("Enter first number: "))
# Mistake: input() returns a string.
# Correction: float() converts the input into a number.

b = float(input("Enter second number: "))
# Mistake: The second input was also taken as a string.
# Correction: Convert it into float as well.

average = (a + b) / 2
# Mistake: a + b / 2 divides b first because of operator precedence.
# Correction: (a + b) adds both numbers first, then divides by 2.

print("Average =", average)
# Correction: Prints the correct average.
