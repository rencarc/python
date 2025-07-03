dictionary_file = "dictionary.txt"

try:

    with open(dictionary_file, "r") as file:
        words = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    words = [] 

while True:
    print("Add word, 2 - Search, 3 - Quit")
    function = input("Function: ").strip()

    if function == "1":
        finnish_word = input("The word in Finnish: ").strip().lower()
        english_word = input("The word in English: ").strip().lower()
        new_entry = f"{finnish_word};{english_word}"

        if new_entry in words:
            print("This word pair already exists in the dictionary.")
        else:
            words.append(new_entry)
            with open(dictionary_file, "a") as file:
                file.write(new_entry + "\n")
            print("Dictionary entry added.")

    elif function == "2":
        search_term = input("Search term: ").strip().lower()
        results = []

        for word in words:
            finnish, english = word.split(";")
            if search_term == finnish or search_term == english:
                results.append(f"{finnish} - {english}")

        if results:
            for result in results:
                print(result)
        else:
            print("No entries found.")
            breakpoint()

    elif function == "3":
        print("Bye!")
        break
    else:
        print("Invalid option, please choose 1, 2, or 3.")
