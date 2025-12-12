a = int(input("Enter a number: "))

# Determine the last odd number to print
if a % 2 == 0:
    last = a - 1
else:
    last = a

# Generate and print the odd numbers
result = [str(i) for i in range(1, last + 1, 2)]
print(", ".join(result))
