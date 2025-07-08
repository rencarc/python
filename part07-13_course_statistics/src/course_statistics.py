import urllib.request
import json
import math

def retrieve_all():
    """
    Retrieves all active courses and returns them as a list of tuples.
    Each tuple contains:
    - fullName: the full name of the course
    - name: the short name of the course
    - year: the year the course is active
    - sum of exercises
    """
    url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"
    with urllib.request.urlopen(url) as response:
        courses = json.loads(response.read())
    
    # Filter active courses and extract required fields
    active_courses = [
        (
            course["fullName"],
            course["name"],
            course["year"],
            sum(course["exercises"])
        )
        for course in courses if course["enabled"]
    ]
    return active_courses


def retrieve_course(course_name: str):
    """
    Retrieves statistics for a specific course and returns them as a dictionary.
    The dictionary contains:
    - weeks: number of weeks in the course
    - students: maximum number of students
    - hours: total hours spent
    - hours_average: average hours spent per student
    - exercises: total exercises completed
    - exercises_average: average exercises completed per student
    """
    url = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read())
    
    # Extract required values
    weeks = len(data)
    students = max(week["students"] for week in data.values())
    hours = sum(week["hour_total"] for week in data.values())
    exercises = sum(week["exercise_total"] for week in data.values())
    hours_average = math.floor(hours / students) if students else 0
    exercises_average = math.floor(exercises / students) if students else 0
    
    return {
        "weeks": weeks,
        "students": students,
        "hours": hours,
        "hours_average": hours_average,
        "exercises": exercises,
        "exercises_average": exercises_average
    }

