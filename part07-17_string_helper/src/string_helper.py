
def change_case(orig_string: str):
    return "".join(
        char.upper() if char.islower() else char.lower()
        for char in orig_string
    )

def split_in_half(orig_string: str):
    midpoint = len(orig_string) // 2

    return orig_string[:midpoint], orig_string[midpoint:]

def remove_special_characters(orig_string: str):
    return "".join(
        char for char in orig_string
        if char.isalnum() or char.isspace()
    )


if __name__ == "__main__":
    import string_helper

    my_string = "Well hello there!"

    print(string_helper.change_case(my_string))

    p1, p2 = string_helper.split_in_half(my_string)

    print(p1)
    print(p2)

    m2 = string_helper.remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)