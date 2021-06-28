# To check a list of Postcodes

import re

value = ['M1 1AA', 'M60 1NW', 'CR2 6XH', 'DN55 1PT', 'W1A 1HQ', 'EC1A 1BB']

for element in value:
    ceps = re.match(r"^(([\w]{2})|([\w]{3})|([\w]{4}))([\s])(([\w]{3})$)", element)
    if ceps:
        print(f"Cep {element} is valid")


