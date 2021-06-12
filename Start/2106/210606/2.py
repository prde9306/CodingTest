# 복잡도 = 알고리즘의 성능을 평가하는 객관적 기준
# 1. 시간 복잡도 : 실행하는 데 필요한 시간을 평가
# 2. 공간 복잡도 : 메모리(기억공간)와 파일 공간이 얼마나 필요한지 평가

# 선형검색의 시간 복잡도

from typing import Sequence


def seq_search(a:Sequence, key:Any)-> int:
    i = 0
    while i< n:
        if a[i] == key:
            return i
        i += 1

    return -1

# 이진 검색의 시간 복잡도
