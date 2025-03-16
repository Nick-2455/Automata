### **1. Descripción del programa**

Este programa está diseñado para tokenizar expresiones matemáticas y de programación, identificando y clasificando los diferentes componentes como números enteros, números reales, variables, operadores, paréntesis, y comentarios. El programa está escrito en **Python** y utiliza expresiones regulares para identificar los distintos tipos de tokens en el código de entrada.
![image](https://github.com/user-attachments/assets/16703efa-bc81-4734-941a-3992343a4ea0)

### **2. Lenguaje de programación utilizado**

Este programa está desarrollado en el lenguaje de **Python**.

### **3. Requisitos previos**

Antes de ejecutar el programa, debe tener instalada la versión de Python 3 en su sistema. Puede descargar e instalar Python desde el siguiente enlace oficial:  
[Python Oficial](https://www.python.org/downloads/)

Además, el programa utiliza la biblioteca estándar de Python `re` (expresiones regulares) y `collections` (para el uso de `namedtuple`). Estas bibliotecas están incluidas por defecto en Python, por lo que no necesita instalar nada adicional.

Si el sistema muestra una versión de Python 3, está listo para ejecutar el programa.

### **4. Archivos necesarios**

- **Archivo de código fuente:** `automata.py` (Este es el archivo que contiene el programa en Python).
- **Archivo de entrada:** `expresiones.txt` (Este archivo contiene el código o las expresiones a analizar).

### **5. Cómo ejecutar el programa**

Para ejecutar el programa, siga estos pasos:

1. Asegúrese de tener el archivo `expresiones.txt` con el contenido que desea tokenizar.
2. Asegúrese de que el archivo `automata.py` y `expresiones.txt` esten en la misma carpeta.
3. Abra una terminal o línea de comandos en esa carpeta.
4. Ejecute el siguiente comando para correr el programa:

```bash
python tokenizador.py
```

### **6. Qué esperar como salida**

Cuando ejecute el programa, el script leerá el archivo `expresiones.txt`, procesará su contenido y generará una lista de tokens encontrados. Los tokens se mostrarán en la terminal o línea de comandos, con su valor y tipo. 

#### Ejemplo de salida:
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

### **7. Descripción del autómata**

El autómata para este problema es un autómata de tipo **determinista** que recorre el código de entrada de izquierda a derecha, reconociendo patrones específicos definidos por las expresiones regulares.

#### Diagrama del autómata:

(aqui va la imgaen del diagrama) 

1. El autómata comienza en un estado inicial.
2. Luego, lee el siguiente símbolo de la entrada.
3. Según el símbolo leído, el autómata hace una transición a un estado correspondiente:
   - Si el símbolo es un número (ya sea entero o real), se transita al estado que valida los números.
   - Si el símbolo es una letra o un guion bajo, se transita a un estado que valida las variables.
   - Si el símbolo es un operador o un paréntesis, el autómata lo clasifica directamente como un token.
4. Si encuentra un comentario (indicador `//`), el autómata transita a un estado donde consume todo el comentario.
5. Si el autómata no puede reconocer un símbolo, genera un error indicando que el token no es reconocido.

El autómata sigue estas reglas hasta que toda la entrada ha sido procesada, y luego devuelve todos los tokens identificados.



### **8. Conclusion**

Este programa le permitirá tokenizar expresiones matemáticas o de programación de manera eficiente y ordenada. A través de su ejecución, podrá descomponer el código de entrada en sus componentes básicos (tokens), lo que es útil para el análisis de expresiones en un lenguaje específico.
