
from openpyxl import Workbook
# Exercício 1 – Cadastro simples
# Crie um arquivo chamado cadastro.xlsx com uma aba chamada Pessoas.
# Adicione os seguintes dados nas células manualmente (com planilha["A1"] = ...):

# | Nome     | Cidade         |
# |----------|----------------|
# | João     | Recife         |
# | Marina   | São Paulo      |
# | Otávio   | Belo Horizonte |
# E salve o arquivo
# Exercício 2 – Adicionando dados com append
# No mesmo arquivo cadastro.xlsx, adicione mais duas pessoas na aba Pessoas utilizando o método append():

# Letícia, Porto Alegre

# Gustavo, Salvador
# Exercício 3 – Multiplas abas e estrutura de planilha
# Crie uma nova aba chamada Visitas.

# Escreva a estrutura da tabela:

# | Data       | Visitantes |
# |------------|------------|
# | 01/01/2025 | 134        |
# | 02/01/2025 | 156        |
# Na aba Visitas, sobrescreva o número de visitantes do dia 01/01/2025 para 142

arquivo = Workbook()

planilha_atual = arquivo.active
planilha_atual.title = 'Cadastros'
planilha_atual.append(['Pessoas','Cidade'])
planilha_atual['A2'] = 'João'
planilha_atual['A3'] = 'Marina'
planilha_atual['A4'] = 'Otávio'
planilha_atual['B2'] = 'Recife'
planilha_atual['B3'] = 'São Paulo'
planilha_atual['B4'] = 'Belo Horizonte'
planilha_atual.append(['Leticia', 'Porto Alegre'])
planilha_atual.append(['Gustavo', 'Salvador'])

arquivo.create_sheet('Visitas')

planilha_visitas = arquivo['Visitas']
planilha_visitas.append(['Data','Visitantes'])
planilha_visitas.append(['01/01/2025', '134'])
planilha_visitas.append(['02/01/2025', '156'])
planilha_visitas['B2'] = '142'


arquivo.save('cadastros.xlsx')