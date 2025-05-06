
def add_student(students: dict, name: str):
    if name not in students:
        students[name] = []


def print_student(students: dict, name: str):
    if name in students:
        print(f"{name}:")
        if students[name]:
            for course in students[name]:
                print(f" {course[0]} ({course[1]} credits)")
        else:
            print(" no completed courses")
    else:
        print(f"{name}: no such person in the database")


def add_course(students: dict, name: str, completion: tuple):
    if name not in students:
        print(f"{name}: no such person in the database")
        return

    course_name, grade = completion
    if grade == 0:
        return

    for i, course in enumerate(students[name]):
        if course[0] == course_name:
            students[name][i] = completion
            return

    students[name].append(completion)

def print_student(students: dict, name: str):

    if name not in students:
        print(f"{name}: no such person in the database")
        return

    print(f"{name}:")
    if not students[name]:
        print(" no completed courses")
        return

    total_grade = 0
    total_courses = len(students[name])

    for course in students[name]:
        print(f" {course[0]} {course[1]}")
        total_grade += course[1]

    average_grade = total_grade / total_courses
    print(f" average grade {average_grade:.1f}")


def summary(students: dict):

    total_students = len(students)
    most_courses = 0
    best_average = 0
    most_courses_student = ""
    best_average_student = ""

    for name, courses in students.items():

        completed_courses = len(courses)
        if completed_courses > most_courses:
            most_courses = completed_courses
            most_courses_student = name


        if completed_courses > 0:
            total_grade = sum(course[1] for course in courses)
            average_grade = total_grade / completed_courses
            if average_grade > best_average:
                best_average = average_grade
                best_average_student = name

    print(f"students {total_students}")
    print(f"most courses completed {most_courses} {most_courses_student}")
    print(f"best average grade {best_average:.1f} {best_average_student}")
