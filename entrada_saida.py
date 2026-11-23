print("=== Projeto 3: Entrada e Saida ===")

# input() - leitura do terminal
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
cidade = input("Digite sua cidade: ")
altura = input("Digite sua altura (m): ")

# print() - saida para o terminal
print("\n--- Dados informados ---")
print("Nome:", nome)
print("Idade:", idade)
print("Cidade:", cidade)
print("Altura:", altura, "m")

# Saida com concatenacao
print("\nOla", nome, ", voce tem", idade, "anos e mora em", cidade + ".")

# Saida com f-string (formatacao moderna)
print("\n--- Usando f-strings ---")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Cidade: {cidade}")
print(f"Altura: {altura} m")
print(f"{nome} nasceu em aproximadamente {2026 - int(idade)}.")

# Saida com .format()
print("\n--- Usando .format() ---")
print("Nome: {} | Idade: {} | Cidade: {}".format(nome, idade, cidade))

# Saida com % (formato antigo)
print("\n--- Usando % (formato antigo) ---")
print("Nome: %s | Idade: %s" % (nome, idade))

# input com conversao de tipo
print("\n--- Conversao de tipo na entrada ---")
numero1 = int(input("Digite um numero inteiro: "))
numero2 = float(input("Digite um numero decimal: "))
print("Soma:", numero1 + numero2)

# print com separador e fim personalizados
print("\n--- print com sep e end ---")
print("A", "B", "C", sep="-")
print("Linha 1", end=" ")
print("Linha 2")

# Leitura de varios valores em uma linha
print("\n--- Varios valores em uma linha ---")
valores = input("Digite tres numeros separados por espaco: ").split()
print("Valores lidos:", valores)
print("Quantidade de valores:", len(valores))

# Saida formatada com alinhamento
print("\n--- Alinhamento ---")
print(f"{'Produto':<10} | {'Preco':>10}")
print(f"{'Maca':<10} | {2.50:>10.2f}")
print(f"{'Banana':<10} | {1.80:>10.2f}")