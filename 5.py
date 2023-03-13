"""
5) Escreva um programa que inverta os caracteres de um string.



IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no
código;

b) Evite usar funções prontas, como, por exemplo, reverse;
"""
string = input('Insira qualquer palavra: ')

rev_string = ''
for i, _ in enumerate(string):
    rev_string += string[(len(string) - 1) - i]

print(rev_string)
