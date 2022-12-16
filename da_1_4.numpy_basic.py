# da_1_4.numpy_basic.py

import numpy as np

d = np.random.randint(0, 100, 12, dtype=np.int32).reshape(3,4)
print(d)
print(d.dtype)

# 2차원 배열을 1차원으로 변환하세요 (3가지)

#1
d = d.reshape(1,12)

print(d)

#2
print(d.reshape(d.size))
