# Write your solution here
def create_tuple(x: int, y: int, z: int):
    point = (x, y, z)
    s = min(point)
    l = max(point)
    total = sum(point)
    return(s, l, total)

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))