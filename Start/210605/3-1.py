#for 문으로 작성한 선형 검색 알고리즘
from typing import Sequence


def seq_search(a:Sequence, key: Any) -> int:
    for i in range(len(a)):
        if a[i] == key:
            return i
        return -1

#보초법을 통해 판단 횟수 절반으로 줄이기 

# 이진 탐색
