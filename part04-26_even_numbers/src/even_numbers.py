# Write your solution here
def even_numbers(numbers):
    new_list = [num for num in numbers if num % 2 == 0 ]
    return new_list
m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
print(count_matching_elements(m, 1))  # 输出：3
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)