'''
Created on 2017年6月1日

@author: Alex
'''


from urllib import request


with request.urlopen('http://www.qdaily.com/') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' %(k, v))
    print('Data:', data.decode('utf-8'))
