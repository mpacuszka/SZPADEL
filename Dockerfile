FROM python:3.11.4-slim-bullseye

WORKDIR /usr/src/app

COPY requirements.txt ./
# COPY src /usr/src/app/src/
# COPY tests /usr/src/app/tests/

COPY . .

RUN echo starting hahaha

RUN pip install --no-cache-dir -r requirements.txt

#CMD ["python", "src/main.py"]
