seconds = int(input("Enter seconds: "))

hours = seconds // 3600
remaining = seconds % 3600

minutes = remaining // 60
seconds = remaining % 60

print(hours, "h", minutes, "min", seconds, "s")