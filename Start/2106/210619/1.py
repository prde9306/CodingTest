# 프로그래머스 스택, 큐
# 가장 중요도 높은 문서 먼저 인쇄
# 대기목록에서 꺼내기
# 나머지 목록에서 중요도 높은 문서 있는지 확인 잇으면 앞에서 꺼낸 것 맨뒤에
# 없으면 바로인쇄

# 인쇄 요청한 문서 몇 번째로 인쇄되는지 ?
# properties = 목록, location = 내문서 위치 return = 몇 번째?
"""
def solution(properties, location):
    properties=[]
    location = properties[i]
    for i in range(properties.len):
        location1 = properties[i+1]
        if location < location1 for in range(properties.len):
            properties.append(location)
        else:
            answer=location
            print(location)
    return ansewer
    """

    def solution(priorities, location):
    answer = 0

    array1 = [c for c in range(len(priorities))] # index 위치 
    array2 = priorities.copy() # 값 저장 (출력되는 값)

    i = 0
    while True:
        if array2[i] < max(array2[i+1:]):
            array1.append(array1.pop(i))
            array2.append(array2.pop(i))
        else:
            i += 1

        if array2 == sorted(array2, reverse=True):
            break

    return array1.index(location) + 1