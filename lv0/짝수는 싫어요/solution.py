# 내 풀이
def solution(n):
    answer = []
    for i in range(1, n+1, 2) :
        answer.append(i)
    return answer

# 다른 풀이
# 메모리 공간을 차지하지 않게 할 수 있다
def solution(n):
    return [i for i in range(1, n+1, 2)]