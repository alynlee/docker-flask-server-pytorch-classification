from flask import Blueprint

bp = Blueprint("main", __name__, url_prefix="/")


@bp.route("/predict", methods=["POST"])
def predict():
    return jsonify({"class_id": "IMAGE_NET_XX", "class_name": "cat"})
