# yetanother-tinyurl
Сервис коротких ссылок позволяет сокращать длинные URL, предоставляя короткий и удобный альтернативный адрес, который будет перенаправлять пользователя на исходный URL.

## Stack:
### Backend:
[![Python 3.10](https://img.shields.io/badge/Python%203.10-14354C?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django%202.2-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/Django%20REST%20Framework%203.12-092E20?style=for-the-badge&logo=django)](https://www.django-rest-framework.org/)

[![Nginx](https://img.shields.io/badge/NGINX-008000?style=for-the-badge&logo=NGINX)](https://nginx.org/ru/)
[![Gunicorn](https://img.shields.io/badge/gunicorn-ffffff?style=for-the-badge&logo=gunicorn)](https://gunicorn.org/)

[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)

### Infrastructure and Automation:
[![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)](https://ubuntu.com/)
[![Docker](https://img.shields.io/badge/Docker-87cefa?style=for-the-badge&logo=docker)](https://www.docker.com/)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-1e90ff?style=for-the-badge&logo=Yandex.Cloud)](https://cloud.yandex.ru/)

## Локальный запуск проекта и установка зависимостей:
```zsh 
sudo apt update
```
```zsh 
sudo apt upgrade -y
```
```zsh 
sudo apt install python3-pip -y
```
### Установливаем Docker и docker-compose:
```zsh 
sudo apt install docker.io -y
```
```zsh 
sudo curl -SL https://github.com/docker/compose/releases/download/v2.13.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
```
```zsh 
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```
```zsh 
sudo chmod 666 /var/run/docker.sock
```
```zsh 
 DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
 mkdir -p $DOCKER_CONFIG/cli-plugins
 curl -SL https://github.com/docker/compose/releases/download/v2.13.0/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
 chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
 ```
### Клонируем репозиторий:
```zsh 
git clone https://github.com/0ne1ce/yetanother-tinyurl.git
```
### Создаем .env:
```zsh 
cd yetanother-tinyurl/infra
```
```zsh 
nano .env
```
```zsh 
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY='*SECRET_KEY*'
ALLOWED_HOSTS=*
```
### Поднимаем контейнеры:
```zsh 
docker compose up
```
```zsh 
docker compose up --build
```
### Выполняем миграции:
```zsh 
docker compose exec web python3 manage.py makemigrations
```
```zsh 
docker compose exec web python3 manage.py migrate
```
### Создаем суперпользователя (опционально):
```zsh 
docker compose exec web python3 manage.py createsuperuser
```