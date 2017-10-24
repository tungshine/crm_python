from django.test import TestCase

# Create your tests here.


import MySQLdb
import time


def test():
    conn = MySQLdb.connect(user='root', db='py_crm', passwd='system', host='192.168.1.7')
    cursor = conn.cursor()
    cursor.execute("select * from py_crm.crm_user")
    results = cursor.fetchall()
    print(results)


# test()


def test2():
    print(time.time())
    struct_time = time.localtime(time.time())  # 获取本地结构化时间
    print(struct_time)
    print(time.localtime())
    print(time.strftime('%Y-%m-%d %H:%M:%S', struct_time))  # 自定义时间格式


# test2()


print('ssss'.strip('-'))