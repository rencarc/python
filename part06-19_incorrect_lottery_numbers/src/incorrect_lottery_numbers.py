def filter_incorrect():
    input_file = "lottery_numbers.csv"
    output_file = "correct_numbers.csv"

    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        for line in infile:
            line = line.strip()
            if not line.startswith("week "):  
                continue
            
            parts = line.split(";")
            if len(parts) != 2:  
                continue
            
            week, numbers = parts
            if not week[5:].isdigit(): 
                continue
            
            number_list = numbers.split(",")
            if len(number_list) != 7: 
                continue
            
            try:
                number_list = [int(num) for num in number_list]  
            except ValueError: 
                continue
            
            if any(num < 1 or num > 39 for num in number_list): 
                continue
            
            if len(set(number_list)) != len(number_list): 
                continue

            outfile.write(line + "\n")
