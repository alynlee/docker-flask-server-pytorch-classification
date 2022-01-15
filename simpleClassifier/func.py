import io

import torchvision.transforms as transforms
from PIL import Image
from .model import model as g


def transform_image(image_bytes):
    my_transform = transforms.Compose([transforms.Resize(255),
                                       transforms.CenterCrop(224),
                                       transforms.ToTensor(),
                                       transforms.Normalize(
        [0.485, 0.456, 0.406],
        [0.229, 0.224, 0.225])])

    image = Image.open(io.BytesIO(image_bytes))
    # image.show()
    return my_transform(image).unsqueeze(0)


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = g.model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return g.imagenet_class_index[predicted_idx]


if __name__ == '__main__':
    # test
    image_path = './img/elephant.jpeg'
    with open(image_path, 'rb') as f:
        image_bytes = f.read()
        predict = get_prediction(image_bytes)  # ImageNet 분류ID, Class
        print(predict)
