# Write your solution here
from datetime import datetime
day_of_birth = int(input("Day:"))
month_of_birth = int(input("Month:"))
year_of_birth = int(input("Year: "))
new_millennium = datetime(1999, 12, 31)
birthdays = datetime(year_of_birth, month_of_birth, day_of_birth)
if birthdays < new_millennium:

    delta = new_millennium - birthdays
    print(f"You were {delta.days} days old on the eve of the new millennium.")    

else:
    print(f"You weren't born yet on the eve of the new millennium.")  