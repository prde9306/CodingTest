#소수 알고리즘 개선 2번째
# n의 제곱근 이하의 어떤 소수로도 나누어 떨어지지 않는다. 
counter =0 # 곱셈과 나눗셈을 합한 횟수
ptr =0 # 이미 찾은 소수의 개수
prime = [None] * 500
prime[ptr] = 2 # 2는 소수
ptr +=1
prime[ptr] = 3 # 3은 소수
ptr +=1

for n in range(5, 1001, 2):
    i=1
    while prime[i]*prime[i]<=n:
        counter +=2
        if n % prime[i] ==0:
            break
        i +=1
    else
    prime[ptr]=n
    ptr+=1
    counter += 1

for i in range(ptr):
    print(print[i])
print(f'곱셈과 나눗셈을 실행한 횟수:{counter}')
