# Falta que detecte 6.1E-8 y -8.6
# Para correrlo YO tengo que hacerlo desde terminal con python3 /Users/nicolasperalta/Documents/TEC/IV\ SEMESTRE/MetodosComputacionales/Automata-1/automata.py


import re
from collections import namedtuple

# Definir los tipos de token
Token = namedtuple('Token', ['type', 'value'])

# Expresion para identificar los tokens
token_patterns = [
    (r'//.*', 'COMENTARIO'), 
    (r'\d+\.\d+', 'REAL'), 
    (r'\d+', 'ENTERO'), 
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'VARIABLE'),  
    (r'[=]', 'ASIGNACION'),  
    (r'[+]', 'SUMA'),  
    (r'[-]', 'RESTA'),  
    (r'[*]', 'MULTIPLICACION'),  
    (r'[/]', 'DIVISION'),  
    (r'[\^]', 'POTENCIA'),  
    (r'\(', 'PARENTHESIS_IZQUIERDO'),  
    (r'\)', 'PARENTHESIS_DERECHO'), 
    (r'\s+', None),  
]

# Funcion para tokenizar la entrada
def tokenize(code):
    tokens = []
    while code:
        match = None
        for pattern, token_type in token_patterns:
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                value = match.group(0)
                if token_type:
                    tokens.append(Token(token_type, value))
                break
        if not match:
            raise ValueError(f"Token no reconocido: {code}")
        code = code[len(match.group(0)):]
    return tokens

# leer el archivo de texto
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Leer expresiones desde un archivo de texto
file_path = 'expresiones.txt'  
input_code = read_file(file_path)

tokens = tokenize(input_code)

# Imprimir los tokens encontrados
print("Tokens encontrados:")
for token in tokens:
    print(f"Token: {token.value}  Tipo: {token.type}")
