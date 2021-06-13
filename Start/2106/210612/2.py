# 정렬 알고리즘
# 정렬 알고리즘의 핵심은 교환, 선택, 삽입이다. 
# 버블 정렬 알고리즘
from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        for j in range(n-1, i-1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
if __name__ == '__main__':
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num #원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'[x{i}]:'))
    bubble_sort(x)

    print('오름차순으로 정렬했ㅅ브니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

####################################
# 알고리즘 개선 1
def bubble_sort(a: MutableSequence) -> None:
    n=len(a)
    for i in range(n-1):
        exchange = 0
        for j in range(n-1, i-1):
            if a[j-1]>a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                exchng += 1
            if exchng == 0:
                break
# 알고리즘 개선 2
