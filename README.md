# Regex challenge 

The UK postcode system consists of a string that contains a number of characters and numbers – a typical example is ST7 9HV (this is not valid – see below for why). The rules for the pattern are available from idealpostcodes (2020).
Create a python program that implements a regex that complies with the rules provided above – test it against the examples provided.
Examples:
* M1 1AA
* M60 1NW
* CR2 6XH
* DN55 1PT
* W1A 1HQ
* EC1A 1BB

How do you ensure your solution is not subject to an evil regex attack?

Resources:

https://regex101.com/
hhttps://jex.im/regulex/#!flags=&re=%5B0-9%5D%7B5%7D-%5B%5Cd%5D%7B3%7D
https://blog.geekhunter.com.br/python-regex/
