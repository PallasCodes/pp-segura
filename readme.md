# Proyecto de programación segura
## Pre-requisitos
1. Python 3+
2. Docker

## Instalación
1. Descargar repo
```
  git clone https://github.com/PallasCodes/pp-segura.git
```

2. Dentro de la carpeta del proyecto, crear la imagen de docker
```
docker-compose build
```

3. Correr docker-compose
```
docker-compose up -d
```

4. Abrir docker desktop e ir a la terminal del contenedor 'web' y correr los siguientes comandos
```
python manage.py collecstatic
```
Esto va a mover los archivos estáticos del admin de django a nuestro carpeta actual para archivos estáticos

```
python manage.py migrate
```
Crear las migraciones para la BD

```
python manage createsuperuser
```
Crear super usuario para poder entrar al admin

5. Entrar al admin en http://localhost:1337/admin y crear un grupo llamado 'professor'
6. Asignarle el grupo 'professor' a la cuenta de un profesor (puede ser la cuenta de admin)
7. Crear un User Telegram con el chat_id necesario y vincularlo a la cuenta del profesor

El proyecto corre en http://localhost:1337