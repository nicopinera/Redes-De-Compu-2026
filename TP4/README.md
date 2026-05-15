# Informe TP4

## Integrantes

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

El presente informe detalla el estudio y la implementación de técnicas fundamentales para la comunicación en sistemas distribuidos. Se abordan los conceptos de serialización binaria y no binaria (JSON, XML), destacando sus ventajas y los compromisos existentes entre legibilidad y rendimiento. Asimismo, se describe la implementación de un servidor TCP contenedorizado mediante Docker y la integración de seguridad a través de cifrado simétrico utilizando el estándar Fernet (AES). Los resultados demuestran la importancia de la estructuración de datos y la protección de la integridad de los mensajes en redes modernas.

**Palabras clave**: Serialización, JSON, Docker, TCP, Cifrado Simétrico, AES, Fernet.

---

## Introducción

En el ámbito de las redes de computadoras, el intercambio de información requiere mecanismos que garanticen que los datos estructurados en memoria puedan ser transmitidos y reconstruidos fielmente por distintos nodos. Este proceso, conocido como **serialización**, es el pilar de la interoperabilidad en la web y los sistemas distribuidos contemporáneos. Este trabajo práctico explora estas dimensiones mediante el desarrollo de un servidor TCP en Python, su despliegue en un entorno aislado con Docker y la aplicación de algoritmos de cifrado simétrico para asegurar la confidencialidad e integridad de la comunicación.

---

## Resultados

En la memoria de una computadora, los datos suelen estar organizados mediante punteros y referencias a direcciones de memoria volátiles. Estos datos no pueden enviarse tal cual a través de una red, ya que el receptor no comparte el mismo espacio de direccionamiento.

La **serialización** consiste en "aplanar" estas estructuras complejas (objetos, arreglos, grafos) en un flujo lineal de bytes (_stream_). La **deserialización** es el proceso inverso, donde el receptor interpreta ese flujo para reconstruir una réplica exacta del objeto original.

Dependiendo de los requisitos de interoperabilidad y rendimiento, existen dos grandes categorías: la serialización binaria y la no binaria. La diferencia fundamental entre ambas radica en la representación de los datos para su transporte: bits optimizados para la máquina frente a caracteres legibles para el ser humano.

### Serialización en Formato de Texto (No binaria)

La **serialización basada en texto** es el proceso de convertir estructuras de datos en una secuencia de caracteres legible por humanos. Esto facilita enormemente la depuración y se ha consolidado como el estándar en la web moderna.

- **JSON (JavaScript Object Notation)**: El más utilizado por su equilibrio entre ligereza y legibilidad.
- **XML**: Robusto y con soporte para esquemas complejos, común en entornos corporativos.
- **YAML**: Ampliamente adoptado en archivos de configuración por su claridad visual.

**Ventajas**:

- **Legibilidad humana**: Permite inspeccionar el contenido directamente en archivos o interceptando paquetes de red.
- **Interoperabilidad universal**: Soportado por prácticamente cualquier lenguaje de programación.
- **Facilidad de depuración**: Identificar errores en la estructura de los datos es directo.

**Desventajas**:

- **Tamaño**: Los archivos son más voluminosos debido a la inclusión de etiquetas, llaves y espacios en blanco.
- **Velocidad**: El CPU consume más ciclos en el procesamiento (parsing) para convertir texto a tipos de datos nativos.

