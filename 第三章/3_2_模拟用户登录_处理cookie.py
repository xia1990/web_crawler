# 登录->得到cookie
# 带着cookie去请求书架url->书架上的内容
# 必须得把上面的两个操作连起来
# 我们可以使用session进行请求->session你可以认为是一连串的请求，在这个过程中的cookie不会丢失。

import requests
import json

session = requests.session()
# url = "https://passport.17k.com/login/"
# url = "https://api.17k.com/pv/log.php?Platform=Web&Guid=1094c899-0474-41ad-b7d6-a1eec6a709b6&Uid=104340037&Nickname=primary_90&cpsSource=0&Channel=web&callback=Q_jsonp_848266"
# data = {
#     "loginName":"18016074089",
#     "password":"gyx@624526"
# }
# headers = {
#     "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
#     "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
#     "accept-encoding":"gzip, deflate, br, zstd",
#     "accept-language":"zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
#     "connection":"keep-alive",
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Origin': 'https://passport.17k.com',
#     'Referer': 'https://passport.17k.com/login/'
# }
# resp = session.post(url, headers = headers, data = data)
# print(resp.text)

# 得到17K小说，我的书架中的内容
url = "https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919"
resp = requests.get(url, headers = {
    "cookie":"GUID=1094c899-0474-41ad-b7d6-a1eec6a709b6; c_channel=0; c_csc=web; Hm_lvt_9793f42b498361373512340937deb2a0=1760948527,1761032018; HMACCOUNT=B2459451283CDC76; acw_sc__v2=68f74ca804d5c73cf1874f6e484637fbbc94bbe3; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F17%252F37%252F00%252F104340037.jpg-88x88%253Fv%253D1760948689000%26id%3D104340037%26nickname%3Dprimary_90%26e%3D1776589895%26s%3Ddff9cc3fe15bc13e; tfstk=gzgrQgbtxULP6SBXPxUF_DorMuU8RyJ6U2wQtXc3N82uR3e3KXHYOwG3qtvU3ve7VzDIL9kSh8DE9QF3KvDUd0tX5bh8JyvsLFTswzFeWugz-9G0yWTwd1jy5bhRitp1_T81T_02H82nKuq0i5ecKyq3xIy0T5IhEv4HgIP39_VuxWYcn5Pz-JD3-Il0HW43Zv4Hgj2YtAtQKR_4_uAjGR44kUKuDRcu3wbN67roCFeV-eg4abeiZsbh-qPz2qYVmK98VDcTX4GB8ZUS_m40T2dGYJrZx4amrKYgDkmnfkofEQMiLjDLPqAhqRmSFr0ob6bngzynQqqGUKyiyj0TooTM_j0xFb3qO6Y3GAwmw44eSCUzr844M29ArJomx4Z8JTvUpqlmrDSrA9F0NV3K49jUqSF4CIRVkfk8iEH5LXsdvunYgROJwMILqSF4CIRVvME8kSy6wQC..; BAIDU_SSP_lcr=https://www.baidu.com/link?url=3BWNYE-thUg4K03QKLlLhWCBVZ_jB3PXX-bAR03mQz_&wd=&eqid=e5544079000655440000000668f750b0; ssxmod_itna=eqAx0DcDujG=GQGCDzZDU7jXgDCTk0ioRBODDv5PUKtD/KiIDnqD=GFDK40EEk+TKfW4r4eU3U3I+KUtcGDQ5U8egAxH45Qx0aDbqGk39C84GG9xBYDQxAYDGDDPDoxKD1D3qDkD7g1ZlndtDm4GW/qDgl4GgYliD04XybqrD4qDBf2dDKkrgQDDlQ7Wq+0Q4+BiDYRde2kTMWicxKB=DjkrD/4hC=B6dcpHqlTaOE6iHbqGyWKGunTRS9n4gDCX4LYf5Y74hzAjwKixW+BDIBFhn5Xx9MiArCyGfzDh69bLUxD32LGqxD==; ssxmod_itna2=eqAx0DcDujG=GQGCDzZDU7jXgDCTk0ioRBODDv5PUKG98w8SDBdbgx7pxmYl78D6QGxtGeYBk0jCYaA79DCgWi7OvCDrnrv+K=IoQ341=z4j5uXKp+uo7PBQnt7UANmDKkW4rD5aUkRovovn4Dw1TeaP+tKCDt1DH+dKaYNKEt5D08DYIx4D; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22104340037%22%2C%22%24device_id%22%3A%2219a00b6212bbfa-02e93f82e2140e8-26061851-1327104-19a00b6212c683%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221094c899-0474-41ad-b7d6-a1eec6a709b6%22%7D; Hm_lpvt_9793f42b498361373512340937deb2a0=1761039064"
})
resp.encoding = "utf-8"
data = resp.json()
books = data.get("data")
for book in books:
    print("~"*100)
    print("书名：",book.get("bookName"))
    print("简介：", book.get("introduction"))
