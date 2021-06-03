#DoIt p86~
# 1. 배열의 원소를 역순으로 정렬하는 알고리즘

from typing import MutableSequence


def reverse_array(a: MutableSequence) -> None:
    n=len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]

# 2. 리스트를 역순으로 정렬 list의 reverse()함수를 사용
# x.reverse()

# 3. 역순으로 정렬한 리스트 생성
 y=list(reversed(x))

 # 4. ㅜ

