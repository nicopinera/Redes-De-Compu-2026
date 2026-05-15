# Informe TP4

## Nombres

- Nicolás Piñera
- Julián Krede
- Federico Arnaudo
- Franco Perotti

**Nombre del Grupo**: Puerto1337

## UNC - Facultad de Ciencias Exactas, Físicas y Naturales

## Cátedra: Redes de Computadoras

### Profesores

- Henn, Santiago Martín
- Oliva Cúneo, Facundo

**Fecha**: 24/04/2026

---

## Información de los autores

- **Información de contacto**:
  - [nicolas.pinera@mi.unc.edu.ar](mailto:nicolas.pinera@mi.unc.edu.ar)
  - [julian.krede@mi.unc.edu.ar](mailto:julian.krede@mi.unc.edu.ar)
  - [federico.arnaudo@mi.unc.edu.ar](mailto:federico.arnaudo@mi.unc.edu.ar)
  - [franco.perotti@mi.unc.edu.ar](mailto:franco.perotti@mi.unc.edu.ar)

---

## Resumen

**Palabras clave**:

---

## Introducción

---

## Resultados

En la memoria de una computadora, los datos suelen estar organizados mediante punteros y referencias a direcciones de memoria volátiles. Estos datos no pueden enviarse tal cual a través de una red, ya que el receptor no comparte el mismo espacio de memoria.

La **serialización** aplana estas estructuras complejas (objetos, arrays, grafos) en un flujo lineal de bytes (*stream*). La **deserialización** es el proceso inverso, donde el receptor interpreta ese flujo para reconstruir una réplica exacta del objeto original.

Dependiendo de los requisitos de interoperabilidad y rendimiento, existen dos grandes categorías: Serializacion binaria y no binaria.

La diferencia fundamental entre la serialización binaria y la no binaria (basada en texto) radica en cómo se representan los datos para su transporte: los unos y ceros optimizados para la máquina frente a los caracteres legibles para el ser humano.

### Serialización en Formato de Texto o No binaria

La **serialización basada en texto** o no binaria es el proceso de convertir objetos o estructuras de datos complejos en una secuencia de caracteres (string) legible por humanos, facilita la depuración, siendo el estándar en la web moderna.

- **JSON (JavaScript Object Notation)**: El más utilizado por su equilibrio entre ligereza y legibilidad.
- **XML**: Más robusto y con soporte para esquemas complejos, común en entornos corporativos antiguos.
- **YAML**: Muy usado en archivos de configuración.

**Ventajas**:

- **Legibilidad humana**: Se puede abrir el archivo o interceptar el paquete de red y entender qué dice.
- **Interoperabilidad universal**: Prácticamente cualquier lenguaje de programación o sistema operativo puede leer JSON o XML.
- **Facilidad de depuración**: Es muy sencillo encontrar errores en los datos.

**Desventajas**:

- **Tamaño**: Los archivos son mucho más grandes porque incluyen etiquetas, llaves y espacios.
- **Velocidad**: El CPU gasta más ciclos convirtiendo texto a números y viceversa (parsing).

![XML vs JSON](https://github.com/user-attachments/assets/d3b4215a-d0a1-4b51-88e9-5663169e0b54)

![YAML](https://github.com/user-attachments/assets/9394989a-f6b5-4e7d-898c-8966035cbeef)

### Serialización Binaria

La **serialización binaria** es el proceso de convertir objetos complejos de programación en una secuencia lineal de bytes para almacenarlos (en disco/memoria) o transmitirlos por red, permitiendo reconstruirlos de manera idéntica. No es legible por humanos, pero es mucho más eficiente en términos de tamaño de archivo y velocidad de procesamiento.

- **Protocol Buffers (Protobuf)**: Desarrollado por Google, optimiza el ancho de banda al máximo.
- **MessagePack**: Similar a JSON pero en formato binario.
- **Apache Avro**: Común en sistemas de Big Data como Hadoop.
- **Formatos Nativos**: Como Pickle en Python o Serializable en Java, aunque limitan la comunicación a sistemas que usen el mismo lenguaje.

**Ventajas**:

- Eficiencia extrema: Los paquetes de datos son significativamente más pequeños (ahorro de ancho de banda).
- Alto rendimiento: La máquina procesa los datos binarios casi de forma nativa, lo que reduce la latencia.
- Tipado fuerte: Suelen requerir un "contrato" o esquema previo, lo que evita errores de datos corruptos.

**Desventajas**:

- Ilegibilidad: Si abres un archivo binario, verás símbolos extraños. Necesitas herramientas especiales para leerlo.
- Acoplamiento: A veces, tanto el emisor como el receptor necesitan conocer el esquema exacto de antemano para poder interpretar los bytes.

---

## Conclusiones

---

## Referencias
