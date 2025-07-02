# Write your solution here
def store_personal_data(person: tuple):
    with open("people.csv", "a") as my_file:
        new_entry = f"{person[0]};{person[1]};{person[2]}\n"
        my_file.write(new_entry)