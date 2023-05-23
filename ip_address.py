
# Importing Regular Expression from python library


import re

"""Creating an IP pattern variable with RegEx characters sequence"""

ip_pattern = r'^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$'


"""Creating a variable IP adress for inputing random numbers 
with the maximum of twelve digits, followed by period for each one to three digits."""


ip_address = input('Enter an IP address: ')


a = re.search(ip_pattern, ip_address)

print(a)