![XML vs JSON](https://github.com/user-attachments/assets/d3b4215a-d0a1-4b51-88e9-5663169e0b54)

![YAML](https://github.com/user-attachments/assets/9394989a-f6b5-4e7d-898c-8966035cbeef)

### Serialización Binaria

La **serialización binaria** convierte objetos en una secuencia lineal de bytes optimizada para el almacenamiento o la transmisión. Aunque no es legible para humanos, es significativamente más eficiente en términos de tamaño y velocidad de procesamiento.

- **Protocol Buffers (Protobuf)**: Desarrollado por Google para optimizar al máximo el ancho de banda.
- **MessagePack**: Una alternativa binaria similar a JSON en su estructura.
- **Apache Avro**: Estándar en ecosistemas de Big Data como Hadoop.
- **Formatos Nativos**: Como `Pickle` en Python, aunque limitan la comunicación a sistemas que utilicen el mismo lenguaje.

**Ventajas**:

- **Eficiencia extrema**: Los paquetes son compactos, ahorrando ancho de banda.
- **Alto rendimiento**: El procesamiento es casi nativo, lo que reduce la latencia.
- **Tipado fuerte**: A menudo requieren un esquema previo, lo que previene la corrupción de datos.

**Desventajas**:

- **Ilegibilidad**: La inspección directa de los datos requiere herramientas especializadas.
- **Acoplamiento**: El emisor y el receptor deben compartir el esquema exacto de antemano.

## Servidor TCP

Para el despliegue del servidor TCP, se creó una imagen de Docker que contiene el script del servidor configurado para escuchar en el puerto 5000. El archivo de configuración se encuentra en [Dockerfile](/script/Dockerfile). La gestión del entorno se realiza mediante el `Makefile` con los siguientes comandos:

```bash
# Entramos a la carpeta que contiene el Makefile
cd script

# Construimos la imagen a partir de nuestro Dockerfile
make build

# Ejecutamos el contenedor mapeando el puerto 5000
make run

# Revisamos los logs para observar la interacción
make logs

# Limpieza del entorno (detener y eliminar)
make clean
```

Se generó el siguiente JSON con la información para las pruebas iniciales:

```json
{
  "nombre_grupo": "Puerto 1337",
  "payload": "Hola servidor"
}
```

### Pruebas de Comunicación

En primera instancia, se validó el funcionamiento enviando paquetes a un servidor local, verificando la correcta recepción de los datos:

![Packet Sender Local](https://github.com/user-attachments/assets/b47defea-f064-4638-bf83-77e45aea3174)
![Packet Sender Local 2](https://github.com/user-attachments/assets/546f92f4-6af0-4578-a4b3-06894ff9312c)
![Recepcion Local](https://github.com/user-attachments/assets/80f8d20f-810a-46bd-91a4-f404526cbcb7)

Posteriormente, se replicó la prueba dirigiendo los mensajes al contenedor Docker:

![Recepcion Docker](https://github.com/user-attachments/assets/f99055e0-dfba-41f4-9f3e-6067189222d0)

Finalmente, se ajustó el script del cliente para automatizar el envío de mensajes estructurados:

![Cliente](https://github.com/user-attachments/assets/06fa780b-abf5-4d93-abbf-bd8e62c2015a)

## Cifrado Simétrico

El concepto central del **cifrado simétrico** es la utilización de una única clave matemática tanto para cifrar como para descifrar la información.

- **Ventaja**: Alta velocidad y bajo consumo de recursos, ideal para grandes volúmenes de datos en tiempo real.
- **Desventaja**: El problema de la distribución de la clave; si un tercero intercepta la clave durante el intercambio, la seguridad se ve comprometida.

### Implementación con Fernet

**Fernet** es un estándar criptográfico que utiliza la librería `cryptography`. Implementa una clave de 32 bytes que se divide internamente en:

- **Clave de Cifrado**: Para enmascarar los datos.
- **Clave de Firma (HMAC)**: Para verificar la integridad y autenticidad del mensaje.

Un mensaje cifrado con Fernet incluye:

1. **Versión (1 byte)**.
2. **Timestamp (8 bytes)**: Permite rechazar mensajes antiguos para prevenir ataques de replicación.
3. **IV (Vector de Inicialización)**: Bloque aleatorio de 16 bytes.
4. **Texto Cifrado**: El contenido protegido mediante **AES-128-CBC**.
5. **HMAC (32 bytes)**: Firma digital calculada con SHA256.

### Estándar AES (Advanced Encryption Standard)

AES es el algoritmo de cifrado simétrico más seguro y utilizado actualmente. Es un **cifrado por bloques** que divide la información en segmentos de 128 bits y aplica transformaciones matemáticas complejas (sustitución, rotación y mezcla).

**Características Principales:**

- **Seguridad Robusta**: Resistente ante ataques de criptoanálisis conocidos.
- **Eficiencia**: Optimizado para implementaciones tanto en software como en hardware.
- **Resiliencia**: Diseñado para ser el estándar de protección en comunicaciones críticas.

A continuación, se observa la implementación del cifrado y el descifrado en el servidor:

![Mensaje Encriptado](https://github.com/user-attachments/assets/cf6bc771-1556-413c-9fea-ead83314f776)
![Mensaje Descifrado](https://github.com/user-attachments/assets/cede7e57-98a5-471a-9639-9001bfcd3b21)

---

## Conclusiones

A través del desarrollo de este trabajo práctico, se ha evidenciado que la elección del formato de serialización impacta directamente en el consumo de recursos y la facilidad de mantenimiento de un sistema. Mientras que JSON ofrece una gran flexibilidad y legibilidad, los formatos binarios resultan indispensables en escenarios de alta performance y restricciones de ancho de banda. Finalmente, la integración del cifrado simétrico mediante Fernet subraya que la seguridad no debe ser una idea de último momento; la combinación de AES para la confidencialidad y HMAC para la integridad constituye una solución robusta para proteger la comunicación en entornos potencialmente inseguros. En conjunto, estas tecnologías forman la base técnica para construir aplicaciones de red modernas, escalables y seguras.

---

## Referencias
