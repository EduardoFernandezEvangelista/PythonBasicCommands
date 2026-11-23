print("=== Projeto 2: Metodos e Funcoes ===")

# Funcao simples
def saudacao(nome):
    return "Ola, " + nome + "! Bem-vindo."

# Funcao com parametro default (valor padrao)
def apresentar(nome, curso="Python"):
    return nome + " estuda " + curso

# Funcao com retorno multiplo (retorna tupla)
def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b if b != 0 else None
    return soma, subtracao, multiplicacao, divisao

# Funcao com *args (varios argumentos posicionais)
def soma_todos(*numeros):
    total = 0
    for n in numeros:
        total += n
    return total

# Funcao com **kwargs (varios argumentos nomeados)
def mostrar_dados(**dados):
    for chave, valor in dados.items():
        print(f"  {chave}: {valor}")

# Funcao lambda (anonima)
quadrado = lambda x: x ** 2
soma_lambda = lambda a, b: a + b

# Funcao dentro de funcao (closure simples)
def contador_externo():
    contador = 0
    def incrementar():
        nonlocal contador
        contador += 1
        return contador
    return incrementar

print("\n--- Funcoes Simples ---")
print(saudacao("Carlos"))

print("\n--- Parametro Default ---")
print(apresentar("Joao"))
print(apresentar("Joao", "Java"))

print("\n--- Retorno Multiplo ---")
s, sub, m, d = operacoes(10, 5)
print("operacoes(10, 5):", s, sub, m, d)

print("\n--- *args ---")
print("soma_todos(1,2,3,4,5):", soma_todos(1, 2, 3, 4, 5))

print("\n--- **kwargs ---")
print("mostrar_dados:")
mostrar_dados(nome="Ana", idade=25, cidade="SP")

print("\n--- Lambda ---")
print("quadrado(5):", quadrado(5))
print("soma_lambda(3,7):", soma_lambda(3, 7))

print("\n--- Closure (funcao dentro de funcao) ---")
contar = contador_externo()
print("contar():", contar())
print("contar():", contar())
print("contar():", contar())

# Metodos de string
print("\n--- Metodos de String ---")
texto = "  Python e Incrivel  "
print("strip():", repr(texto.strip()))
print("lower():", texto.lower())
print("upper():", texto.upper())
print("title():", texto.title())
print("replace('Python','Java'):", texto.replace("Python", "Java"))
print("split():", texto.split())
print("startswith('Py'):", texto.startswith("Py"))
print("endswith('vel'):", texto.endswith("vel"))
print("find('e'):", texto.find("e"))
print("isdigit():", "123".isdigit())
print("isalpha():", "abc".isalpha())
print("isspace():", "   ".isspace())
print("join(['a','b','c']):", "-".join(["a", "b", "c"]))

# Metodos de lista
print("\n--- Metodos de Lista ---")
lista = [3, 1, 4, 1, 5]
lista.append(9)
print("append(9):", lista)
lista.insert(1, 100)
print("insert(1,100):", lista)
lista.remove(1)
print("remove(1):", lista)
lista.sort()
print("sort():", lista)
lista.reverse()
print("reverse():", lista)
print("pop():", lista.pop())
print("count(1):", lista.count(1))
print("copy():", lista.copy())
print("clear():", end=" ")
lista.clear()
print(lista)

# Metodos de dicionario
print("\n--- Metodos de Dicionario ---")
d = {"a": 1, "b": 2, "c": 3}
print("keys():", list(d.keys()))
print("values():", list(d.values()))
print("items():", list(d.items()))
print("get('a'):", d.get("a"))
print("get('z', 'nao encontrado'):", d.get("z", "nao encontrado"))
d.pop("b")
print("pop('b'):", d)
d.clear()
print("clear():", d)

# Metodos de set
print("\n--- Metodos de Set ---")
s1 = {1, 2, 3}
s2 = {3, 4, 5}
print("s1:", s1)
print("s2:", s2)
print("uniao (|):", s1 | s2)
print("intersecao (&):", s1 & s2)
print("diferenca (-):", s1 - s2)
s1.add(4)
print("add(4):", s1)
s1.discard(2)
print("discard(2):", s1)

# Escopo de variaveis
print("\n--- Escopo ---")
variavel_global = "sou global"

def escopo():
    variavel_local = "sou local"
    print("  Dentro da funcao:", variavel_local)

escopo()
print("  Fora da funcao:", variavel_global)