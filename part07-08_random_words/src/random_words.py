# Write your solution here
import random
def words(n: int, beginning: str):
    with open("words.txt", "r")as file:
        all_words = file.read().splitlines()
        matching_word = [word for word in all_words if word.startswith(beginning)]
    if len(matching_word) < n:

        raise ValueError(f"Not found enough words starting with'{beginning}'. Reuqired{n}, Found: {len(matching_word)}")
    return random.sample(matching_word, n)

if __name__ == "__main__":
    try:
        word_list = words(3, "ca")
        for word in word_list:
            print(word)
    except ValueError as e:
        print(e)