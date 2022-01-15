# 1.API 엔드포인트의 요청과 응답 정의
# 이미지가 포함된 file HTTP POST로 /predict에 요청
# 응답은 json 형태
# ["class_id" : "blabla", "class_name" : "cat"]


from flask import Flask
from .model import model
import sys


def create_app():
    app = Flask(__name__)

    # for deeplearning model
    model.init()

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
