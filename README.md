# Regex challenge 

This repository contains an assignement of Module 3 (“Secure Software Development”) Unit 4 (Exploring Programming Language Concepts)  of my MSc in Computer Science at the University of Essex, UK. 

## :paperclip: Regex Challenge - Part 1

The UK postcode system consists of a string that contains a number of characters and numbers – a typical example is ST7 9HV (this is not valid – see below for why). The rules for the pattern are available from idealpostcodes (2020).
Create a python program that implements a regex that complies with the rules provided above – test it against the examples provided.
Examples:
* M1 1AA
* M60 1NW
* CR2 6XH
* DN55 1PT
* W1A 1HQ
* EC1A 1BB

 ## :paperclip: Solution  
 
 For this exercise I used an article from [Geekhunter](https://blog.geekhunter.com.br/python-regex/) which explains Regex Parsers syntax. To test my Regex code I used [Regular Expressions 101](https://regex101.com/), which provides a detailed explanation of the Regex code. In the file named [explanation](https://github.com/alicevillar/regex/blob/main/explanation) you can see the detailed response I had from that website. I created two different codes:
 
* [Regex 1](https://github.com/alicevillar/regex/blob/main/regex1.py) -> Python code to check one Postcode (this is done with an If-Else statement) 
* [Regex 2](https://github.com/alicevillar/regex/blob/main/regex2.py) -> Python code check a list of Postcodes (this is done with a FOR structure) 

## Regex Challenge - Part 2

### How do you ensure your solution is not subject to an evil regex attack?

A Regex is called “evil” if it can stuck on crafted input.

Evil Regex pattern contains:

Grouping with repetition
Inside the repeated group:
Repetition
Alternation with overlapping
Examples of Evil Patterns:

(a+)+
([a-zA-Z]+)*
(a|aa)+
(a|a?)+
(.*a){x} for x \> 10
All the above are susceptible to the input aaaaaaaaaaaaaaaaaaaaaaaa! (The minimum input length might change slightly, when using faster or slower machines).

Attacks
The attacker might use the above knowledge to look for applications that use Regular Expressions, containing an Evil Regex, and send a well-crafted input, that will hang the system. Alternatively, if a Regex itself is affected by a user input, the attacker can inject an Evil Regex, and make the system vulnerable.

Resources:

* [OWASP](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS)
* [Regular Expressions 101](https://regex101.com/)
* [Geekhunter](https://blog.geekhunter.com.br/python-regex/)
