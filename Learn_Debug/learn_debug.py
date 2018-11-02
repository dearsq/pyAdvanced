print("============ 错误、调试和测试 ============")
'''
在程序运行过程中，总会遇到各种各样的错误。

有的错误是程序编写有问题造成的，比如本来应该输出整数结果输出了字符串，这种错误我们通常称之为bug，bug是必须修复的。

有的错误是用户输入造成的，比如让用户输入email地址，结果得到一个空字符串，这种错误可以通过检查用户输入来做相应的处理。

还有一类错误是完全无法在程序运行过程中预测的，比如写入文件的时候，磁盘满了，写不进去了，或者从网络抓取数据，网络突然断掉了。这类错误也称为异常，在程序中通常是必须处理的，否则，程序会因为各种问题终止并退出。

Python内置了一套异常处理机制，来帮助我们进行错误处理。

此外，我们也需要跟踪程序的执行，查看变量的值是否正确，这个过程称为调试。Python的pdb可以让我们以单步方式执行代码。

最后，编写测试也很重要。有了良好的测试，就可以在程序修改后反复运行，确保程序输出符合我们编写的测试。
'''

print("============ 1. 错误处理 try...except...finally... ============")
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

print("========================")

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

print("========================")
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar(0)
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
# Test
main()

print("============ 记录错误信息 logging ============")
'''
Python内置的logging模块可以非常容易地记录错误信息
'''
import logging
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar(0)
    except Exception as e:
        print('Error',e)
        # logging.exception(e)
    finally:
        print("Logging record...")

print('code start ...')
main()
print('code go on ...')



print("============ 抛出错误 ============")

class FooError(ValueError):
    pass

def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

# Test
# foo('0')

print("============ 练习 ============")

from functools import reduce

# def str2num(s):
#     return int(s)


def str2num(n):
    try:
        n = int(n)
    except ValueError as e:
        try:
            n = float(n)
        except ValueError as e:
            raise ValueError(r"'%s' not literal" % n)
    return n

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)
    print("END.")

main()