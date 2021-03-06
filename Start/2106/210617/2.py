#조이스틱
def solution(name): 
    answer = 0 # A에서부터 위쪽으로 올라갈지, Z에서부터 아래로 내려갈지 최솟값 구하기 
    change = [min(ord(i) - ord('A'), ord('Z') - ord(i) + 1) for i in name] 
    idx = 0 
    while True: answer += change[idx] 
    change[idx] = 0 # 조정된 알파벳은 0으로 변환 
    if sum(change) == 0: return answer # 좌우 이동방향 정하기 
    left, right = 1, 1 
    while change[idx - left] == 0: left += 1 
    while change[idx + right] == 0: right += 1 # 위치(인덱스) 조정 
    answer += left if left < right else right 
    idx += -left if left < right else right
##아직 100프로 이해 못함
#1. 알파벳 위치보고 위로 갈지 아래로갈지 결정
#2. 첫 알파벳 종료후 다음알파벳이 A이면 왼쪽으로 1번 이동
#3. 3번째부터는 무조건 오른쪽으로 이동1번 

def solution(name):
    answer = 0
    min_move = len(name) - 1
    next = 0
    
    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        
        min_move = min(min_move, i + i + len(name) - next)
    answer += min_move
    return answer