
def spruce(size):
    # Print the title "a spruce!"
    print("a spruce!")
    
    # Print the spruce tree
    for i in range(1, size + 1):
        # Calculate the number of stars and spaces
        stars = 2 * i - 1
        spaces = size - i
        
        # Print the line with spaces and stars
        print(" " * spaces + "*" * stars)
    
    # Print the trunk of the spruce
    print(" " * (size - 1) + "*")

# Example calls
if __name__ == "__main__":
    spruce(3)
    print()
    spruce(5)