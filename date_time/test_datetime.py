from datetime import datetime, timedelta

data_atual = datetime.now()


# # Exercício 1 – Relógio de verificação
# # Mostre a hora atual no terminal, mas com a seguinte regra:
# # Se a hora for antes das 12h, imprima: "Bom dia!"
# if data_atual.hour <= 12:
#     print('Bom dia')

# # Se estiver entre 12h e 18h: "Boa tarde!"
# elif data_atual.hour > 12 and data_atual.hour < 18:
#     print('Boa tarde')

# # Depois disso: "Boa noite!"
# else:
#     print('Boa noite')



# Exercício 2 – Quantos meses faltam?
# Crie um programa que exiba quantos meses faltam para o ano acabar. Exemplo:

# meses_ate_final_do_ano = 12 - data_atual.month
# print(f'Faltam {meses_ate_final_do_ano} meses para o ano acabar')




# # Exercício 3 – Assinatura digital do terminal
# # Crie uma função que receba como argumento um nome, e exiba uma assinatura desta forma:

# # A data e horário devem ser do momento atual da assinatura
# nome = input('Digite seu nome: ')
# def assinatura_digital(nome):
#     print(f'Assinatura gerada por {nome} em {data_atual.day} do {data_atual.month} de {data_atual.year} às {data_atual.hour}:{data_atual.minute}')

# assinatura_digital(nome)



# Exercício 1 – Contagem regressiva para o fim do ano
# Mostre quantos dias faltam para o dia 31 de dezembro do ano atual.
# final_do_ano = datetime(2026, 12, 31)
# print(f'Faltam {final_do_ano.day - data_atual.day} dias e {final_do_ano.month - data_atual.month} meses para o final do ano')



# # Exercício 2 – Verificador de evento
# # Peça ao usuário que digite uma data de um evento
# pergunta_evento = input('Digite a data do evento conforme modelo(dd/mm/aaaa): ')
# data_evento = datetime.strptime(pergunta_evento,'%d/%m/%Y')
# # Mostre se o evento já aconteceu, se está acontecendo hoje, ou quantos dias faltam.

# if data_evento > data_atual:
#     print('O evento ainda não aconteceu')
# elif data_evento.day == data_atual.day and data_evento.month == data_atual.month and data_evento.year == data_atual.year:
#     print('Hoje é o dia do evento')
# elif data_evento < data_atual:
#     print('O evento já aconteceu')



# Exercício 3 – Validade de produto 🥫
# Considere que ele vence em 180 dias.
# Mostre:

# A data de validade

# Se o produto ainda está válido ou já venceu

# Quantos dias faltam ou há quanto tempo passou do prazo
validade_produto = timedelta(days=180)
data_validade = validade_produto + data_atual

if data_validade > data_atual:
    print('Produto válido')
elif data_validade < data_atual:
    print('Produto vencido')

print(f'O produto vence em {validade_produto.days} dias\nData de vencimento {data_validade.day}/{data_validade.month}/{data_validade.year}')