# pessoa = {
#     'nome': 'Flávio',
#     'idade': 34,
#     'cidade': 'Bauru'
# }
# print(pessoa['nome'])



# Crie um dicionário chamado livro com as chaves: "titulo", "autor" e "ano".
# livro = {
#     'titulo': 'Vamo que vamo',
#     'autor': 'Jackson Joe',
#     'ano': 2026
# }
# Depois, mostre cada valor usando print().
# print(livro['titulo'])
# print(livro['autor'])
# print(livro['ano'])


# Peça para o usuário digitar nome e idade. Guarde esses dados em um dicionário chamado usuario.
# Depois, verifique se a idade é maior ou igual a 18:

# Se sim, imprima: "Acesso liberado para {nome}"

# Se não, imprima: "Acesso negado para {nome}"

# nome = input('Digite seu nome: ')
# idade = int(input('Digite sua idade: '))
# usuario = {'Nome': nome,
#            'Idade':idade}
# print(usuario)
# if idade >= 18:
#     print(f"Acesso liberado para {nome}")
# else:
#     print(f"Acesso negado para {nome}")

# Crie um sistema de login com dois dicionários: um que guarda as credenciais corretas, e outro dicionário que guarde as informações inseridas pelo usuário. Peça ao usuário para digitar o usuário e senha, e verifique se está correto de acordo com o primeiro dicionário.

# Se o usuário e a senha estão corretos → "Login bem-sucedido"

# Senão → "Usuário ou senha incorretos"

credenciais_corretas = {
    'login': 'flaviosalesv',
    'senha': 2026}

login = input('Digite seu login: ')
senha = int(input('Digite sua senha: '))

credenciais_usuario = {
    'login': login,
    'senha': senha
}

if credenciais_usuario['login'] == credenciais_corretas['login'] and credenciais_usuario['senha'] == credenciais_corretas['senha']:
    print("Login bem-sucedido")
else:
    print("Usuário ou senha incorretos")