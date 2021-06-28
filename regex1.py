

import re

# To check one Postcode

value = input("Please type your CEP:")
z = re.match(r"^(([\w]{2})|([\w]{3})|([\w]{4}))([\s])(([\w]{3})$)", value)

print(z)

if z:
    print("Valid Postcode")
else:
    print("Invalid Postcode!")



