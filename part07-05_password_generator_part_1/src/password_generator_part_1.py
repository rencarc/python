# Write your solution here
import random
import string
def generate_password(length: int) -> str:
    return ''.join(random.choices(string.ascii_lowercase, k=length))

if __name__ == "__main__":

    for i in range(10):
        print(generate_password(8))