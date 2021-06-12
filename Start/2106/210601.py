# print('*를 출력합니다.')
# n=int(input('몇 개를 출력할까요?'))
# w=int(input('몇 개마다 줄바꿈할까요?:'))

# for _ in range(n//w):
#     print('*'* w)

# rest =n % w
# if rest:
#     print('*' *rest)


# print('1부터 n까지 정수의 합을 구합니다. ')

# while True:
#     n=int(input('n값을 입력하세요.:'))
#     if n>0:
#         break

#최댓값 구하는 함수
from typing import Any, Sequence


def max_of(a:Sequence)-> Any:
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum