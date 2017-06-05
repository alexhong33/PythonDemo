'''
Created on 2017年6月5日

@author: Alex
'''


import re
import urllib.request


def spider(url, page):
    headers = ("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0")
    print("Start")
    #读取页面的全部源代码
    html1 = urllib.request.urlopen(url).read()
    html1 = str(html1)
    #使用正则表达式 过滤信息
    pat1 = '<div id="plist".+? <div class="page clearfix">'
    result1 = re.compile(pat1).findall(html1)
    result1 = result1[0] 
    #使用正则表达式 第二次 过滤信息 提取图片
    pat2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)">'
    imagelist = re.compile(pat2).findall(result1)



    x = 1
    for imageurl in imagelist(range(10)):
        print("-"*10)
        print(imageurl)
        print("-"*10)
        
        
'''
        #图片储存位置
        imagename = "F:/SpiderPic" + str(page) + str(x) +".jpg"
        imageurl = "https://" + imageurl
        #避免程序中途异常崩溃, 建立异常处理, 若不能爬取到某个图片, 则通过x+=1自动跳到下一个图片
        try:
            #储存图片到本地
            urllib.request.urlretrieve(imageurl, filename=imagename)
        except urllib.error.URLError as e:
            if hasattr(e, "code"):
                x+=1
            if hasattr(e, "reason"):
                x+=1
            x+=1

'''

#抓取10个页面   
for i in range(1, 2):
    print("正在抓取第%d页的图片" % i)
    url = "https://list.jd.com/list.html?cat=9987,653,655&page=" + str(i)
    spider(url, i)
    print("完成第%d页的图片抓取/" % i )
            
  
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        