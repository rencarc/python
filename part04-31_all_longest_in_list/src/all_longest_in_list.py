def all_the_longest(strings):
    best = max(len(string) for string in strings)
    result = []
    for string in strings:

        if len(string) == best:
            result.append(string)
    return result
        