# da_3_3_numpy_matplotlib.py

# 퀴즈
# 텍스트 파일 열어서
# top10  데이터를 막대 그래프로 출력

#f = open("C:\Users\admir\Desktop\python잘해야대\data\2016_GDP.txt",'w')

f = open(r"C:\Users\admir\Desktop\python잘해야대\data\2016_GDP.txt", 'r',encoding='utf-8')
for line in f:
    print(line)
f.close()