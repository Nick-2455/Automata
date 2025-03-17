# Implementación de métodos computacionales
# Actividad 3.2: Programando un DFA
# Nicolas Pacheco Peralta A01255150
# Jesús Felipe Bastidas Valenzuela A01255206
# Fecha de creacion: 14 de marzo de 2025
# Fecha de modificacion: 16 de marzo de 2025

import os
import re
from collections import namedtuple

# Definir los tipos de token
Token = namedtuple('Token', ['type', 'value'])

# Expresión para identificar los tokens
token_patterns = [
    (r'//.*', 'COMENTARIO'), 
    (r'[-+]?\d*\.\d+(?:[eE][-+]?\d+)?', 'REAL'), 
    (r'[-+]?\d+', 'ENTERO'), 
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'VARIABLE'),  
    (r'[=]', 'ASIGNACION'),  
    (r'[+]', 'SUMA'),  
    (r'[-]', 'RESTA'),  
    (r'[*]', 'MULTIPLICACION'),  
    (r'[/]', 'DIVISION'),  
    (r'[\^]', 'POTENCIA'),  
    (r'\(', 'PARENTESIS QUE ABRE'),  
    (r'\)', 'PARENTESIS QUE CIERRA'), 
    (r'\s+', None),  
]

# Función para tokenizar la entrada
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

# Leer el archivo de texto
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Leer expresiones desde un archivo de texto
file_path = input("Inserte el nombre del archivo a analizar (tiene que agregar la terminacion del documento, ejemplo: expresiones.txt) :")

while (os.path.exists(file_path) != True):
    print("\nArchivo no existe. Inserte el nombre de un archivo valido")
    file_path = input("\nInserte el nombre del archivo a analizar (tiene que agregar la terminacion del documento, ejemplo: expresiones.txt) :")



input_code = read_file(file_path)

tokens = tokenize(input_code)

# Imprimir los tokens encontrados
print("Tokens encontrados:")
for token in tokens:
    print(f"Token: {token.value}  Tipo: {token.type}")
