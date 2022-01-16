# 이미지를 가져오는 양식(form)과 예측 결과를 표시하는 페이지
    # url img 넣는 곳 만들기 (원하는 이미지를 넣을 수 있게)
    # predict 버튼 만들기
    # predict된 결과 보여주기
    # img가 아닌 다른 유형의 파일이 들어왔을때 예외처리
    # 모델이 이미지를 인식할 수 없을때 처리하는 구문 만들기


import requests

if __name__ == '__main__':
    resp = requests.post("http://localhost:5000/predict",
                         files={"file": open('./img/elephant.jpeg', 'rb')})
    print(resp.json())
