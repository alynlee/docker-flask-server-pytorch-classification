# url img 넣는 곳 만들기 (원하는 이미지를 넣을 수 있게)
# predict 버튼 만들기
# predict된 결과 보여주기

import requests

if __name__ == '__main__':
    resp = requests.post("http://localhost:5000/predict",
                         files={"file": open('./img/elephant.jpeg', 'rb')})
    print(resp.json())
