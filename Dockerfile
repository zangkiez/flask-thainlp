FROM python:3.9-slim

COPY requirements.txt /flask-app/requirements.txt

RUN pip install -r /flask-app/requirements.txt

COPY app.py /flask-app/app.py

WORKDIR flask-app

 CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]