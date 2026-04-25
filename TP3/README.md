# Informe TP3

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

En este trabajo práctico se estudió el funcionamiento de SSH y su aporte a la seguridad en comunicaciones remotas. Se diferenciaron los conceptos de autenticación y cifrado, y se analizó el uso de claves públicas y privadas para el acceso seguro a equipos del laboratorio. Además, se realizaron pruebas de transferencia y captura de tráfico con herramientas como Ncat y Wireshark para comparar escenarios cifrados y no cifrados. Se verificó cómo el uso de protocolos sin cifrado permite observar el contenido de los mensajes en tránsito. Finalmente se realizo un reflexión sobre confidencialidad en redes de computadoras a partir de un video que muestra la explotación de una vulnerabilidad relacionada a este aspecto.

**Palabras clave**: SSH, cifrado, autenticación, claves públicas y privadas, Wireshark, Ncat.

---

## Introducción

La administración remota de sistemas requiere mecanismos que garanticen la confidencialidad y la autenticidad de la información transmitida. En este contexto, SSH se utiliza como estándar para establecer conexiones seguras entre equipos, evitando la exposición de credenciales y datos sensibles.

En el presente informe se describe el marco teórico necesario para comprender la diferencia entre autenticación y cifrado, junto con el rol de la criptografía asimétrica en el esquema de claves de SSH. Luego, se documentan las actividades prácticas realizadas en las máquinas virtuales del laboratorio, incluyendo el análisis de tráfico de red para observar el comportamiento de distintos protocolos.

El objetivo principal fue contrastar comunicaciones protegidas por SSH con transferencias sin cifrado, de modo de evidenciar el impacto real que tiene la seguridad de transporte en la privacidad de los datos.

---

## Resultados

### SSH

**SSH** (Secure Shell) es un protocolo de red que permite acceder y administrar, de forma segura, sistemas remotos mediante una conexión cifrada.

Antes de SSH, se utilizaban protocolos como **Telnet** o **FTP**, que transmitían información (incluidas las contraseñas) en texto plano. Esto generaba riesgos graves de seguridad, ya que los datos podían ser interceptados con facilidad. SSH soluciona este problema mediante:

- **Cifrado de la comunicación**: protege los datos durante la transmisión.
- **Autenticación segura**: mediante contraseñas o claves criptográficas.
- **Integridad de datos**: evita que la información sea modificada en el camino.

### Autenticación vs. cifrado

En la **autenticación**, el objetivo es verificar la identidad de un usuario o de una máquina. Es el proceso de demostrar que una entidad es quien dice ser antes de habilitar el acceso a un sistema. Puede basarse en algo que se sabe (una contraseña), algo que se tiene (una llave física o token) o algo que se es (huella digital o reconocimiento facial).

En cambio, el cifrado tiene como objetivo proteger la **confidencialidad** de los datos. Consiste en transformar un mensaje legible en uno ininteligible para terceros, de manera que, aunque se intercepte durante la transmisión, no pueda interpretarse su contenido. Para ello se emplean algoritmos matemáticos y claves criptográficas.

### Clave pública y privada

Las claves pública y privada conforman un par de llaves digitales vinculadas matemáticamente, pero con funciones opuestas. Este esquema se conoce como criptografía asimétrica.

La **clave pública** puede compartirse sin comprometer la seguridad. Se utiliza para cifrar información o para verificar firmas digitales.

La **clave privada** debe mantenerse en secreto y nunca compartirse. Es la única capaz de descifrar lo cifrado con su clave pública correspondiente y también permite generar firmas digitales válidas.

La clave privada es el elemento central de seguridad en este modelo. Si un tercero la obtiene, puede autenticarse como el usuario legítimo, acceder a servidores vía SSH y firmar mensajes en su nombre. En ese escenario, se comprometen la confidencialidad, la autenticidad y la integridad del sistema.

Las claves SSH presentan varias ventajas frente al uso de contraseñas, principalmente en términos de seguridad y practicidad. A diferencia de las contraseñas, se basan en criptografía asimétrica, lo que las hace mucho más difíciles de vulnerar mediante ataques de fuerza bruta o adivinación. Además, la clave privada nunca se transmite por la red, reduciendo significativamente el riesgo de interceptación. También permiten una autenticación automática sin necesidad de ingresar credenciales manualmente, lo que resulta especialmente útil en procesos automatizados. En conjunto, ofrecen un mecanismo más robusto y confiable para el acceso seguro a sistemas remotos.

