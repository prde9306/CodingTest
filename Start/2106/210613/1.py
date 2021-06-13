#단순 선택 정렬 알고리즘

from typing import MutableSequence


def selection_sort(a: MutableSequence) -> None:
    n=len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]

##단순 삽입 정렬 알고리즘 

def insertion_sort(a:MutableSequence)-> None:
    n=len(a)
    for i in range(1,n):
        j=i
        tmp=a[i]
        while j>0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j-=1
        a[j]=tmp
if __name__ =='__main__':
    print('단순 삽입 정렬을 수행합니다. ')
    num=int(input('원소 수를 입력하세요.:'))
    x=[None] * num
    
    for i in range(num):
        x[i] = int(input(f'x[{i}]'))
    insertion_sort(x)

    print('오름 차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

#이진 삽입 정렬 알고리즘

def binary_insertion_sort(a: MutableSequence) -> None:

    n=len(a)
    for i in range(1,n):
        key = a[i]
        pl = 0
        pr =i-1

        while True:
            pc = (pl + pr) //2
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc+1
            else:
                pr = pc-1
            if pl > pr:
                break

        pd = pc+1 if pl<=pr else pr+1

        for j in range(i, pd, -1):
            a[j] = a[j-1]

        a[pd] = key

if __name__ =="__main__":
    print('이진 삽입 정렬을 수행합니다. ')
    num = int(input('원소 수를 입력하세요.'))
    x = [None] * num
    
    for i in range(num):
        x[i] = int(input(f"x[{i}]:)")

    binary_insertion_sort(x)

    print("오름차순으로 정렬했습니다.")
    for i in range(num):
        print(f"x[{i}] = {x[i]}")