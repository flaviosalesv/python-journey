# nota_filme = int(input('Qual nota você dá para este filme: '))

# if nota_filme == 9 or nota_filme == 10:
#     print('Excelente')
# elif nota_filme == 7 or nota_filme == 8:
#     print('Muito bom')
# elif nota_filme == 5 or nota_filme == 6:
#     print('Regular')
# else:
#     print('Ruim')




cliente_cadastrado = True
valor_do_produto = int(input('Qual o valor do seu produto? '))

if valor_do_produto >= 100 and cliente_cadastrado == True:
    print('Frete grátis aplicado!')
else:
    print('Frete não disponível gratuitamente.')