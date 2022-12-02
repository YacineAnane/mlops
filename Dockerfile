FROM python:3.10.4

USER root
WORKDIR /home/user
COPY model/model_api.py /home/user/
COPY model/random_forest.joblib /home/user/
COPY requirements.txt /home/user/

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "model_api.py"]
