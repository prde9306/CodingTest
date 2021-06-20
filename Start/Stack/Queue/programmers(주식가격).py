#주식가격 문제
# 1.가격이 떨어지지 않는 기간은 몇 초?

def solution(prices):
    pirces = [0] * len(prices)
    sec = 0
    total =[]

    while prices:
        for i in range len(prices):
            if (prices[0]<=prices[i]):
                sec +=1
            else:
                total.append(sec)
                prices.pop(0)
    return sec


def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    sec = 0
    while bridge :
        bridge.pop(0)
        sec += 1
        if truck_weights :
            if (sum(bridge) + truck_weights[0]) <= weight :
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return sec