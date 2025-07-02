
diary_file = "diary.txt"


try:
    with open(diary_file, "r") as file:
        entries = file.read().strip().split("\n")
except FileNotFoundError:
    entries = []

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = input("Function: ")

    if function == "1":
        diary_entry = input("Diary entry: ")
        entries.append(diary_entry)
        with open(diary_file, "a") as file:
            file.write(diary_entry + "\n")
        print("Diary saved")
    elif function == "2":

        print("Entries:")
        for entry in entries:
            print(entry)
    elif function == "0":

        print("Bye now!")
        break
    else:
        print("Invalid option, please choose 1, 2, or 0.")
