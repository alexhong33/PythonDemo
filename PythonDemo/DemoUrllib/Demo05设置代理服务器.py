'''
Created on 2017年6月8日

@author: Alex
'''

#建立一个自定义函数 用于实现使用代理服务器来爬取某个URL网页的功能
def use_proxy(proxy_address, url):
    
    import urllib.request
    #设置代理服务器的信息  式为({'http':代理服务器地址})
    proxy = urllib.request.ProxyHandler({'http':proxy_address})
    #创建一个自定义的opener对象 第一个对象为代理信息, 第二个对象为urllib.request.HTTPHandler类
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    #安装opener对象
    urllib.request.install_opener(opener)
    #调用urlopen
    data = urllib.request.urlopen(url).read()
    return data

proxy_address = "218.18.232.59:8080"
data = use_proxy(proxy_address, "http://www.baidu.com")
print(len(data))