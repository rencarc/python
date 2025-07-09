# Write your solution here
# Remember the import statement
# from datetime import date

from datetime import date
def list_years(dates: list):
       new_list = sorted(dates)
       year_list = [dates.year for dates in new_list]
       return year_list