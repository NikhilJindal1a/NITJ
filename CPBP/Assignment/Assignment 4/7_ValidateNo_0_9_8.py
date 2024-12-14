# 7. Write a program that validates a mobile phone number. The number should start with 7, 8, or 9 followed by 9 digits.

import re
def validate_mobile_number(number):
    if re.fullmatch(r'[789]\d{9}', number):
        return "Valid mobile number"
    else:
        return "Invalid mobile number"

input_number = "9876543210"
print(validate_mobile_number(input_number))
