"""
Create a program to validate email addresses and mobile phone numbers using regex.
"""

import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

def validate_mobile(mobile):
    pattern = r'^[6-9]\d{9}$'
    if re.match(pattern, mobile):
        return True
    return False

email = input("Enter an email address to validate: ")
mobile = input("Enter a mobile number to validate: ")

if validate_email(email):
    print(f"{email} is a valid email address.")
else:
    print(f"{email} is not a valid email address.")

if validate_mobile(mobile):
    print(f"{mobile} is a valid mobile number.")
else:
    print(f"{mobile} is not a valid mobile number.")