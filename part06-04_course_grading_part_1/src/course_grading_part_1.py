student_info = input("Student information: ").strip()
exercise_data = input("Exercises completed: ").strip()

student_names = {}
exercises = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue  
        id = parts[0]
        first_name = parts[1]
        last_name = parts[2]
        student_names[id] = f"{first_name} {last_name}"

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue  
        id = parts[0]
        total_exercises = sum(map(int, parts[1:]))
        exercises[id] = total_exercises

for id, full_name in student_names.items():
    total_exercises = exercises.get(id, 0)  
    print(f"{full_name} {total_exercises}")
