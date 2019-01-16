#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

headers = {'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive',
           'Cookie': 'JSESSIONID=E22E1DC798558630B993D7D50E9586DA', 'Host': 'weixin.mwr.gov.cn', 'Pragma': 'no-cache', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

address = 'http://weixin.mwr.gov.cn/pub/poll/201812/p14410.html'

votesAddr = 'http://weixin.mwr.gov.cn/poll/poll/poll_skim_dowith.jsp?PollId=144&Item_707=3292&Item_707=3292&Item_707=3292&Item_707=3292&Item_707=3292&Item_707=3292&Item_707=3292&Item_707=3292&Item_707=3292&Item_707=3292&txtVerifyCode='

def func():
    r=requests.get(url=address,headers=headers)
    rcookies = r.cookies
    print(rcookies.get_dict())
    soup = BeautifulSoup(r.text,'html.parser')
    imgSrc = soup.find('img').get('src')
    verifyCode = requests.get(imgSrc,headers=headers)
    rcookies = verifyCode.cookies
    print(rcookies.get_dict())
    im = Image.open(BytesIO(verifyCode.content))
    im.save('verifyCode.jpeg', 'jpeg')
    code = input('验证码是：')
    votes = requests.get(votesAddr+code,headers = headers, cookies = rcookies)
    print(votes.text)





if __name__ == '__main__':
    func()
