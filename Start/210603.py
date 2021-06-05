#DoIt p86~
# 1. 배열의 원소를 역순으로 정렬하는 알고리즘

from typing import MutableSequence

"""
def reverse_array(a: MutableSequence) -> None:
    n=len(a)
    for i in range(n//2):
        a[i], a[n-i-1] = a[n-i-1], a[i]
"""
# 2. 리스트를 역순으로 정렬 list의 reverse()함수를 사용
# x.reverse()

# 3. 역순으로 정렬한 리스트 생성
 #y=list(reversed(x))

 # 4. N 진수 구하기 
def card_conv(x: int, r: int) -> str:
    """정수값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열 반환"""
     d=''
     dchar ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

     while x>0:
         d+=dchar[x%r]
         x//=r
     return d[::-1]
# 5 함수 사이에 인수 주고받기(immutable)
def sum_1ton(n):
    """1부터 n까지 정수의 합"""
    s=0
    while n > 0:
        s+= n
        n-= 1
    return s
x = int(input('x의 값을 입력하세요 : '))
print(f'1부터 {x}까지 정수의 합은 {sum_1ton(x)}입니다.')

#5-2) mutable -> list
counter = 0
for n in range(2, 1001):
    for i in range(2, n):
        counter +=1
        if n%i == 0:
            break
    else:
        print(n)
print(f'나눗셈을 실행한 횟수:{counter}')