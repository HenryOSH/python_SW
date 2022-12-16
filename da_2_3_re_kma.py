# da_2_3_re_kma.py
import re
import requests


url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
response = requests.get(url)
text = response.content.decode('utf-8')     # euc-kr 추세는 utf-8
print(text)
print(type(text))
# 퀴즈
# 정규 표현식을 사용해서 이전 파일과 똑같은 형태로 출력해보세요.
print('-'*30)
i = re.findall(r'[0-9]+',text)
j = re.findall(r'[가-힣]+',text)



# for k in range(len(j)):
#     print(i[k], j[k])

# for x, y in zip(i,j):
#     print(x,y)


# codes = re.findall(r'{"code":"([0-9]+)"', text)
# areas = re.findall(r'{"code":"([0-9]+)"', text)
#


codes = re.findall(r'"code":"([0-9]+)","value":"([가-힣]+)"', text)

print(codes)

for code, area in codes:
    print(code, area)