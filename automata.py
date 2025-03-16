import re
from collections import namedtuple

# Definir los tipos de token
Token = namedtuple('Token', ['tipo', 'valor'])

# Expresión para identificar los tokens
patrones_token = [
    (r'//.*', 'COMENTARIO'),
    (r'\d+\.\d+(?:[eE][+-]?\d+)?', 'REAl'),
    (r'\d+', 'ENTERO'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'VARIABLE'),
    (r'[=]', 'ASIGNACION'),
    (r'[+]', 'SUMA'),
    (r'[-]', 'RESTA'),
    (r'[*]', 'MULTIPLICACION'),
    (r'[/]', 'DIVISION'),
    (r'[\^]', 'POTENCIA'),
    (r'\(', 'PARENTESIS_IZQUIERDO'),
    (r'\)', 'PARENTESIS_DERECHO'),
    (r'\s+', None),
]

# Función para tokenizar la entrada
def tokenizar(codigo):
    tokens = []
    while codigo:
        coincidencia = None
        for patron, tipo_token in patrones_token:
            regex = re.compile(patron)
            coincidencia = regex.match(codigo)
            if coincidencia:
                valor = coincidencia.group(0)
                if tipo_token:
                    tokens.append(Token(tipo_token, valor))
                break
        if not coincidencia:
            raise ValueError(f"Token no reconocido: {codigo}")
        codigo = codigo[len(coincidencia.group(0)):]
    return tokens

# Leer el archivo de texto
def leer_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return archivo.read()

# Leer expresiones desde un archivo de texto
ruta_archivo = 'expresiones.txt'
codigo_entrada = leer_archivo(ruta_archivo)

tokens = tokenizar(codigo_entrada)

# Imprimir los tokens encontrados
print("Tokens encontrados:")
for token in tokens:
    print(f"Token: {token.valor}  \t Tipo: {token.tipo}")
