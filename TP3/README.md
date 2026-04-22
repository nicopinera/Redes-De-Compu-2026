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

**Fecha**: 12/03/2026

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

---

## Conclusiones

---

## Referencias

- [Switch](https://www.tp-link.com/ar/home-networking/soho-switch/tl-sf1008d/#overview)
