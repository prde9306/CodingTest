# 프로그래머스 스택, 큐
# 다리를 지나가는 트럭

# 문제 : 최소 몇 초가 걸리나?
# 최대 올라갈 수 있는 대수 bridge_length
# 견딜 수 있는 무게 weight

# 건너는데 1초에 1미터 

#길이를 기준으로 초도 늘리면서,
# #트럭 총 대수 
# len(truck_weights)


# if(truck_weights[i] 다 더한 값이 >=weight):
#     중단

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

#스택, 큐 문제만 몰아서 풀고 이런식으로 풀어## 최대한 빨리 실력 느는 방법
#나동빈이 말한 유형 먼저
