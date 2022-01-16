FROM python:3.8.5

# WORKDIR /usr/src/app
# COPY ./ ./
# RUN pip install -r requirements.txt
# ENTRYPOINT export FLASK_APP=simpleClassifier
# ENTRYPOINT export FLASK_ENV=development
# EXPOSE 5000

#CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["echo", "-u" "hello"]