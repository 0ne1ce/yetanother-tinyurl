sudo apt update && sudo apt install -y python3 python3-pip && \
pip3 install psycopg2-binary

sudo apt install docker.io -y
sudo curl -SL https://github.com/docker/compose/releases/download/v2.13.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
sudo chmod 666 /var/run/docker.sock
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}
mkdir -p $DOCKER_CONFIG/cli-plugins
curl -SL https://github.com/docker/compose/releases/download/v2.13.0/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose

git clone https://github.com/0ne1ce/yetanother-tinyurl.git
cd yetanother-tinyurl
cd infra
nano .env
nano nginx.conf

docker compose up --build

docker compose exec web python3 manage.py migrate
docker compose exec web python3 manage.py makemigrations
docker compose exec web python3 manage.py collectstatic --no-input
docker compose exec web python3 manage.py createsuperuser