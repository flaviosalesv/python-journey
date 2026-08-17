nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
print('')

if idade >= 18:
    print(f'Muito prazer {nome}, você possui {idade} anos e já é maior de idade!\n')
else:
    print(f'Muito prazer {nome}, você possui {idade} anos mas ainda não é maior de idade!\n')

input('Pressione ENTER para fechar')