#da_1_2_list.py

import random

#퀴즈
#0~99 사이의 정수 난수 10개로 이루어진 리스트를 만드세요.

random.seed(23)

a = []

for _ in range(10):
    a.append(random.randrange(100))

print(a)

b = []

for i in range(10):
    b.append(a[9-i])

print(b)

for i in range(5):
    b[i], b[-1-i] = b[-1-i], b[i]  #파이썬 스왑 잴 중요!!

