# da_2_2_json.py
import json
import requests

a = {"ip": "8.8.8.8"}
print(a)

b = json.dumps(a)
print(b, type(b))

# 퀴즈
# 문자열 b로 부터 딕셔너리를 추출하세요.

c= json.loads(b)
print(c, type(c))
# 내부적으로 어떻게 바뀌는지는 알빠 아님.

# 퀴즈
# 아래의 json 문자열로부터 값만 출력하세요
d = '''{
"time": "03:53:25 AM",
   "milliseconds_since_epoch": 1362196405309,
   "date": "03-02-2013"
}'''
'''
e = json.loads(d)
print(type(e))
print(e.values())
# 가끔 가다 반복문을 써야할  때,

for k in e:
    print(e[k], end='   ')
'''
# 진짜 퀴즈

print('-'*30)
#url = 'https://www.naver.com/'
url = 'http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'

response = requests.get(url)
print(response)
print(response.content)

text = response.content.decode('utf-8')     # euc-kr 추세는 utf-8
print(text)


# 퀴즈
# 기상청 데이터로부터 코드와 지역 이름을 깨끗하게 출력하세요.

print(type(text))

lst = json.loads(text)

for a in lst:
    print(a["value"], a["code"])



