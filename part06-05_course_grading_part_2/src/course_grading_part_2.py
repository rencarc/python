
student_info = input("Student information: ").strip()
exercise_data = input("Exercises completed: ").strip()
exam_points = input("Exam points: ").strip()


student_names = {}
exercises = {}
grades = {}


with open(student_info) as file:
    for line in file:
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue 
        student_id = parts[0]
        first_name = parts[1]
        last_name = parts[2]
        student_names[student_id] = f"{first_name} {last_name}"

with open(exercise_data) as file:
    for line in file:
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue  
        student_id = parts[0]
        total_exercises = sum(map(int, parts[1:])) 
        exercises[student_id] = total_exercises


with open(exam_points) as file:
    for line in file:
        parts = line.strip().split(';')
        if parts[0] == "id":
            continue 
        student_id = parts[0]
        total_exam_points = sum(map(int, parts[1:])) 
        grades[student_id] = total_exam_points

for student_id, full_name in student_names.items():
    exercise_points = exercises.get(student_id, 0) // 4 
    exam_points = grades.get(student_id, 0)  
    final_points = exercise_points + exam_points 


    if final_points <= 14:
        grade = 0
    elif 15 <= final_points <= 17:
        grade = 1
    elif 18 <= final_points <= 20:
        grade = 2
    elif 21 <= final_points <= 23:
        grade = 3
    elif 24 <= final_points <= 27:
        grade = 4
    else:  
        grade = 5

    print(f"{full_name} {grade}")
