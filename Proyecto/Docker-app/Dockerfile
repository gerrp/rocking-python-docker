
FROM python:3.8

RUN mkdir /app
RUN mkdir app/Archivos
WORKDIR /app
ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["-m", "flask", "run", "--host", "0.0.0.0"]

