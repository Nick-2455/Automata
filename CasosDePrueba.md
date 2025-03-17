### **Caso de prueba base**

El caso de prueba base es aquel que es dado en el ejemplo de la plataforma, al cual se le asigna el nombre de 'expresiones.txt', el cual contiene lo siguiente:
```plaintext
b=7
a = 32.4 *(-8.6 - b)/ 6.1E-8
d = a ^ b // Esto es un comentario
```
El python de 'automata.py' debe de recibir la entrada del archivo a analizar, en este caso se insetara el nombre del archivo 'expresiones.txt':

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

### **Primer Caso de pruebas**

Al primer caso de pruebas se le asigna el nombre de 'expresiones1.txt', el cual contiene lo siguiente:
```plaintext
x = 15.2 * (4.3 - y) / 2.5E-6
z = x ^ y // Operacion exponencial
```
El python de 'automata.py' debe de recibir la entrada del archivo a analizar, en este caso se insetara el nombre del archivo 'expresiones1.txt':

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


### **Segundo caso de pruebas**

Al segundo caso de pruebas se le asigna el nombre de 'expresiones2.txt', el cual contiene lo siguiente:
```plaintext
m = 89 / (7.2 + n) * 3.1E-4
p = m ^ n // Calculo de potencia
```
El python de 'automata.py' debe de recibir la entrada del archivo a analizar, en este caso se insetara el nombre del archivo 'expresiones2.txt':

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


### **Tercer caso de pruebas**
Al tercer caso de pruebas se le asigna el nombre de 'expresiones3.txt', el cual contiene lo siguiente:
```plaintext
c = 45.7 * (-5.8 - d) / 9.8E-3
e = c ^ d // Elevacion a la potencia
```
El python de 'automata.py' debe de recibir la entrada del archivo a analizar, en este caso se insetara el nombre del archivo 'expresiones3.txt':

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


### **Cuarto caso de pruebas**

Al cuarto caso de pruebas se le asigna el nombre de 'expresiones4.txt', el cual contiene lo siguiente:
```plaintext
g = 12.6 * (3.9 - h) / 4.7E-5
k = g ^ h // Resultado final
```
El python de 'automata.py' debe de recibir la entrada del archivo a analizar, en este caso se insetara el nombre del archivo 'expresiones4.txt':

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
