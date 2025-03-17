Instituto Tecnológico y de Estudios Superiores de Monterrey: Campus Sonora Norte
Actividad 3.2: Programando un DFA
UF: Implementación de métodos computacionales
Profesor: Baldomero Olvera Villanueva
Grupo: 601
Alumnos:
Nicolas Pacheco Peralta - A01255150
Jesús Felipe Bastidas Valenzuela - A01255206


### **Manual de usuario**

#### **1. Descripción del programa**

Este programa está diseñado para tokenizar expresiones matemáticas y de programación, identificando y clasificando los diferentes componentes como números enteros, números reales, variables, operadores, paréntesis, y comentarios. El programa está escrito en **Python** y utiliza expresiones regulares para identificar los distintos tipos de tokens en el código de entrada.
![image](https://github.com/user-attachments/assets/16703efa-bc81-4734-941a-3992343a4ea0)

#### **2. Lenguaje de programación utilizado**

Este programa está desarrollado en el lenguaje de **Python**.

#### **3. Requisitos previos**

Antes de ejecutar el programa, debe tener instalada la versión de Python 3 en su sistema. Puede descargar e instalar Python desde el siguiente enlace oficial:  
[Python Oficial](https://www.python.org/downloads/)

Además, el programa utiliza la biblioteca estándar de Python `re` (expresiones regulares) y `collections` (para el uso de `namedtuple`). Estas bibliotecas están incluidas por defecto en Python, por lo que no necesita instalar nada adicional.

Si el sistema muestra una versión de Python 3, está listo para ejecutar el programa.

#### **4. Archivos necesarios**

- **Archivo de código fuente:** `automata.py` (Este es el archivo que contiene el programa en Python).
- **Archivo de entrada:** El usuario introduce el nombre del archivo a analizar, ejemplo: `expresiones.txt` (Este archivo contiene el código o las expresiones a analizar).

#### **5. Cómo ejecutar el programa**

Para ejecutar el programa, siga estos pasos:

1. Asegúrese de tener el archivo `expresiones.txt` con el contenido que desea tokenizar.
2. Asegúrese de que el archivo `automata.py` y `expresiones.txt` esten en la misma carpeta.
3. Abra una terminal o línea de comandos en esa carpeta.
4. Ejecute el siguiente comando para correr el programa:

```bash
python automata.py
```

#### **6. Qué esperar como salida**

Cuando ejecute el programa, el script leerá el archivo `expresiones.txt`, procesará su contenido y generará una lista de tokens encontrados. Los tokens se mostrarán en la terminal o línea de comandos, con su valor y tipo. 

##### Ejemplo de salida:
```plaintext
Tokens encontrados:
Token: 10  Tipo: ENTERO
Token: +  Tipo: SUMA
Token: 20  Tipo: ENTERO
Token: *  Tipo: MULTIPLICACION
Token: (  Tipo: PARENTESIS_IZQUIERDO
Token: x  Tipo: VARIABLE
Token: )  Tipo: PARENTESIS_DERECHO
Token: // Comentario de ejemplo  Tipo: COMENTARIO
```

#### **7. Descripción del autómata**

El autómata para este problema es un autómata de tipo **determinista** que recorre el código de entrada de izquierda a derecha, reconociendo patrones específicos definidos por las expresiones regulares.

##### Diagrama del autómata:

![image](https://github.com/user-attachments/assets/67ff9013-4bcf-45f6-93db-9ce3d28c2ffb)

1. El autómata comienza en un estado inicial.
2. Luego, lee el siguiente símbolo de la entrada.
3. Según el símbolo leído, el autómata hace una transición a un estado correspondiente:
   - Si el símbolo es un número (ya sea entero o real), se transita al estado que valida los números.
   - Si el símbolo es una letra o un guion bajo, se transita a un estado que valida las variables.
   - Si el símbolo es un operador o un paréntesis, el autómata lo clasifica directamente como un token.
4. Si encuentra un comentario (indicador `//`), el autómata transita a un estado donde consume todo el comentario.
5. Si el autómata no puede reconocer un símbolo, genera un error indicando que el token no es reconocido.

El autómata sigue estas reglas hasta que toda la entrada ha sido procesada, y luego devuelve todos los tokens identificados.



#### **8. Conclusion**

Este programa le permitirá tokenizar expresiones matemáticas o de programación de manera eficiente y ordenada. A través de su ejecución, podrá descomponer el código de entrada en sus componentes básicos (tokens), lo que es útil para el análisis de expresiones en un lenguaje específico.

#### **9. Casos de Pruebas**

Los casos de pruebas tiene la función de verificar que el programa cumpla con las salidas que debe de dar, es una forma que tenemos como desarrolladores para poder autentificar que este todo en orden.

##### **Caso de prueba base**

El caso de prueba base es aquel que es dado en el ejemplo de la plataforma, al cual se le asigna el nombre de `expresiones.txt`, el cual contiene lo siguiente:
```plaintext
b=7
a = 32.4 *(-8.6 - b)/ 6.1E-8
d = a ^ b // Esto es un comentario
```
El python de `automata.py` debe de recibir la entrada del archivo a analizar, en este caso se insetara el nombre del archivo `expresiones.txt`:

```plaintext
Inserte el nombre del archivo a analizar (tiene que agregar la terminacion del documento, ejemplo: expresiones.txt) :expresiones.txt
```
Una vez hecho esto, el programa imprimira en pantalla el siguiente resultado:

```plaintext
Tokens encontrados:
Token: b  Tipo: VARIABLE
Token: =  Tipo: ASIGNACION
Token: 7  Tipo: ENTERO
Token: a  Tipo: VARIABLE
Token: =  Tipo: ASIGNACION
Token: 32.4  Tipo: REAL
Token: *  Tipo: MULTIPLICACION
Token: (  Tipo: PARENTHESIS QUE ABRE
Token: -8.6  Tipo: REAL
Token: -  Tipo: RESTA
Token: b  Tipo: VARIABLE
Token: )  Tipo: PARENTHESIS QUE CIERRA
Token: /  Tipo: DIVISION
Token: 6.1E-8  Tipo: REAL
Token: d  Tipo: VARIABLE
Token: =  Tipo: ASIGNACION
Token: a  Tipo: VARIABLE
Token: ^  Tipo: POTENCIA
Token: b  Tipo: VARIABLE
Token: // Esto es un comentario  Tipo: COMENTARIO
```

##### **Primer Caso de pruebas**

Al primer caso de pruebas se le asigna el nombre de `expresiones1.txt`, el cual contiene lo siguiente:
```plaintext
x = 15.2 * (4.3 - y) / 2.5E-6
z = x ^ y // Operacion exponencial
```
El python de `automata.py` debe de recibir la entrada del archivo a analizar, en este caso se insetara el nombre del archivo `expresiones1.txt`:

```plaintext
Inserte el nombre del archivo a analizar (tiene que agregar la terminacion del documento, ejemplo: expresiones.txt) :expresiones1.txt
```
Una vez hecho esto, el programa imprimira en pantalla el siguiente resultado:

```plaintext
Tokens encontrados:
Token: x  Tipo: VARIABLE
Token: =  Tipo: ASIGNACION
Token: 15.2  Tipo: REAL
Token: *  Tipo: MULTIPLICACION
Token: (  Tipo: PARENTESIS QUE ABRE
Token: 4.3  Tipo: REAL
Token: -  Tipo: RESTA
Token: y  Tipo: VARIABLE
Token: )  Tipo: PARENTESIS QUE CIERRA
Token: /  Tipo: DIVISION
Token: 2.5E-6  Tipo: REAL
Token: z  Tipo: VARIABLE
Token: =  Tipo: ASIGNACION
Token: x  Tipo: VARIABLE
Token: ^  Tipo: POTENCIA
Token: y  Tipo: VARIABLE
Token: // Operacion exponencial  Tipo: COMENTARIO
```


##### **Segundo caso de pruebas**

Al segundo caso de pruebas se le asigna el nombre de `expresiones2.txt`, el cual contiene lo siguiente:
```plaintext
m = 89 / (7.2 + n) * 3.1E-4
p = m ^ n // Calculo de potencia
```
El python de `automata.py` debe de recibir la entrada del archivo a analizar, en este caso se insetara el nombre del archivo `expresiones2.txt`:

```plaintext
Inserte el nombre del archivo a analizar (tiene que agregar la terminacion del documento, ejemplo: expresiones.txt) :expresiones2.txt
```
Una vez hecho esto, el programa imprimira en pantalla el siguiente resultado:

```plaintext
Tokens encontrados:
Token: m  Tipo: VARIABLE
Token: =  Tipo: ASIGNACION
Token: 89  Tipo: ENTERO
Token: /  Tipo: DIVISION
Token: (  Tipo: PARENTESIS QUE ABRE
Token: 7.2  Tipo: REAL
Token: +  Tipo: SUMA
Token: n  Tipo: VARIABLE
Token: )  Tipo: PARENTESIS QUE CIERRA
Token: *  Tipo: MULTIPLICACION
Token: 3.1E-4  Tipo: REAL
Token: p  Tipo: VARIABLE
Token: =  Tipo: ASIGNACION
Token: m  Tipo: VARIABLE
Token: ^  Tipo: POTENCIA
Token: n  Tipo: VARIABLE
Token: // Calculo de potencia  Tipo: COMENTARIO
```


##### **Tercer caso de pruebas**
Al tercer caso de pruebas se le asigna el nombre de `expresiones3.txt`, el cual contiene lo siguiente:
```plaintext
c = 45.7 * (-5.8 - d) / 9.8E-3
e = c ^ d // Elevacion a la potencia
```
El python de `automata.py` debe de recibir la entrada del archivo a analizar, en este caso se insetara el nombre del archivo `expresiones3.txt`:

```plaintext
Inserte el nombre del archivo a analizar (tiene que agregar la terminacion del documento, ejemplo: expresiones.txt) :expresiones3.txt
```
Una vez hecho esto, el programa imprimira en pantalla el siguiente resultado:

```plaintext
Tokens encontrados:
Token: c  Tipo: VARIABLE
Token: =  Tipo: ASIGNACION
Token: 45.7  Tipo: REAL
Token: *  Tipo: MULTIPLICACION
Token: (  Tipo: PARENTESIS QUE ABRE
Token: -5.8  Tipo: REAL
Token: -  Tipo: RESTA
Token: d  Tipo: VARIABLE
Token: )  Tipo: PARENTESIS QUE CIERRA
Token: /  Tipo: DIVISION
Token: 9.8E-3  Tipo: REAL
Token: e  Tipo: VARIABLE
Token: =  Tipo: ASIGNACION
Token: c  Tipo: VARIABLE
Token: ^  Tipo: POTENCIA
Token: d  Tipo: VARIABLE
Token: // Elevacion a la potencia  Tipo: COMENTARIO
```


##### **Cuarto caso de pruebas**

Al cuarto caso de pruebas se le asigna el nombre de `expresiones4.txt`, el cual contiene lo siguiente:
```plaintext
g = 12.6 * (3.9 - h) / 4.7E-5
k = g ^ h // Resultado final
```
El python de `automata.py` debe de recibir la entrada del archivo a analizar, en este caso se insetara el nombre del archivo `expresiones4.txt`:

```plaintext
Inserte el nombre del archivo a analizar (tiene que agregar la terminacion del documento, ejemplo: expresiones.txt) :expresiones4.txt
```
Una vez hecho esto, el programa imprimira en pantalla el siguiente resultado:

```plaintext
Tokens encontrados:
Token: g  Tipo: VARIABLE
Token: =  Tipo: ASIGNACION
Token: 12.6  Tipo: REAL
Token: *  Tipo: MULTIPLICACION
Token: (  Tipo: PARENTESIS QUE ABRE
Token: 3.9  Tipo: REAL
Token: -  Tipo: RESTA
Token: h  Tipo: VARIABLE
Token: )  Tipo: PARENTESIS QUE CIERRA
Token: /  Tipo: DIVISION
Token: 4.7E-5  Tipo: REAL
Token: k  Tipo: VARIABLE
Token: =  Tipo: ASIGNACION
Token: g  Tipo: VARIABLE
Token: ^  Tipo: POTENCIA
Token: h  Tipo: VARIABLE
Token: // Resultado final  Tipo: COMENTARIO
```

