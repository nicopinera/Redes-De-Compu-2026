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

**Palabras clave**: SSH, Cifrado, autenticacion.

---

## Introducción

---

## Resultado

### SSH

**SSH** (Secure Shell) es un protocolo de red que permite acceder y administrar de forma segura sistemas remotos a través de una conexión cifrada.

Antes de SSH, se usaban protocolos como **Telnet** o **FTP** que transmitían información (incluyendo contraseñas) en texto plano. Esto generaba riesgos graves de seguridad, ya que los datos podían ser interceptados fácilmente.SSH soluciona este problema mediante:

- **Cifrado de la comunicación**: protege los datos durante la transmisión.
- **Autenticación segura**: mediante contraseñas o claves criptográficas.
- **Integridad de datos**: evita que la información sea modificada en el camino.

### Autenticacion vs Cifrado

En la **autenticacion** el objetivo es verificar la identidad de un usuario o de una máquina. Es el proceso de demostrar que eres realmente quien dices ser antes de que se te permita entrar a un sistema. Funciona mediante algo que _sabes_ (una contraseña), algo que _tienes_ (una llave física o token) o algo que _eres_ (huella digital o rostro).

En cambio, el cifrado tiene como objetivo proteger la **confidencialidad** de los datos. Consiste en transformar un mensaje legible en un código ininteligible para que, si alguien lo intercepta en el camino, no pueda entender nada. Utiliza algoritmos matemáticos y una "llave" para desordenar la información al enviarla y reordenarla al recibirla.

### Clave publica y privada

Las claves pública y privada son un par de llaves digitales que están vinculadas matemáticamente entre sí, pero que cumplen funciones opuestas. Este sistema se conoce como criptografía asimétrica.

La **Clave Pública** es la llave que puedes compartir con todo el mundo sin ningún riesgo. Sirve para "cerrar" (cifrar) la información o para que otros identifiquen tu "cerradura". No compromete la seguridad si otros la conocen.

La **Clave Privada** es la llave que debes guardar en secreto y nunca compartir con nadie. Eta clave es la única capaz de "abrir" (descifrar) lo que se cerró con su clave pública correspondiente. También sirve para poner tu "firma digital" y demostrar que un mensaje realmente vino de ti.

La clave privada no debe compartirse porque es el elemento que garantiza la seguridad y la identidad en un sistema criptográfico. Si alguien obtiene tu clave privada, puede leer todos los datos que fueron cifrados para vos. Pueden autenticarse como si fuera vos (por ejemplo, acceder a servidores vía SSH). Pueden generar firmas digitales válidas, haciendo pasar mensajes falsos como legítimos. Compartir la clave privada equivale a entregar acceso total: se pierde la confidencialidad, la autenticidad y la integridad del sistema.

Las claves SSH presentan varias ventajas frente al uso de contraseñas, principalmente en términos de seguridad y practicidad. A diferencia de las contraseñas, se basan en criptografía asimétrica, lo que las hace mucho más difíciles de vulnerar mediante ataques de fuerza bruta o adivinación. Además, la clave privada nunca se transmite por la red, reduciendo significativamente el riesgo de interceptación. También permiten una autenticación automática sin necesidad de ingresar credenciales manualmente, lo que resulta especialmente útil en procesos automatizados. En conjunto, ofrecen un mecanismo más robusto y confiable para el acceso seguro a sistemas remotos.

### Acceso SSH a maquinas de laboratorio (VM)

Para poder acceder a la PC3 y PC4 que se nos brindaron para realizar el laboratorio, tuvimos que descargar la clave privada de ambas PC, cambiarle los permisos y pudimos acceder correctamente como se ve en la imagen a continuacion:

![Imagen Acceso](https://github.com/user-attachments/assets/40c88eb4-5762-4fbe-b35a-67b0e9bc2866)

Se crea la carpeta con el nombre de equipo en ambas PC

![Creacion de Carpeta](https://github.com/user-attachments/assets/32b3be62-daa4-415d-9cb6-b6037ec52c09)

Se configuro wireshark para capturar el trafico con destino a la IP de la PC4 y vemos que en la carga no se puede acceder al contenido del paquete capturado:

![Trafico Capturado con wireshark](https://github.com/user-attachments/assets/8d99d618-39cd-4dd1-8ae6-3cfe878645d7)

![Carga del paquete SSH](https://github.com/user-attachments/assets/0d91eae1-e713-48f0-b20d-727ffc15bd70)

El siguiente paso fue instalar netcat en ambas paquina virtuales, esta herramienta sirve para leer, escribir y redirigir datos a traves de una red. En la VM utilizamos el comando **ncat -l puerto**, con el flag _-l_ convertimos a la maquina virtual en un servidor que esta escuchando en el puerto que le indicamos, luego nos contectamos con nuestra PC y realizamos una conversacion, ademas capturamos trafico de esta conversacion con wireshark:

![Conversacion entre PC y VM](https://github.com/user-attachments/assets/3ed6dd09-0d85-4f67-a4e0-904c8d1c2e69)

![Trafico](https://github.com/user-attachments/assets/06fcf64d-4b6e-4780-a0ac-f93aa1551891)

Lo que podemos ver es que no se puede descifrar el contenido.

Ahora si utilizamos el flag _-u_ utilizamos el protocolo **UTP** en vez de **TCP**

![Envio datos desde PC](https://github.com/user-attachments/assets/5f34b423-947f-4dc6-b7f0-9d6d910bbea1)

![Wireshark](https://github.com/user-attachments/assets/3fec55be-eaca-4c94-a5c5-778b3d88d87d)

Por ultimo no conectamos PC3 y realizamo una conversacion entre la PC3 y PC4

![PC3 - PC4](https://github.com/user-attachments/assets/8ec59474-c53d-4350-a580-8c65c993c175)

Para la ultima actividad, nos enviamos con la herramienta ncat desde nuestra PC hacia la maquina virtual el archivo **index.html** y levantamos un servidor http con python, lo visualizamos desde nuestra PC y vemos que en whireshark podemos descifrar el contenido que obtenemos con el metodo GET:

![Envio archivo index.html](https://github.com/user-attachments/assets/b8d26589-fe80-48bb-84b0-a164e782eb0f)

![Levantamo servidor](https://github.com/user-attachments/assets/0e714513-114c-47f5-a105-63b32ca875b8)

![Pagina](https://github.com/user-attachments/assets/7ab5b29b-d3ad-4cd6-89bc-359060e91934)

![Wireshark](https://github.com/user-attachments/assets/9f0b31fc-9a0e-4456-8056-ade06be4980d)

---

## Conclusiones

---

## Referencias
