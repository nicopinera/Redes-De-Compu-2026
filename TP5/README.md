# Informe TP5

## Integrantes

- Nicolás Piñera
- Julián Krede
- Federico Andres Arnaudo
- Franco Perotti

**Nombre del Grupo**: Puerto1337

## UNC - Facultad de Ciencias Exactas, Físicas y Naturales

## Cátedra: Redes de Computadoras

### Profesores

- Henn, Santiago Martín
- Oliva Cúneo, Facundo

**Fecha**: 04/06/2026

---

## Información de los autores

- **Información de contacto**:
  - [nicolas.pinera@mi.unc.edu.ar](mailto:nicolas.pinera@mi.unc.edu.ar)
  - [julian.krede@mi.unc.edu.ar](mailto:julian.krede@mi.unc.edu.ar)
  - [federico.arnaudo@mi.unc.edu.ar](mailto:federico.arnaudo@mi.unc.edu.ar)
  - [franco.perotti@mi.unc.edu.ar](mailto:franco.perotti@mi.unc.edu.ar)

---

## Resumen

El presente trabajo práctico analiza el comportamiento de una arquitectura de servicios mediante el simulador **Server Survival**. A partir de distintos tipos de tráfico, como solicitudes estáticas, lecturas, escrituras, cargas de archivos, búsquedas y tráfico malicioso, se estudia el rol de componentes como firewall, balanceador de carga, colas, servidores de cómputo, bases de datos, caché, almacenamiento y CDN. El objetivo es observar cómo una infraestructura responde ante variaciones de carga, identificar cuellos de botella y evaluar estrategias de escalabilidad. Además, se busca relacionar los elementos del simulador con conceptos reales de redes, servicios cloud, seguridad y disponibilidad.

**Palabras clave**: arquitectura cloud, balanceo de carga, firewall, colas, caché, base de datos, escalabilidad, tráfico malicioso, cuello de botella, Server Survival.

---

## Introducción

En una arquitectura de servicios real, las solicitudes de los usuarios no son procesadas por un único componente, sino por un conjunto de servicios especializados. Cada uno cumple una función específica: filtrar tráfico, distribuir carga, ejecutar lógica de aplicación, almacenar datos, acelerar consultas o proteger la infraestructura frente a ataques. En este trabajo se utiliza el simulador **Server Survival** para representar estos conceptos de forma práctica. A través de distintas pruebas se analiza cómo impactan los cambios en el tipo y volumen de tráfico, qué componentes fallan primero y qué decisiones permiten mejorar la estabilidad del sistema. De esta manera, el trabajo permite vincular conceptos de redes e infraestructura cloud con situaciones concretas de diseño, operación y escalabilidad.

---

## Resultados

## 1) Reconocimiento de componentes de la arquitectura

| Componente | Función principal | Capa TCP/IP asociada | Impacto si no está presente |
|---|---|---|---|
| **Firewall** | Filtra tráfico malicioso y protege la infraestructura. | Opera principalmente en la capa de Aplicación (inspección de tráfico HTTP) y en la capa de Red/Internet. | Los ataques llegarían directamente a los servicios internos, aumentando riesgos de caídas y compromisos de seguridad. |
| **Load Balancer** | Distribuye las solicitudes entre múltiples instancias para evitar sobrecargas. | Principalmente **Transporte** o **Aplicación**, según si distribuye conexiones o peticiones HTTP. | Una instancia puede saturarse mientras otras quedan subutilizadas. También se dificulta el escalado horizontal y la tolerancia a fallos. |
| **Queue** | Desacopla componentes y absorbe picos de tráfico almacenando solicitudes temporalmente. | Opera en la capa de **Aplicación**. | Los picos de carga provocarían pérdida de solicitudes o saturación inmediata de los servidores. |
| **Compute** | Este componente representa un servidor de procesamiento generico. | Opera en la capa de **Aplicación**. | No habría procesamiento de solicitudes ni ejecución de la aplicación. |
| **Serverless Function** | Ejecuta tareas específicas bajo demanda sin necesidad de servidores permanentes. | Opera en la capa de **Aplicación**. | Las tareas event-driven deberían ejecutarse en servidores tradicionales, aumentando complejidad y costos. |
| **SQL DB** | Almacena datos estructurados con consistencia y transacciones. | Opera en la capa de **Aplicación**. | No habría persistencia confiable para los datos de negocio. |
| **NoSQL** | Almacena grandes volúmenes de datos no estructurados o semiestructurados. | Opera en la capa de **Aplicación**. | Algunos casos de uso requerirían bases relacionales menos eficientes o difíciles de escalar. |
| **Cache** | Guarda datos accedidos frecuentemente para reducir tiempos de respuesta y carga sobre la base de datos. | Opera en la capa de **Aplicación**. | La base de datos recibiría muchas más consultas y podría convertirse rápidamente en cuello de botella. |
| **CDN (Content Delivery Network)** | Distribuye contenido estático desde ubicaciones cercanas a los usuarios. | Principalmente **Aplicación**, aunque se apoya en mecanismos de red como DNS y ruteo. | Aumentaría la latencia y el consumo de ancho de banda de los servidores principales. |
| **Storage** | Almacena archivos como imágenes, videos, documentos y backups. | Opera en la capa de **Aplicación**. | Los archivos deberían almacenarse en servidores de aplicación o bases de datos, reduciendo eficiencia y escalabilidad. |
| **Search Engine** | Permite búsquedas rápidas e indexadas sobre grandes volúmenes de datos. | Opera en la capa de **Aplicación**. | Las búsquedas serían lentas y consumirían recursos excesivos de la base de datos. |
| **Réplica** | Replica datos de una base principal para distribuir consultas de lectura. | Opera en la capa de **Aplicación**. | Toda la carga recaería sobre la base principal, reduciendo rendimiento y escalabilidad. |

