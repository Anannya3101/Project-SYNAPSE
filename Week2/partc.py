age = int(input("Enter age: "))  # Bug 1: input() returns a string, so int() is used to convert it into an integer.

if age >= 18:
    print("Adult")

elif age >= 13:  # Bug 2: Colon (:) was missing at the end of the elif statement.
    print("Teen")

else:
    print("Child")