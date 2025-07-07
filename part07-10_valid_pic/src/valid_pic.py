from datetime import datetime

def is_it_valid(pic: str) -> bool:

    if len(pic) != 11:
        return False

    date_part = pic[:6]
    century_marker = pic[6]
    individual_number = pic[7:10]
    control_character = pic[10]

    try:
        day = int(date_part[:2])
        month = int(date_part[2:4])
        year = int(date_part[4:])
        
        if century_marker == "+":
            year += 1800
        elif century_marker == "-":
            year += 1900
        elif century_marker == "A":
            year += 2000
        else:
            return False  

        birth_date = datetime(year, month, day)
    except ValueError:
        return False

    if not individual_number.isdigit():
        return False

    control_base = f"{date_part}{individual_number}"
    control_number = int(control_base) % 31
    valid_characters = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    if valid_characters[control_number] != control_character:
        return False


    return True

if __name__ == "__main__":
    test_pics = [
        "230827-906F",  # valid
        "120488+246L",  # valid
        "310823A877",   # valid
        "311299A123",   # invalid control character
        "310299-999X",  # invalid date
    ]

    for pic in test_pics:
        print(f"{pic}: {'Valid' if is_it_valid(pic) else 'Invalid'}")
