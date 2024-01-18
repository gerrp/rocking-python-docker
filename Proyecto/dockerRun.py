import os

dockerRun = "docker run -p 5000:5000 -d --name FlaskDesafio prueba:1.0"
os.system(dockerRun)