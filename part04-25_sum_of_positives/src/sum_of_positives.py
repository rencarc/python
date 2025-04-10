def sum_of_positives(numbers):
    # Filter out positive numbers and sum them
    return sum(num for num in numbers if num > 0)

# Ensure main program code is inside this block
if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
