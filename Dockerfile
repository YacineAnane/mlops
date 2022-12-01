FROM ubuntu:latest
USER root
WORKDIR /home/user
COPY model/model_api.py /home/user/
COPY model/random_forest.joblib /home/user/
COPY requirements.txt /home/user/

# ENV PYTHONUNBUFFERED=1
# RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
# RUN python3 -m ensurepip
# RUN python3 -m pip install --upgrade pip setuptools wheel
# RUN pip3 install --no-cache --upgrade pip
# RUN pip3 install -r requirements.txt

RUN ls -la
RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "model_api.py"]
