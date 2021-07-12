#!/usr/bin/env python
# encoding: utf-8
"""
@author: liubowen
@contact: 15178940382@163.com
@site: http://www.liubowen.icu/
@file: test_threadpool.py
@time: 2021/7/12 13:46
"""
from concurrent.futures import ThreadPoolExecutor
import time


def spider(page):
    time.sleep(page)
    print(f"craw1 task{page} finished")
    return page


def main():
    with ThreadPoolExecutor(max_workers=5) as t:  # 创建一个最大容量为5的线程池
        task1 = t.submit(spider, 1)
        task2 = t.submit(spider, 2)
        task3 = t.submit(spider, 3)

        print(f"task1: {task1.done()}")  # 通过done来判断线程是否完成
        print(f"task2: {task2.done()}")
        print(f"task3: {task3.done()}")

        time.sleep(2.5)
        print(f"task1: {task1.done()}")
        print(f"task2: {task2.done()}")
        print(f"task3: {task3.done()}")
        print(task1.result())  # 通过result来获取返回值


if __name__ == '__main__':
    main()