### 2) Tipos de trafico

| Tipo de tráfico | Ejemplo real                                                    | Componente recomendado            | Riesgo si se procesa incorrectamente                                                                           |
| --------------- | --------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| STATIC          | Imágenes, archivos CSS, JavaScript, logos, fuentes web.         | CDN + Storage                     | Se desperdicia capacidad de cómputo, aumenta la latencia y los servidores pueden saturarse innecesariamente.   |
| READ            | Consultar perfil de usuario, ver productos, leer publicaciones. | Cache + SQL DB / NoSQL + Réplicas | La base de datos recibe demasiadas consultas y puede convertirse en un cuello de botella.                      |
| WRITE           | Registrar usuarios, realizar compras, publicar contenido.       | Compute + SQL DB + Queue          | Pérdida de datos, inconsistencias o saturación de la base de datos durante picos de tráfico.                   |
| UPLOAD          | Subir imágenes, videos, documentos o archivos adjuntos.         | Storage + Serverless Function     | Los servidores de aplicación consumen demasiado almacenamiento y recursos de procesamiento.                    |
| SEARCH          | Buscar productos, usuarios, artículos o documentos.             | Search Engine                     | Las búsquedas se vuelven lentas y generan una carga excesiva sobre la base de datos.                           |
| MALICIOUS       | Ataques DDoS, escaneo de vulnerabilidades, bots maliciosos.     | Firewall                          | El tráfico malicioso alcanza los servicios internos provocando degradación, caídas o compromisos de seguridad. |

### 3) Testeando el componente Queue

Como describimos anteriormente, el componente Queue se encarga de absorber picos de tráfico almacenando temporalmente las solicitudes. Esto permite que el componente Compute (Servidor) procese las peticiones, evitando su saturación ante aumentos repentinos de carga. Este comportamiento lo podemos ver en la siguiente imagen:

