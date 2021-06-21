#프로그래머스 프린터 문제

#sol1

from collections import deque 
def solution(priorities, location): 
    queue = deque(priorities) 
    counter = 0 
    while queue: 
        max_priority = max(queue) 
        priority = queue.popleft() 
        
        if priority == max_priority: 
            counter += 1 
            if location == 0: 
                break 
            else: 
                location -= 1 
        else: 
            queue.append(priority)
            if location == 0:
                location = len(queue) - 1 
            else: 
                location -= 1 
    return counter 
    
if __name__ == '__main__': assert solution([2, 1, 3, 2], 2) == 1


#sol2

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
