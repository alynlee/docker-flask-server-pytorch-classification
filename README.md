# flask_model_serving_practice

## Just execute app in local
1. in terminal `FLASK_APP=simpleClassifiler`
2. Enter simpleClassifier folder
3. in terminal `flask run`
4. Open another terminal
5. in another terminal `python test.py`

result : {'class_id': 'n02504458', 'class_name': 'African_elephant'}

## Using docker 

1. `docker build -t alynlee/flask-example ./`
2. `docker run -it -p 5000:5000 alynlee/flask-example`
3. Open another terminal
4. in another terminal `curl -X POST -F "file=@simpleClassifiler/img/elephant.jpeg" dockerIP:PORT/predict
