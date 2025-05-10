def read_fruits():
    fruits_dict = {}
    with open("fruits.csv") as new_file:
         for line in new_file:
              line = line.strip()
              name, price = line.split(";")
              fruits_dict[name] = float(price)
    return fruits_dict


