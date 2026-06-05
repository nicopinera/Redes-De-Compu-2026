# Informe TP5

## Integrantes

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

**Palabras clave**:

---

## Introducción

---

## Resultados

### Componentes de la arquitectura

**Firewall**: Filtra tráfico malicioso y protege la infraestructura. Opera principalmente en la capa de Aplicación (inspección de tráfico HTTP) y en la capa de Red/Internet. Sin él, los ataques llegarían directamente a los servicios internos, aumentando riesgos de caídas y compromisos de seguridad.

**Load Balancer**: Distribuye las solicitudes entre múltiples instancias para evitar sobrecargas. Opera en la capa de Aplicación o Transporte. Sin él, algunos servidores podrían saturarse mientras otros permanecen ociosos.

**Queue**: Desacopla componentes y absorbe picos de tráfico almacenando solicitudes temporalmente. Opera en la capa de Aplicación. Sin ella, los picos de carga provocarían pérdida de solicitudes o saturación inmediata de los servidores.

**Compute**: Este componente representa un servidor de procesamiento generico. Ejecuta la lógica principal de la aplicación. Opera en la capa de Aplicación. Sin él, no habría procesamiento de solicitudes ni ejecución de la aplicación.

**Serverless Function**: Ejecuta tareas específicas bajo demanda sin necesidad de servidores permanentes. Opera en la capa de Aplicación. Sin ella, las tareas event-driven deberían ejecutarse en servidores tradicionales, aumentando complejidad y costos.

**SQL DB**: Almacena datos estructurados con consistencia y transacciones. Opera en la capa de Aplicación. Sin ella, no habría persistencia confiable para los datos de negocio.

**NoSQL**: Almacena grandes volúmenes de datos no estructurados o semiestructurados. Opera en la capa de Aplicación. Sin ella, algunos casos de uso requerirían bases relacionales menos eficientes o difíciles de escalar.

**Cache**: Guarda datos accedidos frecuentemente para reducir tiempos de respuesta y carga sobre la base de datos. Opera en la capa de Aplicación. Sin ella, la base de datos recibiría muchas más consultas y podría convertirse rápidamente en cuello de botella.

**CDN (Content Delivery Network)**: Distribuye contenido estático desde ubicaciones cercanas a los usuarios. Opera en la capa de Aplicación. Sin ella, aumentaría la latencia y el consumo de ancho de banda de los servidores principales.

**Storage**: Almacena archivos como imágenes, videos, documentos y backups. Opera en la capa de Aplicación. Sin él, los archivos deberían almacenarse en servidores de aplicación o bases de datos, reduciendo eficiencia y escalabilidad.

**Search Engine**: Permite búsquedas rápidas e indexadas sobre grandes volúmenes de datos. Opera en la capa de Aplicación. Sin él, las búsquedas serían lentas y consumirían recursos excesivos de la base de datos.

**Réplica**: Replica datos de una base principal para distribuir consultas de lectura. Opera en la capa de Aplicación. Sin ella, toda la carga recaería sobre la base principal, reduciendo rendimiento y escalabilidad.

### Tipos de trafico

| Tipo de tráfico | Ejemplo real                                                    | Componente recomendado            | Riesgo si se procesa incorrectamente                                                                           |
| --------------- | --------------------------------------------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| STATIC          | Imágenes, archivos CSS, JavaScript, logos, fuentes web.         | CDN + Storage                     | Se desperdicia capacidad de cómputo, aumenta la latencia y los servidores pueden saturarse innecesariamente.   |
| READ            | Consultar perfil de usuario, ver productos, leer publicaciones. | Cache + SQL DB / NoSQL + Réplicas | La base de datos recibe demasiadas consultas y puede convertirse en un cuello de botella.                      |
| WRITE           | Registrar usuarios, realizar compras, publicar contenido.       | Compute + SQL DB + Queue          | Pérdida de datos, inconsistencias o saturación de la base de datos durante picos de tráfico.                   |
| UPLOAD          | Subir imágenes, videos, documentos o archivos adjuntos.         | Storage + Serverless Function     | Los servidores de aplicación consumen demasiado almacenamiento y recursos de procesamiento.                    |
| SEARCH          | Buscar productos, usuarios, artículos o documentos.             | Search Engine                     | Las búsquedas se vuelven lentas y generan una carga excesiva sobre la base de datos.                           |
| MALICIOUS       | Ataques DDoS, escaneo de vulnerabilidades, bots maliciosos.     | Firewall                          | El tráfico malicioso alcanza los servicios internos provocando degradación, caídas o compromisos de seguridad. |

### Testeando el componente Queue

Como describimos anteriormente, el componente Queue se encarga de absorber picos de tráfico almacenando temporalmente las solicitudes. Esto permite que el componente Compute (Servidor) procese las peticiones, evitando su saturación ante aumentos repentinos de carga. Este comportamiento lo podemos ver en la siguiente imagen:

![Aumento repentino de tráfico](https://github.com/user-attachments/assets/d58e6674-a1b0-4399-bb16-14e0a077a3c6)

Luego al diminuir el trafico a 0 la queue envia de manera secuencial y gradual las peticiones que retuvo, cumpliendo su proposito y sin rechazar peticiones

![Disminucion del trafico](https://github.com/user-attachments/assets/6b1ac1d4-a9b0-4cde-b5c0-8901f5a9cf10)

### Primera infraestructura

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

Finalmente en un intento de aumentar el trafico, perdimos de manera abrupta toda la reputacion, intentamos bajarlo al nivel anterior pero ya habiamos perdido

![Game over](https://github.com/user-attachments/assets/b9ebdb26-c8a4-486d-a803-ec961d5e6e42)

### Cuestionario

**¿Qué componente falló primero?**

El primer componente en fallar fue el servidor

**¿Por qué creés que falló?**

Debido a que es el componente por el cual pasan casi todos los tipos de request

**¿Fue un problema de capacidad, diseño, costo o seguridad?**

Fue un problema de capacidad del servidor

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

---

## Referencias

- [Enlace al juego](https://pshenok.github.io/server-survival/)
