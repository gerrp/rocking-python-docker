sudo apt update

#instalacion de python
sudo apt install -y python3

#docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh

#usar docker sin sudo
sudo groupadd docker
sudo usermod -aG docker vagrant
newgrp docker



