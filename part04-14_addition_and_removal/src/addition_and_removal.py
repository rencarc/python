my_list = []
next_item = 1

while True:
    print(f"The list is now {my_list}")
    choice = input("a(d)d, (r)emove or e(x)it: ")
    if choice == "d": 
        my_list.append(next_item)
        next_item += 1
    elif choice == "r":
        if my_list != []:
            my_list.pop()
    elif choice == "x":
        print("Bye!")
        break
    # Write your solution here