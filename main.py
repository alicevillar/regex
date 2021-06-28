# O sistema de código postal em alguns países consiste em uma string que contém vários caracteres e números - um exemplo típico é ST7 9HV (isso não é válido - veja abaixo o motivo). As regras para o padrão estão disponíveis em idealpostcodes (2020).
# Programa em python que implemente um regex para isso - testar com os exemplos fornecidos.
# Para teste:
# M1 1AA
# M60 1NW
# CR2 6XH
# DN55 1PT
# W1A 1HQ
# EC1A 1BB
# Como proteger contra ataque de regex?


import re

# To check one CEP

value = input("Please type your CEP:")
z = re.match(r"^(([\w]{2})|([\w]{3})|([\w]{4}))([\s])(([\w]{3})$)", value)

print(z)

if z:
    print("match")




# https://regex101.com/
# hhttps://jex.im/regulex/#!flags=&re=%5B0-9%5D%7B5%7D-%5B%5Cd%5D%7B3%7D
# https://blog.geekhunter.com.br/python-regex/