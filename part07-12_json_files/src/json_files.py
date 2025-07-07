import json

def print_persons(filename: str):
    try:

        with open(filename) as my_file:
            data = my_file.read()

        contents = json.loads(data)

        for person in contents:
            name = person["name"]
            age = person["age"]
            hobbies = ", ".join(person["hobbies"])
            print(f"{name} {age} years ({hobbies})")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
