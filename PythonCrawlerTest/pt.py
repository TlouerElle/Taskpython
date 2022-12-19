#!/usr/bin/python3.6
# -*- coding:utf-8 -*-
# @Time :2021/12/24 14:25
# @Author : haitao
# @Email : zhangsan@163.com


'''
Target
   1、网页状态码
   2、防反爬策略
   3、多线程、多进程
   4、selenium


'''
from functools import wraps

import requests
import time
import random
import threading # 多线程
from multiprocessing import Process,Pool
import numpy
from selenium import webdriver

# 装饰器
def staticTime(f):
    @wraps(f)
    def myCrawler(*args):
        start = time.time()
        f(*args)
        end = time.time()
        print("spend time is %s"%(end - start))
    return myCrawler

@staticTime
def crawler(urls):
    '''
    1XX:服务器收到用户请求，但是请求参数不完善，不够，还需要进一步操作！
    101：
    102
    
    2XX：向服务器发起请求，同时服务器成功处理了你的请求
    200：
    201：成功处理你的 请求，但同时创建新的资源，
    202：服务器收到你的请求，但是尚未处理
    
    3XX：请求重定向，
    301：永久移动
    302：临时移动
    
    
    4XX:请求错误（用户的错）
    400：http:sdafdsafasdfdsfsdfdsfdsf,语法出错
    404：找不到用户请求的网页，
    403：服务器拒绝你的请求
    
    5XX：服务器内部出错
    503：服务器不可用（DDos）
    
    
    防反爬策略：
    1、header，伪装用户角色
    2、cookies,携带用户信息
    3、proxies,设置代理
    4、time，增加随机时间间隔
    5、selenium自动测试工具，
    
    Python
    多进程：multiprocessing
    多线程：multithreading
    
    '''
    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
               "Connection":"keep-alive",
               "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
    cookies_str = "bid=j2l0N89H; sajssdk_2015_cross_new_user=1; __gads=ID=987f28da872e930a-22588f7886cf00b4:T=1640308743:RT=1640308743:S=ALNI_Ma5CjmN_m3EbGyI-NqqocJyL8jwcA; BAIDU_SSP_lcr=https://www.baidu.com/link?url=IF78fy8-kYxHosS5s9vE_pDSRbcw3izDswX7Q70Cub-7INlkYSXKt_7btsLlAT0J&wd=&eqid=d71b2d40000582570000000661c56fc6; Hm_lvt_ecd4feb5c351cc02583045a5813b5142=1640308743,1640329160; __utma=177678124.511816119.1640308743.1640308743.1640329160.2; __utmc=177678124; __utmz=177678124.1640329160.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217dea051b712b7-0f6db409c0a0ec-3e644204-2073600-17dea051b72bf2%22%2C%22%24device_id%22%3A%2217dea051b712b7-0f6db409c0a0ec-3e644204-2073600-17dea051b72bf2%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; __utmb=177678124.5.10.1640329160; Hm_lpvt_ecd4feb5c351cc02583045a5813b5142=1640329189"
    cookies = {}
    [cookies.update({st.split("=",1)[0]:st.split("=",1)[1]}) for st in cookies_str.split(";")]
    proxies = {
        "HTTP": "113.119.47.199",
        "HTTP": "111.3.118.247",
        "HTTP": "183.157.168.223",
        "HTTP": "113.119.47.199",
        "HTTP": "113.119.47.199",
        "HTTP": "183.157.168.223",
        "HTTP": "113.119.47.199",
        "HTTP": "113.119.47.199",
        "HTTP": "223.241.77.241",
        "HTTP": "113.119.47.199",
        "HTTP": "119.180.133.43",
        "HTTP": "117.34.25.11",
        "HTTP": "182.84.145.206",
        "HTTP": "60.250.159.191",
        "HTTP": "110.189.152.86",
    }
    for url in urls:
        time.sleep(random.randint(1,11)*0.1)
        res = requests.get(url, timeout=5,headers=headers,cookies=cookies,proxies = proxies)
        if res.status_code == 200:
            print("success!!!")


if __name__ == '__main__':
    # urls = ["https://www.xiachufang.com/category/40076/?page={}".format(i) for i in range(1,26)]
    # urls_avg = numpy.array_split(urls,4)

    # for i in range(len(urls_avg)):
    #     t = threading.Thread(target=crawler,args=(urls_avg[i],))
    #     t.start()

    # shops = Pool(processes=len(urls_avg)) # 进程池
    # for i in range(len(urls_avg)):
    #     shops.apply_async(crawler,args=(urls_avg[i],))
    # shops.close()
    # shops.join()# 上面没有执行完，后面不允许申请新的进程





    # crawler(urls)
    # t1 = threading.Thread(target=crawler,args=(urls[0:5],))
    # t2 = threading.Thread(target=crawler, args=(urls[5:10],))
    # t1.start()
    # t2.start()
    # print((1,))
    ch = webdriver.Chrome("chromedriver.exe")
    ch.get("https://www.baidu.com/")
    time.sleep(1)
    ch.refresh()
    time.sleep(1)
    ch.back()
    time.sleep(1)
    ch.forward()
    content = ch.find_element_by_xpath('//*[@id="hotsearch-content-wrapper"]/li[1]/a')
    print(content.text)
    th = ch.find_element_by_xpath('//*[@id="auto-id-1640332495228"]').send_keys("用")
    bt = ch.find_element_by_xpath('//*[@id="su"]').click()


