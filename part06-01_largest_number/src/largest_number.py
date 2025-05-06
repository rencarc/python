# write your solution here
def largest():
    with open("numbers.txt") as new_file:
        numbers = [int(line.strip()) for line in new_file]
        return max(numbers)


