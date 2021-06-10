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
    ㅊ
            

