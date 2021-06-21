#다리를 지나는 트럭

#모범답안

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

#핵심(암기)
# bridge = [0] * bridge_length 이렇게 해서 pop해서 꺼내면서 따지는 방법
# while bridge - 배열 비면 false돼서 나옴 