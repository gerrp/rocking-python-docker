import os

def createDockerFile(baseImage,port):
    dockerText= f"""
FROM {baseImage}

RUN mkdir /app
RUN mkdir app/Archivos
WORKDIR /app
ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py

EXPOSE {port}

ENTRYPOINT ["python"]

CMD ["-m", "flask", "run", "--host", "0.0.0.0"]

"""
    with open ("./Docker-app/Dockerfile","w") as dockerfile:
        dockerfile.write(dockerText)

if __name__ == "__main__":

    imageName = "prueba:1.0"
    baseImage = "python:3.8"
    port = "5000"

    createDockerFile(baseImage,port)
    dockerBuild = f"docker build ./Docker-app -t {imageName}"
    os.system(dockerBuild)

