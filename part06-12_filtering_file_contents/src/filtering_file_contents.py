def filter_solutions():

    with open("solutions.csv", "r") as input_file:

        with open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
            for line in input_file:

                line = line.strip()

                parts = line.split(";")
                
                if len(parts) != 3:

                    continue
                
                name_of_student, problem, result = parts

                if "+" in problem:
                    operands = problem.split("+")
                    operator = "+"
                elif "-" in problem:
                    operands = problem.split("-")
                    operator = "-"
                else:

                    continue
                
                try:

                    operand1 = int(operands[0])
                    operand2 = int(operands[1])
                    
                    if operator == "+":
                        correct_result = operand1 + operand2
                    elif operator == "-":
                        correct_result = operand1 - operand2

                    if correct_result == int(result):
                        correct_file.write(line + "\n")
                    else:
                        incorrect_file.write(line + "\n")
                except ValueError:

                    incorrect_file.write(line + "\n")
