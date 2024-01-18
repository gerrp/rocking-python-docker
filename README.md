# Creación de aplicación web flask con entorno de Docker
### La aplicación web cumple con las siguientes 3 funciones en sus respectivas rutas:
#### Subida de archivos - localhost:5000
#### Lista de archivos - localhost:5000/ls
#### Eliminación de archivos - localhost:5000/rm
## Vagrant
Como primer paso utilicé vagrant con una imagen de **ubuntu** para crear la máquina virtual sobre la cuál voy a trabajar, en ella por medio del **bootstrap.sh** instale:                                                                                                 

**Python** (para correr los scripts de docker)                                                                                                                        
                                                                                                                                                
**Docker** (para contenerizar la aplicación)                                                                                                                    

Levantamos la máquina con ``` vagrant up 
                                           ```

Luego nos conectamos con ``` vagrant ssh
                                           ```
                                                                                                                                                                                                                                    
## Automatización de Docker con Python
Utilicé **Python** y el modulo **os** para automatizar la creación del **Dockerfile**, realizar el **docker build** y **docker run**                              
                                                
Corremos el primer script para la creación y buildeo del **Dockerfile** con ``` python3 dockerCreateBuild.py ```                              
                                                                                                              
Corremos el segundo script para correr el contenedor con ``` python3 dockerRun.py ```                                                                 

Desde este momento ya podemos ingresar al **localhost:5000** con sus respectivas rutas y probar todas las funcionalidades de la aplicación, además podemos ver el contenedor corriendo con ``` docker ps ```

                                                              
