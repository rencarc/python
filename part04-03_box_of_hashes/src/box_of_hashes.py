def line(length, char):
    if char == "":
        char = "*"

    print(char[0] * length)

def box_of_hashes(height):
    for i in range(height):
        line(10, "#")

if __name__  == "_main_":
    box_of_hashes(5)
    print()
    box_of_hashes(2)
