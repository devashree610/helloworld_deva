FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app
Run pip install -r requirements.txt
EXPOSE 5000
CMD python app.py 