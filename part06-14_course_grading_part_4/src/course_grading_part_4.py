
student_info_file = input("Student information: ").strip()
exercises_file = input("Exercises completed: ").strip()
exam_points_file = input("Exam points: ").strip()
course_info_file = input("Course information: ").strip()


with open(course_info_file) as file:
    course_name = file.readline().strip().split(": ")[1]
    course_credits = file.readline().strip().split(": ")[1]


students = {}
with open(student_info_file) as file:
    for line in file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = f"{parts[1]} {parts[2]}"


exercises = {}
with open(exercises_file) as file:
    for line in file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exercises[parts[0]] = sum(map(int, parts[1:]))

# Parse exam points
exam_points = {}
with open(exam_points_file) as file:
    for line in file:
        parts = line.strip().split(";")
        if parts[0] == "id":
            continue
        exam_points[parts[0]] = sum(map(int, parts[1:]))


grades = {}
results = []
for student_id, name in students.items():
    exec_nbr = exercises.get(student_id, 0)
    exec_points = exec_nbr // 4  # Convert exercises to points
    exam_pts = exam_points.get(student_id, 0)
    total_points = exec_points + exam_pts

    if total_points < 15:
        grade = 0
    elif total_points < 18:
        grade = 1
    elif total_points < 21:
        grade = 2
    elif total_points < 24:
        grade = 3
    elif total_points < 28:
        grade = 4
    else:
        grade = 5

    grades[student_id] = grade
    results.append((name, exec_nbr, exec_points, exam_pts, total_points, grade))

with open("results.txt", "w") as file:
    file.write(f"{course_name}, {course_credits} credits\n")
    file.write("=" * 30 + "\n")
    file.write("name                           exec_nbr  exec_pts. exm_pts.  tot_pts. grade\n")
    for name, exec_nbr, exec_points, exam_pts, total_points, grade in results:
        file.write(f"{name:<30}{exec_nbr:<10}{exec_points:<10}{exam_pts:<10}{total_points:<10}{grade}\n")


with open("results.csv", "w") as file:
    for student_id, grade in grades.items():
        file.write(f"{student_id};{students[student_id]};{grade}\n")

print("Results written to files results.txt and results.csv")
