# Write your solution here
def shortest(strings):
    worst = strings[0]

    for string in strings:
        if len(string) < len(worst):
            worst = string
    return worst
