# 다른 풀이 2
# fractions 라이브러리 활용 - 유리수를 계산할 때 사용하는 모듈
from fractions import Fraction

def solution(denum1, num1, denum2, num2):
    answer = Fraction(denum1, num1) + Fraction(denum2, num2)
    return [answer.numerator, answer.denominator]