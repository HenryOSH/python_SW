# da_3_1_loop

# 출력하기

# *
# **
# ***
# ****

# print('*'* i for i in range(4))

#for i in range(4):
# print('*'*(i+1) for i in range(5))

for i in range(4-1, -1, -1):
    for j in range(4):
        if i>= j:
            print('*', end='')
        else:
            print('-', end='')
    print()
print()





