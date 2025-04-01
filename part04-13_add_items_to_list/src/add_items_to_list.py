# 写下你的解决方案
num_items = int(input("How many items: "))  # 使用更清晰的变量名
items = []  # 初始化一个空列表

for i in range(num_items):  # 循环 num_items 次
    value = int(input(f"Item {i + 1}: "))  # 提示用户输入每个数字
    items.append(value)  # 将用户输入的值添加到列表中

print(items)  # 打印最终的列表
