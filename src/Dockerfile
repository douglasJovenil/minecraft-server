  
FROM python

WORKDIR /minecraft

RUN apt-get update -y
RUN apt-get install openjdk-17-jre-headless -y

COPY src/setup.py .
COPY src/start.py .
COPY src/utils.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN python setup.py

EXPOSE 25565

ENTRYPOINT ["python", "start.py"]