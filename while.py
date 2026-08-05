# contador = 1

# while contador <= 5:
#     print(f'Contando {contador}')
#     contador +=1


# senha = ''

# while senha != 'python':
#     senha = input('digite sua senha: ')

# print('senha correta')

# for numero in range (1, 6):
#     print(numero)

# produtos = ['bolacha', 'pão', 'cerveja', 'carne']

# for produto in produtos:
#     print(f'Temos {produto} em estoque')


#Crie um programa que imprime os números de 10 até 1 usando um loop while.
# numero = 10
# while numero >= 1:
#     print(f'Número {numero}')
#     numero -=1




#Usando loops, peça 5 números ao usuário (com input()), some todos e mostre o resultado.

numero_digitado = 0
numeros = []
soma_dos_numeros = 0

for n in range(5):
    
    numero_digitado = int(input('Digite um número: '))
    numeros.append(numero_digitado)
    soma_dos_numeros += numero_digitado
    

print(soma_dos_numeros)
print(numeros)












#Peça ao usuário que vá digitando valores para guardar no cofrinho (em reais).
#Quando o usuário digitar 0, o programa para e mostra o total economizado.
# valor = ''

# while valor != 0:
#     valor = int(input('Digite um valor para guardar no cofrinho: '))
#     if valor != 0:
#         print(f'Você depositou {valor} no cofrinho')
#     elif valor == 0:
#         break
#     else:
#         print('Digite um valor válido')

    








# Crie um sistema de votação onde o usuário escolhe entre:

# 1."Pizza"

# 2."Hambúrguer"

# 3."Sair"

# Enquanto ele não digitar "3", continue perguntando

# No final, mostre quantos votos cada item recebeu


# voto = ''
# pizza1 = 0
# hamburguer2 = 0


# while voto != 3:
#     voto = int(input('Digite 1 para pizza, 2 para hamburguer e 3 para sair. '))
#     if voto == 1:
#         pizza1 = pizza1 + 1
#         print('Você votou em pizza')
#         print(pizza1)
#     elif voto == 2:
#         hamburguer2 = hamburguer2 + 1
#         print('Você votou em hamburguer')
#         print(hamburguer2)
#     else:
#         print('Você digitou um código inválido. Escolha 1 para pizza, 2 para hamburguer ou 3 para sair.')

# print(f'Total de:\n{pizza1} votos para Pizza\n{hamburguer2} votos para Hamburguer')
    

