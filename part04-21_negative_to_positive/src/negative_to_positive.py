# Write your solution here

positive_integer = int(input("Please type in a positive integer:"))

for i in range(-positive_integer, positive_integer + 1):
    if i != 0:
        print(i)
