ano_atual = int (input ('Em que ano estamos? Resposta: '))
ano_nascimento = int (input ('Em que ano você nasceu? Resposta: '))
anos_de_vida = ano_atual - ano_nascimento

print(f'Você tem {anos_de_vida} anos')
print('_______________________________________________________________________________')

nota_matemática = int (input('Nota de Matemática: '))
nota_portugues = int (input('Nota de Português: '))
nota_ingles = int (input('Nota de Inglês: '))
media_das_notas = (nota_matemática + nota_portugues + nota_ingles)/3

print(f'A média de suas notas é: {media_das_notas}')