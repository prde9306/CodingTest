# #코드업 6052
# a =int(input())
# print(bool(a))

# #코드업 6053
# a = bool(int(input()))
# print(not a)

# #코드업 6054
# a,b= input().split()
# print(bool(int(a)),bool(int(b)))

# #코드업 6055
# a,b = input().split()
# print(bool(int(a)) or bool(int(b)))

#코드업 6056
a,b = input().split()
print(bool(int(a)) != bool(int(b)))
#이렇게 안되나??
a,b=input().split()
c=bool(int(a))
d=bool(int(b))
print((c and (not d))or ((not c)and d))


