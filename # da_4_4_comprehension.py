import random


a0 = [random.randrange(100) for _ in range(10)]
a1 = [random.randrange(100) for _ in range(10)]
a2 = [random.randrange(100) for _ in range(10)]

a = [a0, a1, a2]
print(a)

# 퀴즈
# 2차원 리스트를 1차원으로 만드세요.
b=[]
for i in a:
    for j in i:
        b.append(j)
        print(j,end=' ')
    print()

print(b)





print([j for i in a for j in i])

# 퀴즈
# 2차원 리스트에서 가장 큰 값
print(max([j for i in a for j in i]))

print('-'*30)

