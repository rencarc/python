# Copy here code of line function from previous exercise
def line(length, char):
    if char == "":
        char = "*"
    print(char[0] * length)


def square_of_hashes(size):
    for i in range(size):
        line(size, "#")
    # You should call function line here with proper parameters


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
    print()
    square_of_hashes(3)