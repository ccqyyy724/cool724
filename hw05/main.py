import re
str="我的邮箱是tom@qq.com。你可以发送到邮箱jerry123@qq.com.或者3123432@qq.com。这是我的电话182123445678"
print(re.findall('[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+',str))
print(re.findall('[0-9]+',str))
