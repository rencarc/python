# Write your solution here
def invert(dictionary: dict):
    inverted = {value: key for key, value in dictionary.items()}
    dictionary.clear()
    dictionary.update(inverted) 