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

**Palabras clave**: _Ruteo Hop-by-Hop, IP, MAC, Encapsulamiento, EDAC, Checksum, Paridad, LAN._

---

## Introduccion

---

## Resultado Primera Parte: Repaso general didactico. Simulacion de envio de paquetes, ARP y ruteo entre redes

Para empezar esta actividad el aula se convirtio en una red heterogenea. Para ello, los diferentes grupos fueron adoptando roles: Algunos representaran una LAN (Red de area local) y otros tomaran el rol de Routers Intermedios.

Dentro de las LAN uno de los integrantes del grupo toma el rol de Gateway predeterminado de los otros 3 host que forman la LAN. El Gateway predeterminado se encarga de ser la puerta de salida de los paquetes que desean enviar los host fuera de la LAN. Por otro lado los Routers intermedios se encargan de reenviar los paquetes a los gateway predeterminados correspondiente a la LAN de destino. A continuacion se presenta un diagrama de la distribucion, se puede ver claramente que cada LAN representa una **topologia estrella** donde todos los host se conectan a su gateway predeterminado.

![Diagrama de Red](https://github.com/user-attachments/assets/5a4898bb-138c-47f1-b6aa-8adc413afd83)

Una vez entendida la distribucion de roles por grupo, nos toco definir dentro de la red LAN, los roles de cada integrante. Los host tienen un **prefijo de red**, una **IP de host**, **IP de host de destino**, direccion fisica o **MAC** y una carga o **Payload** que deberian enviar en binario. Ademas se establecio un TTL (Time to Live) de 6, para los paquetes. Este valor se decrementa cada vez que el paquete realiza un salto entre dispositivos, si el parametro llega a _0_ el paquete se _descarta_. Con estos datos se completaron la **NIC** de cada integrante. A continuacion se presenta una tabla con los datos y roles asignados a cada integrante.

| Nombre   | Tipo de Dispositivo    | Prefijo de red | Ip          | Ip destino  | MAC      | Payload | TTL |
| -------- | ---------------------- | -------------- | ----------- | ----------- | -------- | ------- | --- |
| Julian   | Gateway Predeterminado | 10.14          | 10.14.0.1   |             |          |         | x   |
| Nicolas  | Host                   | 10.14          | 10.14.0.104 | 10.13.0.101 | AD:44:54 | 355b    | 6   |
| Franco   | Host                   | 10.14          |             |             |          |         | 6   |
| Federico | Host                   |                |             |             |          |         | 6   |

Para realizar el envio de un paquete desde un host a otro ubicado en diferentes LAN se debia seguir los siguientes pasos:

- El host debe consultar al Gateway Predeterminado su direccion MAC. Una vez entregada, el host agrega esta direccion a la cabecera del paquete a enviar.
- El Gateway predeterminado debe armar una tabla en la cual registra las direcciones IP de la red local junto con su direccion MAC.
- Una vez que el gateway recibio el paquete, le consulta al router intermedio su direccion MAC. Una vez conodica, en el paquete original, elimina la direccion MAC del primer host, como direccion MAC de origen coloca la propia (Gateway) y como direccion de origen coloca la del router intermedio. En todo este proceso, el gateway nunca modifica las direcciones IP de origen o destino.
- El router intermedio forma una tabla con informacion de cada router intermedio y las redes que estan a su alcance, para saber a quien reenviar ese paquete.
- Por otro lado, el proceso de preguntar la direccion MAC al proximo dispositivo y completar esta informacion en el paquete sigue hasta que el mimo llegue a destino.

El proceso en el cual un dispositivo consulta a otro su direccion MAC se llama **Protocolo de Resolucion de direcciones (ARP)**, el mismo es un protocolo de la capa de enlace de datos, que se encarga de vincular una direccion de red (IP) con una direccion fisica (MAC).

El mismo consta de una consulta realizada por el dispositivo que intenta enviar el paquete a todos los dispositivos que tiene acceso, realizando una **ARP Request** por **broadcast (difucion)** a todos los dispositivos de la Red. Al dispositivo que le corresponda la direccion IP o tenga acceso a esa red, contestara con su direccion MAC.

> [!NOTE]
> A nuestro grupo no nos llego ningun paquete en esta actividad

## Resultado Segunda Parte: Inyeccion y deteccion de errores

---

## Conculsiones

---

## Referencias
