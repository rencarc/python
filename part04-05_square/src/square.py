# Copy here code of line function from previous exercise
# Copy here code of line function from previous exercise
def line(length, char):
    if char == "":
        char = "*"
    print(char[0] * length)

def square(size, character):
    for i in range(size):
        line(size, character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "*")
    print()
    square(3, "o")