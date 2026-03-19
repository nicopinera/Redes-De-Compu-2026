# Trabajo Practico N1

## Nombres

- Nicolas Piñera
- Julian Krede

**Nombre del Grupo**: Puerto1337

## UNC - Facultad de ciencias Exactas, Fisicas y Naturales

## Catedra: Redes de Computadoras

### Profesores

- Henn, Santiago Martin
- Oliva Cuneo, Facundo

**Fecha**: 12/03/2026

---

## Informacion de los autores

- **Información de contacto**:
  - [nicolas.pinera@mi.unc.edu.ar](mailto:nicolas.pinera@mi.unc.edu.ar)
  - [julian.krede@mi.unc.edu.ar](mailto:julian.krede@mi.unc.edu.ar)

---

## Resumen

Este documento detalla la simulación de una infraestructura de red WAN y el estudio de los sistemas de detección de errores en la **capa de enlace**. En la fase inicial, se modeló el intercambio de datos entre redes de área local (LAN), verificando el funcionamiento del protocolo **ARP** y el direccionamiento **hop-by-hop**. Asimismo, se examinó el encapsulamiento de datos, contrastando la naturaleza volátil de las tramas Ethernet respecto a la persistencia de los paquetes IP. Posteriormente, se implementaron métodos de **detección de errores (EDAC)**, tales como **CRC y paridad**, para garantizar la integridad de la información transmitida.

**Palabras clave**: *Ruteo Hop-by-Hop, IP, MAC, Encapsulamiento, EDAC, Checksum, Paridad, LAN.*

---

## Introduccion

---

## Resultado Primera Parte: Repaso general didactico - Simulacion de envio de paquetes, ARP y ruteo entre redes

Para el desarrollo de la actividad, nuestro grupo represento una LAN dentro de la distribucion de roles por equipo. Dentro del equipo, los role e informacion pertinente fue la siguiente:

| Nombre   | Tipo de Dispositivo    | Prefijo de red | Ip          | Ip destino  | MAC      | Payload |
| -------- | ---------------------- | -------------- | ----------- | ----------- | -------- | ------- |
| Julian   | Gateway Predeterminado | 10.14          | 10.14.0.1   |             |          |         |
| Nicolas  | Host                   | 10.14          | 10.14.0.104 | 10.13.0.101 | AD:44:54 | 355b    |
| Franco   | Host                   | 10.14          |             |             |          |         |
| Federico | Host                   |                |             |             |          |         |

- Los host son los aparatos que intentan comunicarse con otro host o end device a traves de la red
- El Gateway Predeterminado es el encargado de redireccionar los paquetes que quieren enviar los host que pertenecen a su red, a los Router intermedios de la WAN

## Resultado Segunda Parte: Inyeccion y deteccion de errores

---

## Conculsiones

---

## Referencias
