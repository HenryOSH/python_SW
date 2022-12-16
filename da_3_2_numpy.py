# da_3_2_numpy.py
import numpy as np




a = np.zeros([5, 5],dtype = np.int32)
print(a)
print(a.dtype)

# print(np.ones(6))
# print(np.full(5, -1))

# 퀴즈
# 2차원 배열 a의 테두리를 1로 채우세요.



a[0], a[4], a.T[0], a.T[4] = 1, 1, 1, 1



print(a)

print('-'*30)
# 퀴즈
# 2차원 배열 속을 2로 바꿔보세요

a[1:-1,1:-1] = 2

print(a)

# 퀴즈
# 2차원 배열 a의 대각선을 3으로 채우세요

print('-'*30)

np.fill_diagonal(a,3)

print(a)

print('-'*30)

print(np.random.rand(3,4))
print(np.random.choice(['a','b','c'],5))
print(np.random.choice(range(10),10, replace = False))

b = sorted(set('weekend'))
b = np.array(b)
print(b)

# 퀴즈
# choice 함수를 사용해서 100보다 작은 양수 3행 4열을 만드세요

e = [23, 45, 23, 46, 35, 27, 87]
f = e.argsort()
print(f)
