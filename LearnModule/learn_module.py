#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'Younix Zhang'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello Younix")
    elif len(args)==2:
        print('Hello, %s' %args[1])
    else:
        print("Too many arguments!")

if __name__=="__main__":
    test()


# 作用域 private
def _private_1(name):
    return '_private1, %s' %name

def __private_2(name):
    return '__private2, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return __private_2(name)


