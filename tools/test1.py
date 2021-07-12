#!/usr/bin/env python
# encoding: utf-8
"""
@author: liubowen
@contact: 15178940382@163.com
@site: http://www.liubowen.icu/
@file: test1.py
@time: 2021/7/9 15:01
"""
from collections import defaultdict

# dict_one_to_more = defaultdict(list)
dict_one_to_more = defaultdict(list)
obj1 = {"key1": ["zhangsan", 1]}
obj2 = {"key2": ["lisi", 2]}
objs = [obj1, obj2]
if __name__ == '__main__':
    # for x in range(10):
    # dict_one_to_more["Key"].append()
    # dict_one_to_more["Key"].append("lisi")
    # print(dict_one_to_more)
    # print(dict_one_to_more.values())
    # name = dict_one_to_more.get("Key")
    # print(name[0], name[1])
    # print(obj2.get("key2")[0])
    for i in objs:
        #print(i)
        for x in i.values():
            for y in x:
                print(y)
