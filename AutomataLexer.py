class AutomataLexer:
    def __init__(self):
        self.estado = 'q0'
        self.token_actual = ""
        self.tokens = []
    
    def transicion(self, caracter):
        """
        Cambia el estado del autómata basado en el carácter actual.
        """
        if self.estado == 'q0':
            if caracter.isalpha():  # Identificadores (variables)
                self.estado = 'q_var'
            elif caracter.isdigit():  # Números enteros
                self.estado = 'q_int'
            elif caracter in "+-*/^=":  # Operadores
                self.estado = 'q_op'
            elif caracter in "()":  # Paréntesis
                self.estado = 'q_par'
            elif caracter == '.':  # Posible número flotante
                self.estado = 'q_float'
            elif caracter == '/':  # Comentarios "//"
                self.estado = 'q_comment_start'
            elif caracter.isspace():  # Ignorar espacios en blanco
                return
            else:
                self.estado = 'q_error'
        
        elif self.estado == 'q_var':
            if not (caracter.isalnum() or caracter == '_'):
                self.finalizar_token()
                self.transicion(caracter)  # Volver a procesar el carácter

        elif self.estado == 'q_int':
            if caracter == '.':
                self.estado = 'q_float'
            elif caracter in "Ee":
                self.estado = 'q_exp'
            elif not caracter.isdigit():
                self.finalizar_token()
                self.transicion(caracter)

        elif self.estado == 'q_float':
            if caracter.isdigit():
                pass  # Sigue siendo parte del número flotante
            elif caracter in "Ee":
                self.estado = 'q_exp'
            else:
                self.finalizar_token()
                self.transicion(caracter)

        elif self.estado == 'q_exp':
            if caracter in "+-" or caracter.isdigit():
                pass  # Parte de la notación exponencial
            else:
                self.finalizar_token()
                self.transicion(caracter)

        elif self.estado == 'q_op':
            self.finalizar_token()
            self.transicion(caracter)

        elif self.estado == 'q_par':
            self.finalizar_token()
            self.transicion(caracter)

        elif self.estado == 'q_comment_start':
            if caracter == '/':
                self.estado = 'q_comment'
            else:
                self.finalizar_token()
                self.transicion(caracter)

        elif self.estado == 'q_comment':
            if caracter == '\n':
                self.finalizar_token()
                self.transicion(caracter)

        elif self.estado == 'q_error':
            print(f"Error: Token no reconocido '{self.token_actual}'")
            self.token_actual = ""
            self.estado = 'q0'

        self.token_actual += caracter

    def finalizar_token(self):
        """
        Guarda el token identificado y reinicia el estado.
        """
        if self.token_actual:
            tipo = self.obtener_tipo_token(self.estado)
            self.tokens.append((self.token_actual.strip(), tipo))
        self.token_actual = ""
        self.estado = 'q0'

    def obtener_tipo_token(self, estado):
        """
        Retorna el tipo de token según el estado final alcanzado.
        """
        tipos = {
            'q_var': "Variable",
            'q_int': "Entero",
            'q_float': "Real",
            'q_exp': "Real",
            'q_op': "Operador",
            'q_par': "Paréntesis",
            'q_comment': "Comentario"
        }
        return tipos.get(estado, "Desconocido")

    def analizar(self, linea):
        """
        Analiza una línea de código y genera los tokens correspondientes.
        """
        for caracter in linea:
            self.transicion(caracter)
        self.finalizar_token()  # Capturar último token
        return self.tokens


def lexerAritmetico(archivo):
    """
    Función principal para analizar un archivo de expresiones.
    """
    automata = AutomataLexer()
    with open(archivo, 'r', encoding='utf-8') as file:
        for linea in file:
            tokens = automata.analizar(linea.strip())
            for token, tipo in tokens:
                print(f'{token:<20} {tipo}')


if __name__ == "__main__":
    archivo_entrada = "expresiones.txt"  # Asegúrate de que este archivo exista
    lexerAritmetico(archivo_entrada)
