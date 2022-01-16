FROM python:3.8-slim

WORKDIR /usr/src/app
COPY ./ ./
RUN pip install -r requirements.txt
ENV FLASK_APP=simpleClassifier
ENV FLASK_ENV=development
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]