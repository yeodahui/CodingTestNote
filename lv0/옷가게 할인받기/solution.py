# 내 풀이
import math

def solution(price):
    discount_rate = 0

    if price >= 500000 :
        discount_rate = 0.2
    elif price >= 300000 :
        discount_rate = 0.1
    elif price >= 100000 :
        discount_rate = 0.05

    return math.floor(price * (1 - discount_rate))

# 다른 풀이
# math 라이브러리 사용하지 않고 int 함수만으로 내림 할 수 있다
# 딕셔너리 자료형으로 할인률과 기준을 정리해 코드를 읽기도 수정하기도 좋다
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)