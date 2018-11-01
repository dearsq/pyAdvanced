print("============ 多重继承、定制类、元类 ============")
class Student(object):
    pass

s = Student()
s.name = 'Michael' #给实例绑定一个属性
print(s.name)

print("============ 给实例绑定一个方法 MethodType ============")
def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age) # 测试结果

print("============ 限制实例添加属性 __slot__ ============")
'''
只对当前类有效, 对其子类无效
'''
class Student(object):
    __slots__ = ('name', 'age') #用tuple定义允许绑定的类型名称

s = Student() # 创建新的实例
s.name = 'Michael'
print(s.name) # 'Michael' # 绑定属性'name'
s.age = 25
print(s.age)  # 25 # 绑定属性'age'
if 0:
    s.score = 99
    print(s.score) #无法成功 # 绑定属性'score'
# AttributeError: 'Student' object has no attribute 'score'

print("============ @property ============")
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.set_score(60) # ok!
print(s.get_score())
# s.set_score(9999) #Error!
# ValueError: score must between 0 ~ 100!

# property 实现
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
# Test
s = Student()
s.score = 60 # ok!
print(s.score)
# s.score = 9999 # Error!
# ValueError: score must between 0 ~ 100!


class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

# birth 可读可写
# age 仅读

class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,value):
        self._height = value

    @property
    def resolution(self):
        return self._height * self._width

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

print("============ 多重继承 ============")
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

print("============ MixIn ============")

class CarnivorousMixIn(object):
    def eatmeat(self):
        print('Eating meats...')

class HerbivoresMixIn(object):
    def eatgrass(self):
        print('Eating grass...')

class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass

class Bat(Mammal, FlyableMixIn):
    pass

print("============ 定制类 ============")
print("============ __str__ __repr__ ============")
class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Michael'))
print(Student('Good'))
print(Student(''))

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name:%s)' % self.name

print(Student('Michael'))
s = Student('Michael')
print(s)
print("__str__:",s.__str__())
print("__repr__:",s.__repr__())

print("============ __iter__ 迭代类 ============")
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

for n in Fib():
    print(n)