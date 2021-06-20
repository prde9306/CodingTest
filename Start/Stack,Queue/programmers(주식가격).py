#주식가격 문제


#(내풀이)-틀림
def solution(prices):
    pirces = [0] * len(prices)
    total =[]

    while prices:
         sec = 0
         for i in prices:
            if (prices[0]<=prices[i]):
                sec +=1
            else:
                total.append(sec)
                prices.pop(0)
    return total



#정답(답안1)
def solution(prices):
    answer = [] # 결과를 저장할 빈배열 생성
    for i in range(0, len(prices)): # prices의 길이만큼 배열을 생성에 i에 담는다.
        cnt = 0 # 카운트할 변수 초기화
        for j in range(i + 1, len(prices)): # i + 1 번째부터 prices의 길이만큼 배열을 생성하고 j에 담는다.
            if prices[i] <= prices[j]: # prices[j]가 prices[i]보다 크거나 같으면 가격이 떨어지지 않았으므로
                cnt += 1 # cnt 1을 더해준다.
            else: # 주식값이 떨어지는 초도 1초로 포함해야 하기 때문에 cnt+1해준다.
                cnt += 1
                break
        answer.append(cnt) # prices[i]에 prices[j]비교를 모두 끝나면 answer에 cnt를 넣어준다.
    return answer


#정답(모범답안2)
from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        timer = 0
        price = prices.popleft()
        for price_ck in prices:
            timer += 1
            if price_ck < price:
                break
        answer.append(timer)

    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))



##암기(핵심) : 
# 1. 이중포문을 통해서 if prices[i] <= prices[j]: 이렇게 비교할 수 있는지
# 2. https://chaewonkong.github.io/posts/python-deque.html(deque 개념)