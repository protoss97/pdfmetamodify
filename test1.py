# -*- coding:utf-8 -*-
# Author:Liu Hongliang
import hashlib, time


# strb=hashlib.md5(strb).hexdigest().encode("utf-8")
# strb=hashlib.md5(strb).hexdigest().encode("utf-8")
# print(strb)


class Test:

    def __init__(self, name):
        self.name = name


def calc(str):
    strb = str.encode(encoding="utf-8")
    for i in range(100000000):
        strb = hashlib.new('md4', strb).hexdigest().encode("utf-8")
        if i % 2000000 == 0:
            print(i)
    return strb


if __name__ == '__main__':
    str = "孙性空"
    start_time = time.time()
    print(calc(str))
    end_time = time.time()
    print("总用时%f秒" % (end_time - start_time))
