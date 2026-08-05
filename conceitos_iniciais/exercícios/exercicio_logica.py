# salario = int(2500)
# horas_trabalhadas = int(160)

# valor_da_hora_trabalhada = salario / horas_trabalhadas
# print(valor_da_hora_trabalhada)


# nome_visitante = str(input('Qual é seu nome? '))
# print(f'Seja bem vindo {nome_visitante}')


# numero1 = int(input('Digite o primeiro número: '))
# numero2 = int(input('Digite o segundo número: '))

# if numero1 > numero2:
#     print('O primeiro número é maior')
# else:
#     print('O segundo número é maior')


# idades = [15,46,75,34,23]
# total = 0
# for idade in idades:
#     total = total + idade
# print(total)



numero_correto = int(9)
numero_escolhido = int(input('Chute o número correto de 1 a 10: '))

if numero_escolhido > numero_correto:
    print('O número correto é menor')
elif numero_escolhido < numero_correto:
    print('O número correto é maior')
else:
    print('Você acertou o número!')
