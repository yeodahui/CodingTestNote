# 내 풀이
# sort 함수 활용
def solution(array):
    array.sort()
    return array[len(array) // 2]

# 다른 풀이
# 기존 파라미터를 변경하지 않고 정렬한 결과를 반환하도록 sorted()를 사용
def solution(array):
    return sorted(array)[len(array) // 2]