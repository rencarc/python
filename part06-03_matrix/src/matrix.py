def matrix_sum():

    total = 0
    with open("matrix.txt") as new_file:
        for line in new_file:

            line = line.strip()
            elements = line.split(",")

            numbers = [int(element) for element in elements]
            total += sum(numbers)
    return total


def matrix_max():

    max_value = float('-inf') 
    with open("matrix.txt") as new_file:
        for line in new_file:
            line = line.strip()
            elements = line.split(",")
            numbers = [int(element) for element in elements]
            max_value = max(max_value, max(numbers))
    return max_value


def row_sums():

    row_sums_list = []
    with open("matrix.txt") as new_file:
        for line in new_file:

            line = line.strip()
            elements = line.split(",")

            numbers = [int(element) for element in elements]
            row_sums_list.append(sum(numbers))
    return row_sums_list



if __name__ == "__main__":
    print("Matrix Sum:", matrix_sum())  
    print("Matrix Max:", matrix_max())  
    print("Row Sums:", row_sums())      
