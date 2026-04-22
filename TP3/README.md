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

---

## Conclusiones

---

## Referencias

- [Switch](https://www.tp-link.com/ar/home-networking/soho-switch/tl-sf1008d/#overview)
