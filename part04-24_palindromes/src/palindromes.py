def palindromes(word):
    # Check if the word is the same when reversed
    return word == word[::-1]

# Main program
while True:
    user_input = input("Please type in a palindrome: ")
    if palindromes(user_input):
        print(f"{user_input} is a palindrome!")
        break
    else:
        print("That wasn't a palindrome")
