# Trabajo Práctico N2

## Nombres

- Nicolas Piñera
- Julian Krede
- Federico Arnaudo
- Franco Perotti

**Nombre del Grupo**: Puerto1337

## UNC - Facultad de Ciencias Exactas, Físicas y Naturales

## Cátedra: Redes de Computadoras

### Profesores

- Henn, Santiago Martin
- Oliva Cuneo, Facundo

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

**Palabras clave**:

---

## Introducción

---

## Resultado Parte 1 - Armado y verificacion de cables Cat5/Cat5e bajo estandar T568A/B

En esta seccion del trabajo practico se investigo el proceso de armado de un cable CAT5 con ficha RJ45. Para realizar esto, se siguen los siguientes pasos:

1. **Pelar el cable** quitando de funda una longitud equivalente a una ficha y media.
2. **Desenredar y estirar** los cables trenzados y dejarlos lo mas recto posible. Si las puntas son irregulares, emparejar cortando para dejar las puntas lo mas rectas posibles
3. **Ordenar los cables segun la norma** para esto, se utilizo la imagen que se muestra al finalizar los pasos. Se utilizo **T568B**
4. **Insertar el conector**, viendo que los cables se mantengan en orden.
5. **Crimpar** con la herramienta suministrada por el docente.

![Orden de los cables](https://github.com/user-attachments/assets/e7a0d162-1815-443a-9ab5-19ee07664235)

**Imagen cable grupo**:

![Testeo cable](https://github.com/user-attachments/assets/d2bd41ee-87fe-411c-9ba9-fe4f29435f75)

La norma T568 es el estándar internacional que regula el diseño e instalación de sistemas de cableado de telecomunicaciones en edificios comerciales. Su objetivo es asegurar la interoperabilidad entre diferentes fabricantes y equipos. Dentro de esta norma, existen dos esquemas de terminación para conectores RJ45 que definen el orden de los 8 hilos de cobre: T568A y T568B.

- **T568A**: Se utiliza frecuentemente en instalaciones gubernamentales y residenciales antiguas.
- **T568B**: Es el estándar más utilizado en redes comerciales y empresariales modernas, ya que coincide con la mayoría de los equipos de red de los fabricantes.

La única diferencia física es que se intercambian las posiciones de los pares Naranja y Verde. El rendimiento de transmisión es idéntico en ambas

La forma en que se combinan estas normas en cada extremo determina su funcion:

- **Cable derecho**: se contruye utilizando la misma norma en ambos extremos (A-A o B-B). Su funcion es conectar dispositivos diferentes como un Switch a una PC o desde un Router a un Switch.
- **Cable cruzado**: Se construye utilizando normas distintas en cada extremo (una punta T568A y la otra T568B). Esto cruza físicamente los pines de transmisión (Tx) con los de recepción (Rx). Se utiliza para conectar dispositivos identicos. Por ejemplo PC a PC

En la actualidad, la mayoría de los equipos modernos cuentan con una función llamada **Auto MDI-X**. Esta tecnología detecta automáticamente el tipo de cable y cruza las señales electrónicamente si es necesario, lo que ha hecho que el uso de cables derechos sea suficiente para casi cualquier conexión.

Nuestro grupo construyo un total de 3 cables de diferentes largos. Una vez que los verificamos visualmente y con el tester de cable ethernet, intercambiamos cables con el grupo **subnet surfers**, realizamos una inspeccion visual y lo testeamos con el tester. A continuacion se muestra el cable recibido del grupo:

## Resultado Parte 2 - Equipamiento fiscio, verificacion y utilizacion de equipos de red y analisis de trafico

Para esta seccion utilizamos un Switch **TP-Link TL-SF1008d de 8 puertos**, el cual posee las siguientes caracteristicas:

- Interface: 8 Puertos 10/100Mbps, negociación automática, Auto-MDI/MDIX
- Tasas de transferencia de datos: 10/100Mbps en Half Duplex, 20/200Mbps en Full Duplex
- Estándares y Protocolos: IEEE 802.3, IEEE 802.3u, IEEE 802.3x, CSMA/CD
- La tecnología Green Ethernet ahora energía hasta del 60%
- El control de flujo de IEEE 802.3x proporciona una transferencia de datos confiable
- Plug and play (conecte y use), no se requiere configuración

![Switch](https://github.com/user-attachments/assets/4abb5ff0-cbc4-4a5e-b1f6-86bd35ddcb2d)

> [!NOTE]
> Como para varios grupos fue complicado entrar a la configuracion del switch, se utilizo este Plug and Play. Las configuraciones que se detallan a continuacion fueron las necesarias para poder realizar ping entre 2 computadoras conectadas

---

## Conclusiones

---

## Referencias

- [Switch](https://www.tp-link.com/ar/home-networking/soho-switch/tl-sf1008d/#overview)
