import random
import string

def generate_strong_password(length: int, include_numbers: bool, include_special_characters: bool) -> str:
    if length < 1:
        raise ValueError("Password length must be at least 1")


    lowercase_pool = string.ascii_lowercase
    numbers_pool = string.digits
    special_characters_pool = "!?+-()#"


    password = [random.choice(lowercase_pool)]

    if include_numbers:
        password.append(random.choice(numbers_pool))


    if include_special_characters:
        password.append(random.choice(special_characters_pool))


    remaining_length = length - len(password)
    if remaining_length > 0:
        valid_pool = lowercase_pool
        if include_numbers:
            valid_pool += numbers_pool
        if include_special_characters:
            valid_pool += special_characters_pool
        

        password.extend(random.choices(valid_pool, k=remaining_length))

    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":

    for i in range(10):
        print(generate_strong_password(8, True, True))
