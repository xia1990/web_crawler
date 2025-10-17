import re

# lst = re.findall(r"\d+","我的电话号码是：10086，你的电话号码是：10010")
# print(lst)

# # finditer 返回的是迭代器，从迭代器中拿到内容使用.group
# it = re.finditer(r"\d+","我的电话号码是：10086，你的电话号码是：10010")
# for i in it:
#     print(i.group())

# # search 返回的是 match 对象，拿到内容使用.group
# a = re.search(r"\d+","我的电话号码是：10086，你的电话号码是：10010")
# print(a.group())

# match是从头匹配
# b = re.match(r"\d+","10086，你的电话号码是：10010")
# print(b.group())

# obj = re.compile(r'\d+')
# ret = obj.finditer("我的电话号码是：10086，你的电话号码是：10010")
# for it in ret:
#     print(it.group())

# ret1 = obj.findall("呵呵可，我就不信你：111000000000000")
# print(ret1)

s = """
<div class="jay"><span id="1">张三</span></div>
<div class="jj"><span id="2">李四</span></div>
<div class="jolin"><span id="3">王五</span></div>
<div class="sayor"><span id="4">赵六</span></div>
<div class="toary"><span id="5">李七</span></div>
"""
# (?P<分组名称>正则) 可以单独从正则匹配到的内容中进一步提取到内容
obj = re.compile(r'<div class=".*?"><span id="(?P<id>\d+)">(?P<name>.*?)</span></div>', re.S)
result = obj.finditer(s)
for it in result:
    print(it.group("name"))
    print(it.group("id"))