
def line(length, char):
    # 使用 char[0] 作为字符，如果 char 是空字符串，使用 '*' 作为默认字符
    print((char or '*')[0] * length)

# 测试函数
if __name__ == "__main__":
    line(7, "%")   # 输出: %%%%%%%
    line(10, "LOL")  # 输出: LLLLLLLLLL
    line(3, "")     # 输出: ***