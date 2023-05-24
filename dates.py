import re

def validate_date(date_string):
    pattern = r"\d{2}-[A-Za-z]{3}-\d{4}"
    if re.match(pattern, date_string):
        return True
    else:
        return False

# by using those examples
date1= "24-May-2023"
date2= "2023-May-24"
date3= "April-24-2023"

print(validate_date(date1)) #output: True
print(validate_date(date2)) #output: False
print(validate_date(date3)) #output: False