import csv
from datetime import datetime, timedelta

def cheaters():

    start_times = {}
    with open("start_times.csv") as start_file:
        reader = csv.reader(start_file, delimiter=";")
        for row in reader:
            name, start_time = row
            start_times[name] = datetime.strptime(start_time, "%H:%M")


    cheaters_set = set()
    with open("submissions.csv") as submissions_file:
        reader = csv.reader(submissions_file, delimiter=";")
        for row in reader:
            name, task, points, submit_time = row
            submit_time = datetime.strptime(submit_time, "%H:%M")
            if name in start_times:

                if submit_time - start_times[name] > timedelta(hours=3):
                    cheaters_set.add(name)

    return sorted(cheaters_set)
