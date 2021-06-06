# 소수 구하는 알고리즘 성능 향상

counter = 0 #나눗셈 횟수를 카운트
ptr = 0 # 이미 찾은 소수의 개수
prime = [None] * 500 #소수를 저장하는 배열

prime[ptr]=2 #2는 소수이므로 초깃값으로 지정
ptr +=1

for n in range(3, 1001, 2):
    for i in range(1, ptr):
        counter += 1
        if n % prime[i]==0:
            break
        else:
            prime[ptr] = n
            ptr +=1

for i in range(ptr):
    print(prime[i])
print(f' 나눗셈을 실행한 횟수:{counter}')