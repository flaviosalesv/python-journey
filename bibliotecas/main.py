import random

numero_aleatorio = random.randint(1, 10)


while True:
    numero_escolhido = int(input('Escolha um número de 1 a 10: '))
    if numero_escolhido > numero_aleatorio:
        print('Muito alto')
        
    elif numero_escolhido < numero_aleatorio:
        print('Muito baixo')
    else:
        print('Acertou')
        break