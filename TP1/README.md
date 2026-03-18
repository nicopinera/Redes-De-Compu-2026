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
  - [federico.arnaudo@mi.unc.edu.ar](mailto:federico.arnaudo@mi.unc.edu.ar)

---

## Resumen

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
| Federico | Host                   | 10.14          | 10.14.0.102 | 10.7.0.102  | AC:40:87 | 91C2    |

- Los host son los dispositivos que intentan comunicarse con otro host o end device a traves de la red
- El Gateway Predeterminado es el encargado de redireccionar los paquetes que quieren enviar los host que pertenecen a su red, a los Router intermedios de la WAN

Una vez establecidos los roles de los equipos y de cada integrantes del grupo. Se lleno un la tarjeta identificadora, que representa nuestra NIC.

Para que el router descubra la direccion MAC del Router intermedio vecino, se la debe preguntar.

## Resultado Segunda Parte: Inyeccion y deteccion de errores

EDAC: Deteccion de errores y correccion

- CRC: Bit de paridad y XOR
- Checksum

A nuestro grupo nos toco enviar paquetes con el algoritmo de Paridar y recibir paquetes con codigo generado con el algoritmo XOR

Son algoritmos que agregan metadata al paquete, para corroborar si hay errores al momento de recibir los datos

Enviamos paquetes con una carga y un codigo de EDAC. Al recibir un frame, debemos verificar el codigo de EDAC para detectar errores.

Las tramas tienen la siguiente informacion:

- IP de origen: *10.14.0.1*
- IP de destino:
- Payload: D23Ch *1101-0010-0011-1100*b
- EDAC: Por paridad el codigo de EDAC es *0*

En el reporte de recepcion, registramos lo siguiente:
- Ip de origen: 10.1.11
- Payload recibida: *F501*
- EDAC para la payload recibida: *1011* o *B*
- EDAC: *F* o *1111*
- Algoritmo utilizado para calcular el codigo de EDAC fue el CRC calculado por *XOR*
- La payload esta integra: La payload *no* esta integra
- Potenciales payload:
  - Modificando un bit: B501 - F101 - F541 - F505
  - Modificando dos bits: B541 - F105 - B505
  - Modificando tres bits: F145 - B545

---

## Conculsiones

---

## Referencias
