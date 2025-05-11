def search_by_name(filename: str, word: str) -> list:
    with open(filename, "r") as file:
        lines = file.readlines()

    recipes = []
    i = 0
    while i < len(lines):
        name = lines[i].strip()
        prep_time = lines[i + 1].strip()  # Read preparation time
        i += 2  # Move to the ingredients

        # Skip the ingredient lines
        while i < len(lines) and lines[i].strip() != "":
            i += 1

        i += 1  # Skip the blank line

        if word.lower() in name.lower():
            recipes.append(name)

    return recipes


def search_by_time(filename: str, prep_time: int) -> list:
    """Search recipes by preparation time."""
    with open(filename, "r") as file:
        lines = file.readlines()

    recipes = []
    i = 0
    while i < len(lines):
        name = lines[i].strip()
        time = int(lines[i + 1].strip())  # Read preparation time
        i += 2  # Move to the ingredients

        # Skip the ingredient lines
        while i < len(lines) and lines[i].strip() != "":
            i += 1

        i += 1  # Skip the blank line

        if time <= prep_time:
            recipes.append(f"{name}, preparation time {time} min")

    return recipes


def search_by_ingredient(filename: str, ingredient: str) -> list:
    """Search recipes by ingredient."""
    with open(filename, "r") as file:
        lines = file.readlines()

    recipes = []
    i = 0
    while i < len(lines):
        name = lines[i].strip()
        time = int(lines[i + 1].strip())  # Read preparation time
        i += 2  # Move to the ingredients

        ingredients = []
        while i < len(lines) and lines[i].strip() != "":
            ingredients.append(lines[i].strip())
            i += 1

        i += 1  # Skip the blank line

        if ingredient.lower() in map(str.lower, ingredients):
            recipes.append(f"{name}, preparation time {time} min")

    return recipes


# Example Usage
if __name__ == "__main__":
    # File containing recipes
    filename = "recipes1.txt"

    # Part 1: Search by name
    word = input("Enter a word to search by name: ")
    recipes_by_name = search_by_name(filename, word)
    print("\nRecipes found by name:")
    for recipe in recipes_by_name:
        print(recipe)

    # Part 2: Search by preparation time
    prep_time = int(input("\nEnter maximum preparation time: "))
    recipes_by_time = search_by_time(filename, prep_time)
    print("\nRecipes found by preparation time:")
    for recipe in recipes_by_time:
        print(recipe)

    # Part 3: Search by ingredient
    ingredient = input("\nEnter an ingredient to search: ")
    recipes_by_ingredient = search_by_ingredient(filename, ingredient)
    print("\nRecipes found by ingredient:")
    for recipe in recipes_by_ingredient:
        print(recipe)
