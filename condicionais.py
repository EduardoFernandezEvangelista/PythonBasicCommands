print("=== Projeto 4: Condicionais ===")

# if simples
nota = float(input("Digite a nota do aluno (0 a 10): "))
if nota >= 7:
    print("Aprovado!")

# if / else
if nota >= 7:
    print("Aprovado (if/else)!")
else:
    print("Reprovado (if/else).")

# if / elif / else
if nota >= 9:
    conceito = "A"
elif nota >= 8:
    conceito = "B"
elif nota >= 7:
    conceito = "C"
elif nota >= 6:
    conceito = "D"
else:
    conceito = "F"
print("Nota:", nota, "| Conceito:", conceito)

# Operador ternario (condicional em linha)
idade = int(input("\nDigite sua idade: "))
status = "Adulto" if idade >= 18 else "Menor de idade"
print("Status (ternario):", status)

# Condicional aninhado
tem_carteira = input("Tem carteira de motorista? (s/n): ").lower() == "s"
if idade >= 18:
    if tem_carteira:
        print("Pode dirigir.")
    else:
        print("E maior de idade, mas nao tem carteira.")
else:
    print("E menor de idade, nao pode dirigir.")

# Condicional com operadores logicos
tem_dinheiro = input("Tem dinheiro? (s/n): ").lower() == "s"
esta_aberto = input("O estabelecimento esta aberto? (s/n): ").lower() == "s"
if tem_dinheiro and esta_aberto:
    print("Pode comprar.")
elif tem_dinheiro or esta_aberto:
    print("Condicao parcial atendida.")
else:
    print("Nao pode comprar.")

# match / case (Python 3.10+) - semelhante a switch
dia = int(input("\nDigite um numero de 1 a 7 para o dia da semana: "))
match dia:
    case 1:
        nome_dia = "Segunda-feira"
    case 2:
        nome_dia = "Terca-feira"
    case 3:
        nome_dia = "Quarta-feira"
    case 4:
        nome_dia = "Quinta-feira"
    case 5:
        nome_dia = "Sexta-feira"
    case 6 | 7:  # varios valores
        nome_dia = "Final de semana"
    case _:
        nome_dia = "Invalido"
print("Dia:", nome_dia)

# match com estruturas (pattern matching)
ponto = (0, 5)
match ponto:
    case (0, 0):
        print("Ponto na origem")
    case (0, y):
        print(f"Ponto no eixo Y em {y}")
    case (x, 0):
        print(f"Ponto no eixo X em {x}")
    case (x, y):
        print(f"Ponto em ({x}, {y})")

# Condicional com 'in' (pertinencia)
letra = input("\nDigite uma letra: ").lower()
if letra in "aeiou":
    print("Vogal")
else:
    print("Consoante")

# Condicional com None
valor = None
if valor is None:
    print("Valor nao definido (None)")
elif valor is not None:
    print("Valor definido:", valor)