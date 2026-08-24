import sqlite3

conexao = sqlite3.connect('studies_db.db')
cursor = conexao.cursor()

produto_nome = input('Digite o nome do produto que deseja inserir: ')
produto_preco = float(input('Digite o preço do produto: '))

cursor.execute(f'INSERT INTO produtos (nome, preco) VALUES (?,?)', (produto_nome, produto_preco))
cursor.execute('SELECT * FROM produtos')

produtos = cursor.fetchall()

print(produtos)

conexao.commit()