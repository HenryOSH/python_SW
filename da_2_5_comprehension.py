# da_2_5_comprehension.py

import random

# 컴프리핸션 : 한줄 짜리 반복문

# 컴프리핸션 : (함수에 사용할) 리스트를 만드는 !! 한 줄짜리 반복문

a=[]
for i in range(5):
    print(i)
    a.append(i)


print(a)

print('-'*30)
b = [i for i in range(5)]
print(b)

# 퀴즈
# 컴프리핸션을 사용해서 난수 10개가 들어있는 리스트를 만드세요.
random.seed(23)
c = [random.randrange(100) for i in range(10)]
print(c)

# 퀴즈
# 1차원 리스트로부터 홀수만 추출 하세요.

for i in c:
    if i % 2:
        print(i)


print([i for i in c if i % 2])  #와우
print('-'*30)
# 퀴즈
# 다음 문자열에 포함된 모음의 개수를 세어 보세요.

t = 'hello, world'
s = 'aeiou'
cnt = 0
print(type(t))
for i in t:
    if i in s:
        cnt += 1

print(cnt)
print('-'*30)
print([ch for ch in t])

print(sum([ch in 'aeiou' for ch in t ]))







