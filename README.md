# CTF_Proyecto
## Juego de Trivia Multijugador
Este proyecto es un juego de trivia al estilo Kahoot en el que varios jugadores pueden competir en tiempo real para responder preguntas y ganar puntos. La arquitectura se basa en microservicios, donde cada funcionalidad principal (gestión de preguntas, sesiones de juego, perfiles de usuarios, y notificaciones) está aislada en un servicio independiente.

## Tabla de Contenidos
* Tecnologías Utilizadas
* Requisitos
* Configuración del Entorno
* Despliegue con Docker y Kubernetes
* Ejemplo de Endpoints
* Autor y Contribuciones

## Tecnologías Utilizadas
* Lenguaje de Backend: Python (FastAPI) para APIs REST
* Autenticación: JWT
* Contenerización: Docker
* Orquestación: Kubernetes
* Monitorización y Observabilidad: Istio

## Requsitos
* **Docker:** Para empaquetar y ejecutar los microservicios de forma aislada.
* **Kubernetes:** Para gestionar el ciclo de vida de los contenedores y facilitar el escalado.
* **Istio:** Para el monitoreo, gestión de tráfico y supervisión de los servicios.

### Instalación de Docker y kubernetes 

```
Para la instalacion de Docker es necesario descargarlo desde la pagina https://www.docker.com/get-started/
y habilitar kubernetes desde la configuración 
```

### INstalar Istio para el monitoreo
* Descaragar Istio desde el sitio web:
```
curl -L https://istio.io/downloadIstio | sh -
```

* Accede a la carpeta de Istio:
```
cd istio-1.*
```

* Agrega Istio al PATH:
```
$env:Path += ";$PWD/bin"
istioctl install --set profile=demo -y
```

* Habilitar la inyecccion automatica de Istio
```
kubectl label namespace default istio-injection=enabled
```

### Configuración de entorno

1. Clonar repositorio
```
git clone https://github.com/Ernesto0701/CTF_Proyecto.git
cd CTF_Proyecto
```

2. Configurar Docker, cada microservicio tiene su propio Dockerfile.
   Puedes construir e iniciar los contenedores utilizando Docker Compose
```
docker-compose up -d
```



