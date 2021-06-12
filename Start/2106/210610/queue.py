def peek(self) -> Any:
    """큐에서 데이터를 피크(맨 앞 데이터를 들여다 봄)"""
    if self.is_empty():
        raise FixedQueue.Empty # 큐가 비어 있는 경우 예외 처리를 발생
    return self.que[self.front]

def find(self, value: Any) -> Any:
    """큐에서 value를 찾아 인덱스를 반환(없으면 -1을 반환)"""
    for i in range(self.no):
        idx = (i+self.front) % self.capacity
        if self.que[idx] == value: #검색 성공
            return idx
    return -1 # 검색 실패

def count(self, value: Any) -> bool:
    """큐에 있는 value의 개수를 반환"""
    c=0
    for i in range(self.no): # 큐 데이터를 선형 검색
        idx = (i + self.front) % self.capacity
        if self.que[idx] == value: # 검색 성공
            c+=1 #들어 있음
    return c

def __contains__(self, value: Any)-> bool:
    """큐에 value가 있는지 판단"""
    return self.count(value)

def clear(self)-> None:
    """큐의 모든 데이터를 비움"""
    self.no = self.front = self.rear =0

def dump(self) -> None:
    """모든 데이터를 맨 앞부터 맨 끝순으로 출력"""
    if self.is_empty(): # 큐가 비어 있음
        print('큐가 비었습니다.')
    else:
        for i in range(self.no):
            print(self.que[(i + self.front) % self.capacity], end="")
            print()


            

