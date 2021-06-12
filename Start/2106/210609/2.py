def find(self, value: Any) -> Any:
    """스택에서 value를 찾아 인덱스를 반환(없으면 -1을 반환)"""
    for i in range(self.ptr -1, -1, -1): #꼭대기 쪽부터 선형 검색
        if self.stk[i]==value:
            return i
    return -1

def count(self, value: Any) -> int:
    """스택에 있는 value의 개수를 반환"""
    c=0
    for i in range(self.ptr): # 바닥 쪽부터 선형 검색
        if self.stk[i] == value:
            c +=1
        return c
        
def __contains__(self, value: Any) -> bool:
    """스택에 value가 있는지 판단"""
    return self.count(value) > 0

def dump(self) -> None:
    """덤프(스택 안의 모든 데이터를 바닥부터 꼭대기 순으로 출력)"""
    if self.is_empty():
        print('스택이 비어 있습니다.') 
    else:
        print(self.stk[:self.ptr])
