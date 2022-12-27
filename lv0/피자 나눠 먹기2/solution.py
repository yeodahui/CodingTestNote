# 내 풀이
# math.lcm(a, b)을 사용했으나 *파이썬 3.9 버전 이후부터 사용 가능하여 채점 불가*
import math

def solution(n):
    pieces = 6
    return math.lcm(n, pieces) // 6

# 수정한 풀이
# gdc를 활용해 최소공배수 함수를 만듦
import math

def lcm(a, b):
    return a * b / math.gcd(a, b)

def solution(n):
    pieces = 6
    return lcm(n, pieces) // 6