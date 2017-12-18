import math
import random
import string

import ProcessPractise

"""
基本类型练习
"""
# height = 1.75
# weight = 60
# name = '杨九日'
# nameArr = ['杨九日', 12, 3, 43, 54]
# tinyNameArr = ['杨九日', 12]
# nameList = ('杨九日', 12, 3, 43, 54)
# dict = {"haha": 1, 1: 2}
#
# bmi = weight/(height*height)
# print('hello python')
# print(name[2:])
# nameArr.append(12)
# nameArr.append(12)
# print(nameArr)
# print(tinyNameArr)
# print(len(nameList))
# print(nameList[0])
#
# print(dict["haha"])
# print(dict[1])
#
# if bmi < 18.5:
#     print('过轻')
# elif bmi < 25:
#     print('正常')
# elif bmi < 28:
#     print('过重')
# elif bmi < 32:
#     print('肥胖')
# else:
#     print('严重肥胖')

"""
运算符练习
"""
# a = 0
# b = 20
# myList = [1, 2, 3, 4, 5, 20]
# # 与
# if a and b:
#     print("a和b and 为真")
# else:
#     print("a和b and 为假")
# # 或
# if a or b:
#     print("a和b or 为真")
#
# if a in myList:
#     print("a在list中")
# else:
#     print("a不在list中")
#
# if b in myList:
#     print("b在list中")
# else:
#     print("b不在list中")
#
# a = 20
# if a is b:
#     print("a和b对象引用相等")
# c = "20"
# d = "20"
# if d is c:
#     print("d和c对象引用相等")

"""
数字练习
"""
# # 表示16进制
# mathA = 0x111
# print(mathA)
# # 表示8进制
# mathB = 0o111
# print(mathB)
#
# mathA = 1/3
# print(mathA)
# print(int(mathA))
#
# # 向上取整
# print(math)
# # 向下取整
# print(1//3)
#
# # 随机数
# print(int(random.random()*10000))
# print(random.choice(range(100, 1000, 10)))
"""
字符串练习
"""
# str1 = "Hello AlexNine"
# str2 = "Hello Olive"
# str3 = "Hello"
#
# # 字符串运算符
# print(str1[2])
# print(str1[2:])
# print(str1[:2])
# print(str1[2:5])
# # 重复输出字符串
# print(str3*3)
#
# if str3 in str1:
#     print("包含字符串")
# str4 = "我我我叫%s,今年%d岁" % ("小强", 10)
# print(str4)
# print(str4.count('我'))

"""
列表
"""
# list1 = ['Google', 'Runoob', 1997, 2000]
# list2 = [1, 2, 3, 4, 5]
# list3 = ["a", "b", "c", "d"]
#
# list1[0] = 'sanploy'
# print(list1[0])
# del list1[0]
# print(list1[0])
#
# for x in list1:
#     print(x)
#     print(x + x)
#
# print(list1[-1])
# listDouble = [["hehe1", "haha1"], ["hehe", "haha"]]
# print(listDouble[0][1])
# print(list3.index("d"))

"""
元组
"""
# tup1 = ("朱", 1, "杨九日", "王小强")
# tup2 = ("朱", 1, "杨九日", "王小强")
# print("tup1的长度为%d" % len(tup1))
# print("tup1[0]:", tup1[0])
# print("tup1[2:5]:", tup1[2:5])
# print("tup1+tup2", tup1+tup2)

"""
字典 map
"""
# dict1 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# dict2 = {123: '2341', 1233: '9102', "365": '3258'}
# print("dict1[0]", dict1["Alice"])
# print("dict2[0]", dict2[123])
# print("dict2[2]", dict2["365"])
# # 添加元素
# dict1["heheda"] = "memeda"
# dict1["memeda"] = "heheda"
# print("dict1[heheda]", dict1["heheda"])
#
#
# del dict1["heheda"]
# # print("dict1[heheda]", dict1["heheda"])
# dict2.clear()
# print("dict2", dict2)
# del dict2
# print("dict2", dict2)

# 模块导入
ProcessPractise.fibonacci(10)
