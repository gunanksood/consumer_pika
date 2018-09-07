FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app1
WORKDIR /app1
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["worker.py"]