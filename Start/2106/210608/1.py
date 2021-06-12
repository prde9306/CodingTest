class FixedStack:
    """고정길이 스택 클래스"""
    class Empty(Exception):
        """비어 있는 FixedStack에 팝 도는 피크할 때 내보내는 예외 처리"""
    class Full(Exception):
        pass
    def __init__(self, capacity: int = 256) -> None:
        """스택 초기화 """
        self.stk = [None] * capacity # 스택 본체
        self.capacity = capacity # 스택의 크기
        self.ptr = 0 # 스택 포인터

    def __len__(self) -> int:
        """스택에 쌓여 잇는 데이터 개수를 반환 """
        return self.ptr
    
    def is_empty(self) -> bool:
        """스택이 비어 있는지 판단 """
        return self.ptr<=0
    
    def is_full(self_)-> bool:
        """스택이 가득 차 있는지 판단"""
        return self.ptr >=self.capacity
