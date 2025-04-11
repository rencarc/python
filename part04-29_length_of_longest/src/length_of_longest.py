# Write your solution here
def length_of_longest(strings):
    best = 0

    for string in strings:
        if len(string) > best:
            best = len(string)
    return best
        

