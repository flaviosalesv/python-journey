import random

# 🥇 Exercício — Sorteio de Prêmios em uma Festa
# Você está organizando uma festa e tem 5 prêmios diferentes para sortear entre os convidados.

# Cada convidado só pode ganhar um único prêmio.

# Os prêmios também não podem se repetir (obviamente).

# No final, mostre qual convidado ganhou qual prêmio.

# Use as seguintes listas:

convidados = ["Ana", "Lucas", "João", "Marina", "Pedro", "Carla", "Ricardo", "Fernanda"]
premios = ["Bicicleta", "Tablet", "Fone de ouvido", "Livro", "Camisa"]

convidado_sorteado = random.sample(convidados, k=5)
premio_sorteado = random.sample(premios, k=5)
posição= 0

for c in convidado_sorteado:
    print(f'O convidado sorteado foi {c} que ganhou {premio_sorteado[posição]}')
    posição+=1
  
    



