from typing import Any


def push(self, value : Any) -> None:
    """스택에 value를 푸시(데이터를 넣음)"""
    if self.is_full():
        raise FixedStack.Full
    self.stk[self.ptr] = value
    self.ptr +=1

def pop(self) -> Any:
    """스택에서 데이터를 팝(꼭대기 데이터를 꺼냄)"""
    if self.is_empty():
        raise FixedStack.Empty
    self.ptr -=1
    return self.stk[self.ptr]

def peek(self) -> Any:
    """스택에서 데이터를 피크(꼭대기 데이터를 들여다 봄)"""
    if self.is_empty(): #스택이 비어있음
        raise FixedStack.Empty
    return self.stk[self.ptr -1 ]

def clear(self) -> None:
    """스택을 비움(모든 데이터를 삭제)"""
    self.ptr=0



