# Trabajo Práctico Nº 2

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

**Palabras clave**:

---

## Introducción

---

## Resultado Parte 1 - Armado y verificación de cables Cat5/Cat5e bajo estándar T568A/B

En esta sección del trabajo práctico se investigó el proceso de armado de un cable CAT5 con ficha RJ45. Para realizar esto, se siguieron los siguientes pasos:

1. **Pelar el cable**: quitar la funda en una longitud equivalente a una ficha y media.
2. **Desenredar y estirar** los cables trenzados, dejándolos lo más rectos posible. Si las puntas son irregulares, emparejarlas cortando para que queden lo más niveladas posible.
3. **Ordenar los cables según la norma**: para esto, se utilizó la imagen que se muestra al finalizar los pasos. Se utilizó la norma **T568B**.
4. **Insertar el conector**, verificando que los cables se mantengan en orden.
5. **Crimpar** con la herramienta suministrada por el docente.

<div align="center">

![Orden de los cables](https://github.com/user-attachments/assets/e7a0d162-1815-443a-9ab5-19ee07664235)

![Cables propios](https://github.com/user-attachments/assets/47cb674e-e213-423a-a1a3-8cef2ff385e3)

![Testeo cable](https://github.com/user-attachments/assets/d2bd41ee-87fe-411c-9ba9-fe4f29435f75)

</div>

La norma T568 es el estándar internacional que regula el diseño e instalación de sistemas de cableado de telecomunicaciones en edificios comerciales. Su objetivo es asegurar la interoperabilidad entre diferentes fabricantes y equipos. Dentro de esta norma, existen dos esquemas de terminación para conectores RJ45 que definen el orden de los 8 hilos de cobre: T568A y T568B.

- **T568A**: Se utiliza frecuentemente en instalaciones gubernamentales y residenciales antiguas.
- **T568B**: Es el estándar más utilizado en redes comerciales y empresariales modernas, ya que coincide con la mayoría de los equipos de red de los fabricantes.

La única diferencia física es que se intercambian las posiciones de los pares naranja y verde. El rendimiento de transmisión es idéntico en ambas.

La forma en que se combinan estas normas en cada extremo determina su función:

- **Cable directo**: Se construye utilizando la misma norma en ambos extremos (A-A o B-B). Su función es conectar dispositivos diferentes, como un Switch a una PC o desde un Router a un Switch.
- **Cable cruzado**: Se construye utilizando normas distintas en cada extremo (una punta T568A y la otra T568B). Esto cruza físicamente los pines de transmisión (Tx) con los de recepción (Rx). Se utiliza para conectar dispositivos idénticos, por ejemplo, de PC a PC.

En la actualidad, la mayoría de los equipos modernos cuentan con una función llamada **Auto MDI-X**. Esta tecnología detecta automáticamente el tipo de cable y cruza las señales electrónicamente si es necesario, lo que ha hecho que el uso de cables directos sea suficiente para casi cualquier conexión.

Nuestro grupo construyó un total de 3 cables de diferentes largos. Una vez que los verificamos visualmente y con el tester de cable Ethernet, intercambiamos cables con el grupo **Subnet Surfers**, realizamos una inspección visual y lo probamos con el tester. A continuación, se muestra el cable recibido del grupo:

<div align="center">

![Cable grupo Subnet Surfers](https://github.com/user-attachments/assets/bde0a404-8e6f-4dec-b829-f89dba961172)

</div>

## Resultado Parte 2 - Equipamiento físico, verificación y utilización de equipos de red y análisis de tráfico

Para esta sección utilizamos un Switch **TP-Link TL-SF1008D de 8 puertos**, el cual posee las siguientes características:

- **Interfaz**: 8 puertos 10/100 Mbps, negociación automática, Auto-MDI/MDIX.
- **Tasas de transferencia de datos**: 10/100 Mbps en Half Duplex, 20/200 Mbps en Full Duplex.
- **Estándares y protocolos**: IEEE 802.3, IEEE 802.3u, IEEE 802.3x, CSMA/CD.
- **Tecnología Green Ethernet**: ahorra energía hasta un 60%.
- **Control de flujo IEEE 802.3x**: proporciona una transferencia de datos confiable.
- **Plug and Play** (conectar y usar): no se requiere configuración.

<div align="center">

![Switch](https://github.com/user-attachments/assets/4abb5ff0-cbc4-4a5e-b1f6-86bd35ddcb2d)

</div>

> [!NOTE]
> Como para varios grupos fue complicado acceder a la configuración del switch, se utilizó este modelo Plug and Play. Las configuraciones que se detallan a continuación fueron las necesarias para poder realizar un ping entre dos computadoras conectadas.

Para poder realizar un ping entre dos computadoras conectadas a diferentes interfaces del switch, debemos asignar una IP manualmente ya que no tenemos un servidor de DHCP que nos asigne una. Para ello, realizamos los siguientes pasos:

1. Utilizar el comando `ip addr` (Linux) o `ipconfig` (Windows) para verificar las interfaces de red disponibles en cada computadora.
2. Identificar la interfaz de red Ethernet, que generalmente empieza con la letra `e`.
3. En Linux (Ubuntu), dirigirse a la parte superior derecha, donde se encuentra el ícono de Wi-Fi o red cableada. En el apartado de red, seleccionar **Configuración de red cableada**. En Windows, ir a la parte inferior derecha, al ícono de Wi-Fi o conexión por cable, hacer clic derecho y seleccionar **Configuración de red e Internet**.
4. Para Linux, seleccionar la red cableada, hacer clic en el engranaje de opciones, ir a la sección de **IPv4**, deshabilitar la opción **Automático (DHCP)** y seleccionar la opción **Manual**. En Windows, una vez en la sección de configuración de red, ir a **Asignación de IP** y cambiarla a **Manual**.
5. Una vez configurada la opción de IPv4 en manual, asignar una **IP privada**, como por ejemplo **192.168.1.1** para la PC 1 y **192.168.1.2** para la PC 2, con una máscara de subred **255.255.255.0**. Verificar, utilizando los comandos del paso 1, que la configuración se haya aplicado correctamente.
6. Con la IP configurada, realizar dos pruebas:
   1. `ping <ip_propia>`
   2. `ping <ip_compañero>`

![Ping](https://github.com/user-attachments/assets/9b8d8f1b-d3d7-4d37-8918-76712719915d)

---

## Conclusiones

---

## Referencias

- [Switch](https://www.tp-link.com/ar/home-networking/soho-switch/tl-sf1008d/#overview)
