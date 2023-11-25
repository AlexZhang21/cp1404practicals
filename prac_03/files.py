# Q1.
out_file = open("name.txt", 'w')
name = input("Enter name: ")
print(name, file=out_file)
out_file.close()

# Q2.
in_file = open("name.txt", 'r')
name = in_file.read().strip()
print(f"Your name is {name}")
in_file.close()
print("Your name is", name)

# Q3.
total = 0
with open("numbers.txt", 'r') as in_file:
    # read first two numbers
    for i in range(2):
        number = int(in_file.readline())
        total += number
print(total)

# Q4.
total = 0
with open("numbers.txt", 'r') as in_file:
    # load whole files run it
    for line in in_file:
        total += int(line)
print(total)