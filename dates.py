import re

def verify_day(day_string):
    input = r"\d{2}-[B-Za-z]{3}-\d{4}"
    if re.match(input, day_string):
        return True
    else:
        return False

# by using those examples
day1= "24-May-2023"
day2= "2023-May-24"
day3= "May-24-2023"

print(verify_day(day1)) #output: True
print(verify_day(day2)) #output: False
print(verify_day(day3)) #output: False