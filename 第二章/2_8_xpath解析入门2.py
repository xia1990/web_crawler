from lxml import etree

tree = etree.parse("a.html")
# 这里html前面的/不可以省略
# ret = tree.xpath("/html/body/ul/li/a/text()")
# xpath 从1开始，
# ret = tree.xpath("/html/body/ul/li[1]/a/text()")
# ret = tree.xpath("/html/body/ol/li[2]/a/text()")
# 得到大炮的值
# ret = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")
ol_li_list = tree.xpath("/html/body/ol/li")
for li in ol_li_list:
    # 从li查找值，使用相对路径./
    ret = li.xpath("./a/text()")
    print(ret)
    # 拿属性:@href
    ret2 = li.xpath("./a/@href")
    print(ret2)

ret3 = tree.xpath("/html/body/ul/li/a/@href")
print(ret3)

ret4 = tree.xpath("/html/body/div[1]/text()")
print(ret4)

