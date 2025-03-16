import re

def lexerAritmetico(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()
    
    tokens = []
    patrones = [
        (r'//.*', 'Comentario'),
        (r'[a-zA-Z_][a-zA-Z0-9_]*', 'Variable'),
        (r'\d+\.\d+(?:[eE][+-]?\d+)?', 'Real'),
        (r'\d+', 'Entero'),
        (r'=', 'Asignación'),
        (r'\+', 'Suma'),
        (r'-', 'Resta'),
        (r'\*', 'Multiplicación'),
        (r'/', 'División'),
        (r'\^', 'Potencia'),
        (r'\(', 'Paréntesis que abre'),
        (r'\)', 'Paréntesis que cierra'),
        (r'\s+', None)  # Ignorar espacios en blanco
    ]
    
    for linea in lineas:
        i = 0
        while i < len(linea):
            for patron, tipo in patrones:
                regex = re.compile(patron)
                match = regex.match(linea, i)
                if match:
                    if tipo:
                        tokens.append((match.group(), tipo))
                    i = match.end()
                    break
            else:
                i += 1
    
    print("Token\tTipo")
    print("-" * 20)
    for token, tipo in tokens:
        print(f"{token}\t{tipo}")

# Prueba del lexer con un archivo de ejemplo
lexerAritmetico('expresiones.txt')


if __name__ == "__main__":
    archivo_entrada = "expresiones.txt"  # Asegúrate de que este archivo exista
    lexerAritmetico(archivo_entrada)
