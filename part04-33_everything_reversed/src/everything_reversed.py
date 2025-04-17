# Write your solution here
def everything_reversed(strs: list):
    reversed_list = strs[::-1]
    return [i[::-1] for i in reversed_list]
