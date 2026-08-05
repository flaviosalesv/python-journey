escolha_comida = int(input('Digite o número da comida desejada:\n 1 - Pizza\n 2 - Sushi\n 3 - Salada '))
match escolha_comida:
    case 1:
        print('Você escolheu Pizza!')
    case 2:
        print('Você escolheu Sushi')
    case 3:
        print('Você escolheu Salada')
    case _:
        print('Opção inválida')


# escolha_veiculo = int(input('Escolha um meio de transporte: 1-carro, 2-bicicleta ou 3-avião: '))
# match escolha_veiculo:
#     case 1:
#         print('Carro')
#     case 2:
#         print('Bicicleta')
#     case 3:
#         print('Avião')
#     case _:
#         print('Opção inválida')