#한 줄에 주어지는 두 정수를 a와 b에 저장하고 

a, b = [int(w) for w in input().split()]
#합을 구하여 answer에 저장하고
answer = a+b

#그 값을 출력한다
print( answer )

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# n을 입력받아보세요 
n = int(intput())

# "Goorm"을 n번 출력하세요 
# 각 문자열 사이는 ", "로 구분되어야 합니다
print(", ".join( ["Goorm"] * n))

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())

arr = []
# 리스트에 원소를 입력받아보세요
for w in input().split():
	t=int(w)
	arr.append(t)

