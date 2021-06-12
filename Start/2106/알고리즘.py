
# print('세 정수의 최대값을 구합니다.')
# a = int(input('정수 a의 값을 입력하세요.: '))
# b = int(input('정수 b의 값을 입력하세요. : '))
# c = int(input('정수 c의 값을 입력하세요. : '))

# maximum = a
# if b>maximum: maximum = b
# if c>maximum: maximum = c
# print(f'최대값은 {maximum}입니다.')

n= int(input('몇 개를 출력할까요?: '))
for _ in range(1, n//2 +1):
    print('+-', end='')
