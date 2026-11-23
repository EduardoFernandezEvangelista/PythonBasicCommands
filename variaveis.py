print("=== Projeto 1: Variaveis e Tipos de Dados ===")

# Numericos
idade = 25                      # int
temperatura = -5                # int negativo
altura = 1.68                   # float
preco = 19.90                   # float
notacao_cientifica = 2.5e3      # float (2500.0)
grande_numero = 1_000_000       # int com separador visual
numero_complexo = 3 + 4j        # complex

# Texto
nome = "Ana Silva"              # str
sobrenome = 'Souza'             # str com aspas simples
mensagem_multilinha = """Esta e uma
string de varias linhas."""    # str multilinha

# Booleano
estudante = True                # bool
ativo = False                   # bool

# Sequencias / Collections
frutas = ["maca", "banana", "uva", "maca"]   # list (mutavel, ordenada, permite duplicados)
cores = ("vermelho", "verde", "azul")        # tuple (imutavel, ordenada)
pessoa = {"nome": "Ana", "idade": 30, "cidade": "Sao Paulo"}  # dict (chave: valor)
numeros_unicos = {1, 2, 3, 2, 1}             # set (nao ordenado, nao permite duplicados)

# Especial
resultado = None                # NoneType
dados_bytes = b"Hello Python"   # bytes

print("\n--- Numericos ---")
print("idade (int):", idade, type(idade))
print("temperatura (int):", temperatura, type(temperatura))
print("altura (float):", altura, type(altura))
print("preco (float):", preco, type(preco))
print("notacao_cientifica (float):", notacao_cientifica, type(notacao_cientifica))
print("grande_numero (int):", grande_numero, type(grande_numero))
print("numero_complexo (complex):", numero_complexo, type(numero_complexo))

print("\n--- Texto ---")
print("nome (str):", nome, type(nome))
print("sobrenome (str):", sobrenome, type(sobrenome))
print("mensagem_multilinha (str):", mensagem_multilinha, type(mensagem_multilinha))

print("\n--- Booleanos ---")
print("estudante (bool):", estudante, type(estudante))
print("ativo (bool):", ativo, type(ativo))

print("\n--- Collections ---")
print("frutas (list):", frutas, type(frutas))
print("cores (tuple):", cores, type(cores))
print("pessoa (dict):", pessoa, type(pessoa))
print("numeros_unicos (set):", numeros_unicos, type(numeros_unicos))

print("\n--- Especial ---")
print("resultado (NoneType):", resultado, type(resultado))
print("dados_bytes (bytes):", dados_bytes, type(dados_bytes))

# Conversoes de tipos (casting)
print("\n--- Conversoes (Casting) ---")
texto_numero = "10"
numero_inteiro = int(texto_numero)
numero_flutuante = float(texto_numero)
texto = str(idade)
print("int('10'):", numero_inteiro, type(numero_inteiro))
print("float('10'):", numero_flutuante, type(numero_flutuante))
print("str(25):", texto, type(texto))