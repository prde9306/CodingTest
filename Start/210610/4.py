# 데이터를 넣는 enque()함수

def enque(self, x:Any)-> None:
    """데이터 X를 인큐"""
    if self.is_full():
        raise FixedQueue.Full #큐가 가득 차 있는 경우 예외 처리 
    self.que[self.rear] = x
    self.rear +=1
    self.no +=1
    if self.rear ==self.capacity:
        self.rear = 0

def deque(self) -> Any:
    """데이터를 디큐"""
    if self.is_empty():
        raise FixedQueue.Empty
    x= self.que[self.front]
    self.front +=1
    self.no -=1
    if self.front == self.capacity:
        self.front=0
    return x
    