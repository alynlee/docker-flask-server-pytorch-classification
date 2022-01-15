
from torchvision import models
import json


def init():
    global model
    global imagenet_class_index
    print("model initialize")
    imagenet_class_index = json.load(
        open('simpleClassifier/img/imagenet_class_index.json'))
    model = models.densenet121(pretrained=True)
    model.eval()
