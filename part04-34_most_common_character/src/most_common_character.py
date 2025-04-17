def most_common_character(string):
    max_count = 0
    most_common = None

    for char in string:
        count = string.count(char)

        if count > max_count:
            max_count = count
            most_common = char
        elif count == max_count and string.index(char) < string.index(most_common):
            most_common = char
        
    return most_common




