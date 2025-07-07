from datetime import datetime, timedelta

filename = input("Filename: ")
start_date_str = input("Starting date (dd.mm.yyyy): ")
days = int(input("How many days: "))

start_date = datetime.strptime(start_date_str, "%d.%m.%Y")


screen_times = []  
total_minutes = 0

print("Please type in screen time in minutes on each day (TV computer mobile):")


for i in range(days):

    current_date = start_date + timedelta(days=i)
    current_date_str = current_date.strftime("%d.%m.%Y")
    

    screen_time = input(f"Screen time {current_date_str}: ")
    tv, computer, mobile = map(int, screen_time.split())
    screen_times.append((current_date_str, tv, computer, mobile))

    total_minutes += (tv + computer + mobile)


average_minutes = total_minutes / days

lines = []
lines.append(f"Time period: {start_date.strftime('%d.%m.%Y')}-{(start_date + timedelta(days=days - 1)).strftime('%d.%m.%Y')}")
lines.append(f"Total minutes: {total_minutes}")
lines.append(f"Average minutes: {average_minutes:.1f}")
for date_str, tv, computer, mobile in screen_times:
    lines.append(f"{date_str}: {tv}/{computer}/{mobile}")

with open(filename, "w") as file:
    file.write("\n".join(lines))

print(f"Data stored in file {filename}")
