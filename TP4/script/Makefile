IMAGE_NAME = tp4/server
CONTAINER_NAME = tp4-server-instance

# Construir la imagen de Docker
build:
	docker build -t $(IMAGE_NAME) .

# Ejecutar el contenedor mapeando el puerto 5000
run:
	docker run -d -p 5000:5000 --name $(CONTAINER_NAME) $(IMAGE_NAME)

# Detener y eliminar el contenedor
stop:
	docker stop $(CONTAINER_NAME) || true
	docker rm $(CONTAINER_NAME) || true

# Ver los logs en tiempo real
logs:
	docker logs -f $(CONTAINER_NAME)

# Limpiar todo (detener y borrar imagen)
clean: stop
	docker rmi $(IMAGE_NAME) || true
