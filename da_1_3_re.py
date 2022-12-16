# da_1_3_re.py


import re

db = '''3412    Bob 123
3834  Jonny 333
1248   Kate 634
1423   Tony 567
2567  Peter 435
3567  Alice 535
1548  Kerry 534'''


print(re.findall('([A-S][a-z]+|[U-Z][a-z]+)',db))