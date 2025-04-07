list_now = []

while True:
    # Prompt the user to input a new item and convert it to an integer
    try:
        new_item = int(input("New item: "))
    except ValueError:
        print("Please enter an integer!")
        continue

    if new_item == 0:  # Exit if the user enters 0
        print("Bye!")
        break

    list_now.append(new_item)  # Add the new item to the list
    print(f"The list now: {list_now}")  # Print the list in the original order

    in_order = sorted(list_now)  # Create a new list sorted in ascending order
    print(f"The list in order: {in_order}")  # Print the sorted list
