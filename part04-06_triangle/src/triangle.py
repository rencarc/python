
def line(length, char):
    # 如果第二个参数是空字符串，使用 '*' 作为默认字符
    if char == "":
        char = "*"
    # 打印指定长度的字符
    print(char[0] * length)

def triangle(size):
    for i in range(1, size + 1):  # 从1开始，循环直到size
        line(i, "#")  # 每行打印i个字符




# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(6)
    print()
    triangle(3)
