# 내 풀이
# keys = list(set(array))
# set 자료형은 중복된 값을 가지지 않기 때문에, 순서가 중요하지 않으면 이 방법을 활용해 중복값을 제거한 리스트를 구할 수 있음
# count 배열과 함수의 이름이 헷갈림
# max(count)가 두 번 사용되고있음
def solution(array):
    keys = list(set(array))
    count = []

    for i in keys:
        count.append(array.count(i))

    if count.count(max(count)) > 1:
        return -1
    else:
        return keys[count.index(max(count))]

# 수정한 풀이
# 재사용하는 값을 변수에 저장 (maxCount = 가장 많은 빈도 수)
# return -1을 가독성있게 변경
# count → countList 변수명 변경
def solution(array):
    keys = list(set(array))
    countList = []
    maxCount = 0

    for i in keys:
        countList.append(array.count(i))

    maxCount = max(countList)

    if countList.count(maxCount) > 1:
        return -1

    return keys[countList.index(maxCount)]