![Aumento repentino de tráfico](https://github.com/user-attachments/assets/d58e6674-a1b0-4399-bb16-14e0a077a3c6)

Luego al disminuir el trafico a 0 la queue envia de manera secuencial y gradual las peticiones que retuvo, cumpliendo su proposito y sin rechazar peticiones

![Disminucion del trafico](https://github.com/user-attachments/assets/6b1ac1d4-a9b0-4cde-b5c0-8901f5a9cf10)

### 4) Primera infraestructura

Para esta primera parte diseñamos una infraestructura inicial completa con:

- 1 Firewall
- 1 Load balancer
- 2 Servidores (compute) cada uno con un queue
- 1 CDN
- 1 Storage
- 1 Memory cache
- 1 SQL DB

Arrancamos con 10 request por segundo con la distribucion por defecto que ofrece el juego

![Infraestructura inicial](https://github.com/user-attachments/assets/768cbd3d-9aad-454b-9ad4-2666e616785a)

Aumentamos a 15 la cantidad de request por segundo y comenzamos a observar que se producian una baja cantidad de fallas debido a sobrecargas en los servidores

![Carga de 15 request por segundo](https://github.com/user-attachments/assets/c22db37a-5de9-4d00-a2fc-2d0598682da0)

Aumentamos un poco mas la carga a 20 request por segundo y comenzo a aumentar a un nivel significativo la cantidad de fallas, disminuyendo la reputación. Esto no llevo a tener que modificar la infraestructura

![Carga con 20 request por segundo](https://github.com/user-attachments/assets/74a8f1d3-b1bd-4765-8038-6c0c862b8029)

### Escalabilidad y balanceo

Debido a que el problema se encuentra en la sobrecarga de los servidores colocamos un servidor con un correspondiente queue y aumentamos el trafico a 25 request por segundo de forma tal que el sistema se mantiene estable

![Carga con 25 request por segundo](https://github.com/user-attachments/assets/4dba2db1-6ef8-493d-84ea-dd0c8305343c)

Notamos que el principal componente que limita nuestro sistema son los servidores, por lo tanto para poder aumentar el trafico debemos aumentar la cantidad de servidores. Para llegar a 35 request por segundo colocamos un servidor mas, logramos mantener la reputacion a pesar de tener fallas aisladas

![Carga con 35 request por segundo](https://github.com/user-attachments/assets/b8a640c9-7dd4-4feb-a2ce-b1673e783aa7)

### Sobrevivir

Finalmente en un intento de aumentar el trafico, perdimos de manera abrupta toda la reputacion, intentamos bajarlo al nivel anterior pero ya habiamos perdido. El tiempo total sobrevivido es de **11 minutos y 1 segundo**, con un puntaje total de **96643**. Al momento de la captura final, la arquitectura mantenía presupuesto positivo, pero la reputación había caído a **0%**.

![Game over](https://github.com/user-attachments/assets/b9ebdb26-c8a4-486d-a803-ec961d5e6e42)

### Cuestionario

**¿Qué componente falló primero?**

El primer componente en fallar fue el servidor.

**¿Por qué creés que falló?**

Debido a que es el componente por el cual pasan casi todos los tipos de request.

**¿Fue un problema de capacidad, diseño, costo o seguridad?**

Fue un problema de capacidad del servidor.

**¿Por qué elegiste cada componente?**

Agregamos los componentes debido a que algunos son necesarios para completar requests otros porque mejoran la capacidad del sistema y otros previenen de ataques

- Firewall: Este componente filtra las request maliciosas, evita que se propaguen adentro del sistema sobrecargando innecesariamente los demas componentes
- Load balancer: Permite distribuir todas las requests entrantes entre los distintos servidores para evitar sobrecargas
- CDN: Este sirve para atender las peticiones tipo _STATIC_
- Queue: Este componente mejora la capacidad del sistema, permite retener requests con el fin de que los servidores no se sobrecarguen
- Compute: Estos son el eje principal del sistema, estos gestionan los demas tipos de peticiones: _READ_, _WRITE_, _SEARCH_ y _UPLOAD_ que luego son tratados por sus correspondientes componentes
- Cache: Este componente es conectado a la base de datos, tiene un 35% a nivel 1 de que una peticion tipo _READ_ sea resuelta en el mismo de forma tal que reduce la carga que iría a la base de datos
- SQL DB: Esta es la base de dato, trata las peticiones _READ_, _WRITE_ y _SEARCH_

## Conclusiones

A lo largo del trabajo se pudo observar que el diseño de una arquitectura de servicios no depende únicamente de agregar componentes, sino de distribuir correctamente las responsabilidades según el tipo de tráfico recibido. En las primeras pruebas, una infraestructura mínima logró funcionar con cargas bajas, pero al aumentar el rate había saturación en zonas específicas del sistema y aparecieron pérdidas de reputación.

En el modo Survival, la arquitectura fue mejorada progresivamente incorporando mas componentes. Cada uno permitió atender un tipo de tráfico específico: el Firewall filtró ataques, Compute procesó solicitudes dinámicas, SQL DB gestionó lecturas y escrituras, Storage atendió archivos, Search Engine resolvió búsquedas y Cache ayudó a reducir consultas repetidas.

El principal problema observado fue la degradación del sistema frente a una carga creciente. En particular, la zona de Compute apareció como un cuello de botella recurrente, ya que gran parte del procesamiento dependía de estas instancias. Aunque se incorporaron mejoras, la reputación terminó descendiendo, lo que indica que el sistema no logró sostener la calidad de respuesta necesaria durante toda la simulación.

Como mejora futura, se priorizaría escalar la capacidad de Compute y luego reforzar los servicios que concentren mayor carga, como SQL DB, Search Engine o Storage. También sería conveniente ajustar la arquitectura según el tráfico predominante, evitando agregar componentes innecesarios que aumenten el costo sin resolver el cuello de botella real.

En conclusión, el simulador permitió relacionar conceptos de redes e infraestructura cloud con situaciones prácticas de diseño, escalabilidad y tolerancia a fallos. La experiencia nos muestra que una arquitectura eficiente requiere equilibrio entre seguridad, procesamiento, almacenamiento, caché, balanceo de carga y costos operativos.

## Referencias

- [Enlace al juego](https://pshenok.github.io/server-survival/)
