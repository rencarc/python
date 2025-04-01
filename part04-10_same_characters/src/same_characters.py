# Write your solution here
def same_chars(string_number, int_num1, int_num2):
    if int_num1 < 0 or int_num1 >= len(string_number) or int_num2 < 0 or int_num2 >= len(string_number):
        return False 
    return string_number[int_num1] == string_number[int_num2]


# You can test your function by calling it within the following block
if __name__ == "__main__":
    # same characters m and m
    print(same_chars("programmer", 6, 7)) # True

# different characters p and r
    print(same_chars("programmer", 0, 4)) # False

# the second index is not within the string
    print(same_chars("programmer", 0, 12)) # False