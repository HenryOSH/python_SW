    # da_3_7_re_weather.py
import re
import requests
import pandas as pd

f = open('data/weather.csv','w', encoding='utf-8')

url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stdId=184'

# 퀴즈
# province 태그 안쪽의 데이터만 출력하세요
response = requests.get(url)
# # print(response.text)
#
# print(re.findall(r'<province>(.+)</province>', response.text))
# print(re.findall(r'<city>(.+)</city>', response.text))

# 퀴즈
# location 태그를 가져오세요
# DOTALL: 찾으려는 대상이 여러 줄에 걸쳐 있을 때
# .+ : 욕심이 많다(greedy) 가장 긴 패턴 검색
# .+?: 욕심이 없다(non-greedy) 가장 짧은 패턴 검색
locations = re.findall(r'<location wl_ver="3">(.+?)</location>', response.text, re.DOTALL)
# print(locations)
# print(len(locations))

# 퀴즈
# location 안쪽에 있는 province 태그를 가져오세요
for loc in locations:
    prov = re.findall(r'<province>(.+)</province>', loc)
    city = re.findall(r'<city>(.+)</city>', loc)
    print(prov[0], city[0])

print('-'*50)

# 퀴즈
# prov와 city를 findall 1회만 사용해서 해결하세요.



# 퀴즈
# data 태그를 가져오세요
data = re.findall(r'<data>(.+?)</data>', loc, re.DOTALL)
# print(len(data))



# 퀴즈
# mode, tmEf, wf, tmn, tmx, rnSt 태그를 가져오세요
for datum in data:
    mode = re.findall(r'<mode>(.+)</mode>', datum)
    tmEf = re.findall(r'<tmEf>(.+)</tmEf>', datum)
    wf = re.findall(r'<wf>(.+)</wf>', datum)
    tmn = re.findall(r'<tmn>(.+)</tmn>', datum)
    tmx = re.findall(r'<tmx>(.+)</tmx>', datum)
    rnSt = re.findall(r'<rnSt>(.+)</rnSt>', datum)

    print(mode[0], tmEf[0], wf[0], tmn[0], tmx[0], rnSt[0], file=f, sep=',')


#
# <tmEf>2022-12-20 12:00</tmEf>
# <wf>흐림</wf>
# <tmn>-5</tmn>
# <tmx>4</tmx>
# <reliability/>
# <rnSt>40</rnSt>

f.close()

print('-'*50)
# 퀴즈
# 기상청에서 가져온 데이터를 weather.csv 파일로 저장하세요 (data 폴더에)



dt = pd.DataFrame(data)





