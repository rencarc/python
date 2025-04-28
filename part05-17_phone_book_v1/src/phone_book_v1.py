def phone_book_app():
    phone_book = {}  

    while True:

        command = int(input("command (1 search, 2 add, 3 quit): "))

        if command == 2:  
            name = input("name: ")
            number = input("number: ")
            if name not in phone_book:
                phone_book[name] = []  
            phone_book[name].append(number)  
            print("ok!")

        elif command == 1: 
            name = input("name: ")
            if name in phone_book:
                for num in phone_book[name]: 
                    print(num)
            else:
                print("no number")

        elif command == 3:  
            print("quitting...")
            break


