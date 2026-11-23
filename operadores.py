print("=== Projeto 6: Operadores ===")

a = 10
b = 3

print(f"a = {a}, b = {b}")

# Operadores aritmeticos
print("\n--- Aritmeticos ---")
print("Soma (+):", a + b)
print("Subtracao (-):", a - b)
print("Multiplicacao (*):", a * b)
print("Divisao (/):", a / b)
print("Divisao inteira (//):", a // b)
print("Resto da divisao / Modulo (%):", a % b)
print("Potenciacao (**):", a ** b)

# Operadores de comparacao
print("\n--- Comparacao ---")
print("a == b (igual):", a == b)
print("a != b (diferente):", a != b)
print("a > b (maior que):", a > b)
print("a < b (menor que):", a < b)
print("a >= b (maior ou igual):", a >= b)
print("a <= b (menor ou igual):", a <= b)

# Operadores logicos
x = True
y = False
print("\n--- Logicos ---")
print("x and y (E):", x and y)
print("x or y (OU):", x or y)
print("not x (NAO):", not x)

# Operadores de atribuicao
print("\n--- Atribuicao ---")
c = 5
c += 2   # c = c + 2
print("c += 2:", c)
c -= 1   # c = c - 1
print("c -= 1:", c)
c *= 3   # c = c * 3
print("c *= 3:", c)
c /= 2   # c = c / 2
print("c /= 2:", c)
c //= 2  # c = c // 2
print("c //= 2:", c)
c %= 2   # c = c % 2
print("c %= 2:", c)
c **= 2  # c = c ** 2
print("c **= 2:", c)

# Operadores de identidade
print("\n--- Identidade ---")
x1 = [1, 2, 3]
y1 = [1, 2, 3]
z1 = x1
print("x1 is y1:", x1 is y1)       # False (objetos diferentes na memoria)
print("x1 is z1:", x1 is z1)       # True (mesmo objeto na memoria)
print("x1 is not y1:", x1 is not y1)

# Operadores de pertinencia (membros)
print("\n--- Pertinencia (Membros) ---")
lista_num = [1, 2, 3, 4, 5]
print("3 in lista_num:", 3 in lista_num)        # True
print("10 in lista_num:", 10 in lista_num)      # False
print("3 not in lista_num:", 3 not in lista_num) # False
texto_palavra = "Hello World"
print("'World' in texto:", "World" in texto_palavra)  # True
print("'Python' in texto:", "Python" in texto_palavra) # False

# Operadores bitwise
print("\n--- Bitwise ---")
p = 5   # 0101
q = 3   # 0011
print("p & q (AND):", p & q)    # 1
print("p | q (OR):", p | q)     # 7
print("p ^ q (XOR):", p ^ q)    # 6
print("~p (NOT):", ~p)          # -6
print("p << 1 (deslocamento esquerda):", p << 1)  # 10
print("p >> 1 (deslocamento direita):", p >> 1)   # 2

# Operador walrus (atribuicao em expressao) - Python 3.8+
print("\n--- Walrus (:=) ---")
texto = "Python"
if (n := len(texto)) > 5:
    print("String longa, tamanho:", n)

# Operador de pertinencia em strings
print("\n--- Pertinencia em string ---")
print("'Py' in 'Python':", "Py" in "Python")
print("'py' in 'Python':", "py" in "Python")