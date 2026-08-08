from mensagens import boas_vindas
from matematica import dobro, metade

nome = input('Digite seu nome: ')
boas_vindas(nome)

numero = int(input('Digite um número para descobrir seu dobro e sua metade: '))
dobro(numero)
metade(numero)