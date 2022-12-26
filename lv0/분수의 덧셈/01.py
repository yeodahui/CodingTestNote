# 내 풀이
# 유클리드 호제법을 이용해 최대공약수를 구하는 함수 getGCD를 만들어 사용
def getGCD(num1, num2):
    if num1 < num2 :
        x = num1
        y = num2
    else :
        x = num2
        y = num1
    while(y):
        x, y = y, x % y
    return x


def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = getGCD(denum, num)
    return [denum / gcd, num / gcd]
