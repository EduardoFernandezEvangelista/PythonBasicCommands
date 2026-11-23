print("=== Projeto 5: Repeticoes e Loops ===")

# for com range (contagem simples)
print("\n--- for com range(5) ---")
for i in range(5):
    print(i)

print("\n--- for com range(1, 6) ---")
for i in range(1, 6):
    print(i)

print("\n--- for com range(0, 10, 2) (passo 2) ---")
for i in range(0, 10, 2):
    print(i)

# for com lista
print("\n--- for com lista ---")
frutas = ["maca", "banana", "uva"]
for fruta in frutas:
    print(fruta)

# for com string
print("\n--- for com string ---")
for letra in "Python":
    print(letra)

# for com enumerate (indice + valor)
print("\n--- for com enumerate ---")
for indice, fruta in enumerate(frutas):
    print(indice, fruta)

# for com zip (varias listas paralelas)
print("\n--- for com zip ---")
nomes = ["Ana", "Joao", "Maria"]
idades = [25, 30, 28]
for nome, idade in zip(nomes, idades):
    print(nome, "-", idade)

# for com dicionario
print("\n--- for com dicionario (items) ---")
pessoa = {"nome": "Ana", "idade": 30, "cidade": "Sao Paulo"}
for chave, valor in pessoa.items():
    print(chave, ":", valor)

# while (contagem)
print("\n--- while ---")
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# while com break e continue
print("\n--- while com break e continue ---")
i = 0
while i < 10:
    i += 1
    if i == 3:
        continue  # pula o 3
    if i == 8:
        break     # para no 8
    print(i)

# for com break e continue
print("\n--- for com break e continue ---")
for i in range(1, 11):
    if i == 5:
        continue
    if i == 9:
        break
    print(i)

# loop com else (executa se nao houver break)
print("\n--- for com else ---")
for i in range(3):
    print(i)
else:
    print("Loop terminou sem break")

# Loop infinito controlado com break
print("\n--- while True com break ---")
tentativa = 0
while True:
    tentativa += 1
    if tentativa == 3:
        print("Saindo apos 3 tentativas")
        break

# Loop aninhado (for dentro de for)
print("\n--- Loop aninhado (tabuada) ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

# List comprehension (loop compacto para criar listas)
print("\n--- List comprehension ---")
quadrados = [x**2 for x in range(1, 6)]
print("Quadrados de 1 a 5:", quadrados)

pares = [x for x in range(1, 11) if x % 2 == 0]
print("Pares de 1 a 10:", pares)