# Write your solution here
def histogram(strings):
    groups = {}
    for letter in strings:

        if letter not in groups:
            groups[letter] = 0

        groups[letter] += 1

    for letter in sorted(groups.keys()):
        print(f"{letter} {'*' * groups[letter]}") 

if __name__ == "__main__":
    histogram("abba")

