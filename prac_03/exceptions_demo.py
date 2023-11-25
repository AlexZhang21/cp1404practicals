"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when user inputs a value that can't be numerator, which means not an integer, ValueError will occur.

2. When will a ZeroDivisionError occur?

The result will be ZeroDivisionError,When the user enters 0 as the denominator

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Sure, try my best
"""

# Fixed version
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero, please use another number.")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")