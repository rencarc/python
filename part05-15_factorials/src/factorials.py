# Write your solution here
# Write your solution here
import math
def factorials(n: int):
    return {key: math.factorial(key) for key in range(1, n + 1)}
if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])