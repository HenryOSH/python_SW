# da_2_1_numpy_basic.py

import numpy as np


a = np.arange(3)
b = np.arange(6)
c = np.arange(3).reshape(1, 3)
d = np.arange(3).reshape(3, 1)
e = np.arange(6).reshape(2, 3)

#print(b+c)
#print(d+e)


print('-'*30)
np.random.seed(23)
f = np.random.randint(0,100,12)
print(f)

g = (f>=50)
print(g)
print(f[g])


#h = np.reshape(f,3,4)
h = f.reshape(3,4)
print('-'*30)
print(h)

# 퀴즈 2차원 배열에서 처믕과 마지막 요소를 출력하세요.
print(h[0][0])
print(h[-1][-1]) # fancy indexing  이라고 부름

for i in range(3):
    print(h[i,-1])

print(h[:,-1])
print('-'*30)
#퀴즈
#2차원 배열을 거꾸로 출력하세요
print(h[::-1],end='\n\n')
print(h[:,::-1],end='\n\n')
print(h[::-1,::-1],end='\n\n')





