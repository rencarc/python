
def line(length, char):

    if char == "":
        char = "*"
    print(char[0] * length)

def triangle(width, char):

    for i in range(1, width + 1):
        line(i, char)

def shape(triangle_width, triangle_char, rectangle_height, rectangle_char):

    triangle(triangle_width, triangle_char)

    for _ in range(rectangle_height):
        line(triangle_width, rectangle_char)

if __name__ == "__main__":

    shape(5, "x", 3, "*")
    print()
    shape(2, "o", 4, "+")
    print()
    shape(3, ".", 0, ",")
