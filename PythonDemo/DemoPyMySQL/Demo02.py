'''
Created on 2017年6月20日

@author: Admin_lgf
'''

import pymysql

#conn = pymysql.connect(host="localhost", user="root", passwd="admin")
#conn.query("create database QueryWorking")

conn1 = pymysql.connect(host="127.0.0.1",user="root", passwd="admin", db="queryworking")

'''
创建表格

conn1.query("create table mytb(title char(20) not null, keywd char(30))")
'''

'''
插入数据

conn1.query("INSERT INTO mytb(title,keywd) VALUES('first title', 'firstkeywd')")
#必须加上commit()
conn1.commit()
'''

#把数据 输出到控制台

cs=conn1.cursor()
cs.execute("select * from mytb")
for i in cs:
    print("当前是第"+str(cs.rownumber)+"行")
    print("标题是: "+i[0])
    print("关键词是: "+i[1])
