def new_person(name: str, age: int):

    if not name.strip():
        raise ValueError("Name cannot be an empty string.")

    if len(name.split()) < 2:
        raise ValueError("Name must contain at least two words.")
    
    if len(name) > 40:
        raise ValueError("Name cannot be longer than 40 characters.")

    if age < 0:
        raise ValueError("Age cannot be a negative number.")

    if age > 150:
        raise ValueError("Age cannot be greater than 150.")
    

    return (name, age)
