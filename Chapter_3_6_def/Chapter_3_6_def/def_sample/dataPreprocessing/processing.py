# -*- coding: utf-8 -*-
from time import sleep

def process_data(data):
    print("~~ 데이터 전처리 함수를 실행합니다! ~~")
    modified_data = data + "가 수정 완료 되었습니다."
    # print(modified_data)
    sleep(10)
    print("~~ 데이터 전처리가 끝났습니다! ~~")
    return modified_data