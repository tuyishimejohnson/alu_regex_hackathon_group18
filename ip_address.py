
# Importing Regular Expression


import re

"""Creating an IP pattern variable with RegEx characters sequence"""

ip_pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'


"""Creating a variable IP adress for random numbers 
with the maximum of three digits, followed by period for each three digits, with a backslash."""


ip_address = '984.148.84.0'


a = re.search(ip_pattern, ip_address)

print(a)


