import requests
from lxml import etree

url = "https://www.zbj.com/fw/?k=saas"
resp = requests.get(url)
result = resp.text

html = etree.HTML(result)
# //*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]
# //*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div[2]
divs = html.xpath('//*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div')
for div in divs:
    # 注意这里是使用相对路径./                  
    price = div.xpath('./div/div[3]/div[1]/span/text()')[0].replace("¥", "")
    print(price)
    name = 'saas'.join(div.xpath('./div/div[3]/div[2]/div/span/text()'))
    # print(name)
                          
    com_name = div.xpath('./div/div[5]/div/div/div/text()')[0]
    # print(com_name)
    # addr = div.xpath('')