### Acceso SSH a máquinas de laboratorio (VM)

Para acceder a la PC3 y la PC4 provistas para el laboratorio, se descargó la clave privada de cada equipo, se ajustaron sus permisos y se verificó el acceso exitoso por SSH, como se observa en la imagen siguiente:

![Imagen Acceso](https://github.com/user-attachments/assets/40c88eb4-5762-4fbe-b35a-67b0e9bc2866)

Se creó una carpeta con el nombre del equipo en ambas máquinas:

![Creación de carpeta](https://github.com/user-attachments/assets/32b3be62-daa4-415d-9cb6-b6037ec52c09)

Luego, se configuró Wireshark para capturar tráfico con destino a la IP de la PC4. En la carga útil de los paquetes capturados no fue posible visualizar contenido legible, lo que evidencia el cifrado de la sesión SSH:

![Tráfico capturado con Wireshark](https://github.com/user-attachments/assets/8d99d618-39cd-4dd1-8ae6-3cfe878645d7)

![Carga del paquete SSH](https://github.com/user-attachments/assets/0d91eae1-e713-48f0-b20d-727ffc15bd70)

El siguiente paso fue instalar Ncat en ambas máquinas virtuales. Esta herramienta permite leer, escribir y redirigir datos a través de la red. En la VM se utilizó el comando **ncat -l puerto**; con el parámetro _-l_, la máquina virtual quedó en modo escucha en el puerto indicado. Luego se estableció una conexión desde la PC local, se mantuvo una conversación de prueba y se capturó el tráfico con Wireshark:

![Conversación entre PC y VM](https://github.com/user-attachments/assets/3ed6dd09-0d85-4f67-a4e0-904c8d1c2e69)

![Tráfico](https://github.com/user-attachments/assets/06fcf64d-4b6e-4780-a0ac-f93aa1551891)

En esta prueba, el contenido del intercambio no resultó legible en la captura.

Al utilizar el parámetro _-u_, Ncat trabaja sobre **UDP** en lugar de **TCP**:

![Envío de datos desde PC](https://github.com/user-attachments/assets/5f34b423-947f-4dc6-b7f0-9d6d910bbea1)

![Wireshark](https://github.com/user-attachments/assets/3fec55be-eaca-4c94-a5c5-778b3d88d87d)

Por último, se conectó la PC3 y se realizó una conversación entre la PC3 y la PC4:

![PC3 - PC4](https://github.com/user-attachments/assets/8ec59474-c53d-4350-a580-8c65c993c175)

En la última actividad, se envió desde la PC local hacia la máquina virtual el archivo **index.html** mediante Ncat y se levantó un servidor HTTP con Python. Al visualizar la página desde la PC local, en Wireshark se pudo observar y leer el contenido del método GET, lo que confirma que HTTP transmite información sin cifrado:

![Envío del archivo index.html](https://github.com/user-attachments/assets/b8d26589-fe80-48bb-84b0-a164e782eb0f)

![Levantamiento de servidor](https://github.com/user-attachments/assets/0e714513-114c-47f5-a105-63b32ca875b8)

![Página](https://github.com/user-attachments/assets/7ab5b29b-d3ad-4cd6-89bc-359060e91934)

![Wireshark](https://github.com/user-attachments/assets/9f0b31fc-9a0e-4456-8056-ade06be4980d)

### Relación entre el video y los trabajos practicos realizados

#### Relación con el TP1:

En el TP1 se analizaron los sistemas de detección de errores (EDAC) como Paridad y CRC (mediante XOR) para garantizar que la información (payload) llegue íntegra y detectar si algún bit fue modificado por ruido o interferencia. 

En el video, los atacantes logran alterar bits específicos del mensaje binario (cambiando un '0' por un '1' para simular que el lector está offline, o cambiando el flag de transacción de "alto valor" a "bajo valor"). El ataque es exitoso porque, en este caso particular (Apple en modo tránsito + Visa), el sistema omite la verificación de la firma criptográfica asimétrica que funcionaría como un control de integridad avanzado (similar a lo que buscaría evitar un mecanismo EDAC robusto), permitiendo que el paquete alterado sea aceptado como válido.

#### Relación con el TP2:
El TP2 se centra en el equipamiento físico, el cableado y el establecimiento de conexiones locales mediante direcciones IP manuales. En el hackeo, el medio físico de transmisión no es un cable Ethernet, sino un campo magnético compartido (NFC).

Al igual que en una red cableada se requiere conexión física, este ataque depende de interceptar el medio físico colocando un dispositivo intermediario (Proxmark) muy cerca del celular de la víctima para capturar las señales emitidas mediante el campo magnético de la capa física.

#### Relación con el TP3:
En el TP3 se utiliza Wireshark para capturar e inspeccionar tráfico de red, demostrando cómo protocolos en texto plano (como HTTP y conexiones TCP/UDP vía Netcat) permiten que cualquiera intercepte y lea el contenido, a diferencia del protocolo SSH que viaja cifrado. 

Esto se aplica directamente al video: los expertos explican que la información intercambiada entre el celular y el lector viaja sin cifrar osea en texto plano por cuestiones de compatibilidad con miles de dispositivos antiguos. Esto es exactamente lo que permite a los atacantes leer la trama de datos con su script de Python (de manera análoga a usar Wireshark) y reescribir los mensajes al vuelo.

### Consideraciones sobre el principio de confidencialidad y los resultados del laboratorio
El principio de confidencialidad establece que la información solo debe ser accesible y legible para las partes autorizadas. Dado lo observado en este laboratorio y en el video, debemos tener en cuenta lo siguiente:

- El peligro de las comunicaciones sin cifrar: Como se demostró al capturar tráfico HTTP con Wireshark en el TP3, cualquier dato enviado sin encriptación es vulnerable a ser interceptado y leído por un tercero en la red. En el video, la falta de cifrado en la comunicación NFC inicial entre el celular y el lector viola la confidencialidad, dándole al atacante la estructura exacta del mensaje para poder manipularlo.

- El laboratorio demuestra que herramientas como SSH resuelven el problema de la confidencialidad mediante el cifrado de los paquetes. Para evitar ataques financieros o robo de datos (como el del video), las arquitecturas de red deben asegurar tanto la autenticación mutua como el cifrado fuerte (criptografía asimétrica) en cada tramo de la comunicación, asegurando que un nodo intermediario ("Hombre en el medio") no pueda descifrar ni alterar el contenido de los paquetes impunemente.

- El tradeoff entre conveniencia y seguridad: Apple introdujo el modo tránsito para que la gente no tenga que desbloquear su teléfono al pagar el metro. Al omitir el desbloqueo (autenticación del usuario) y las comprobaciones de firma en terminales offline por motivos de velocidad de procesamiento, se creó una vulnerabilidad crítica. En el diseño de redes, flexibilizar las capas de seguridad para ganar comodidad suele abrir puertas a vectores de ataque graves.

---

## Conclusiones

Las prácticas realizadas permitieron comprobar, de forma concreta, la importancia de utilizar protocolos seguros para la administración remota y la transferencia de información sensible.

Por un lado, en las sesiones SSH se observó que el tráfico capturado no expone el contenido de los mensajes, lo que valida el aporte del cifrado en términos de confidencialidad. Por otro lado, al trabajar con HTTP, fue posible visualizar el contenido intercambiado, evidenciando los riesgos de emplear protocolos sin protección criptográfica.

Asimismo, se reforzó el rol de la autenticación por claves pública y privada como mecanismo más robusto que el uso exclusivo de contraseñas. En síntesis, el trabajo permitió integrar fundamentos teóricos con evidencia práctica de laboratorio, destacando que la seguridad en redes depende tanto de la elección del protocolo como de una correcta gestión de credenciales.

---

## Referencias

- [Wikipedia: SSH](https://es.wikipedia.org/wiki/Secure_Shell)

[Wikipedia: Criptografía asimétrica](https://es.wikipedia.org/wiki/Criptograf%C3%ADa_asim%C3%A9trica)

- [Pagina de referencia NCat](https://nmap.org/ncat/)

- [Verasitum: Explotación de vulnerabilidad](https://www.youtube.com/watch?v=PPJ6NJkmDAo)