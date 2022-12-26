# 내 풀이
# for in 구문 활용해 배열 순회
def solution(numbers):
    answer = []
    for i in numbers :
        answer.append(i * 2)
    return answer

# 다른 풀이
# for … in 구문을 활용하되, 리스트 컴프리헨션(List comprehension)을 사용하여 코드를 단축했다.
# 리스트 컴프리헨션 문법 => [표현식 for 항목 in 반복가능객체( if 조건문)]
def solution(numbers):
    return [num * 2 for num in numbers]