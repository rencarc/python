# Write your solution here
def find_words(search_term: str):


    with open("words.txt") as file:
        words = file.read().splitlines()


    if "*" in search_term:
        if search_term.startswith("*"):

            suffix = search_term[1:]
            return [word for word in words if word.endswith(suffix)]
        elif search_term.endswith("*"):

            prefix = search_term[:-1]
            return [word for word in words if word.startswith(prefix)]
    elif "." in search_term:

        import re
        pattern = "^" + search_term.replace(".", ".") + "$"
        return [word for word in words if re.match(pattern, word)]
    else:
        return [word for word in words if word == search_term]
