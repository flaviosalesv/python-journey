from perfil.usuario import criar_perfil
from perfil.validacao import idade_valida

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

if idade_valida(idade) == True:
    print('Acesso autorizado')
    criar_perfil(nome, idade)
else:
    print('Acesso negado')