from flask import Blueprint, jsonify
from flask import request
from simpleClassifier.func import get_prediction, transform_image

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/predict", methods=["POST"])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        image_bytes = file.read()
        class_id, class_name = get_prediction(image_bytes)
        print(f"class_id: {class_id}, class_name: {class_name}")
        return jsonify({"class_id": class_id, "class_name": class_name})
