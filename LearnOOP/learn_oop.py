
print("============ 1. What is OOP ============")
# use dict to show students' grades
std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }


# OPP 面向过程
def opp_print_score(std):
    print('OPP %s: %s' % (std['name'], std['score']))

# OOP 面向对象
class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.set_score(score)

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('score beyonds range !')

    def oop_print_score(self):
        print('OOP %s: %s' % (self.__name, self.__score))

# Test1
bart = Student('Bart Aiiage', 59)
lisa = Student('Lisa Aiiage',88)
bart.oop_print_score()
lisa.oop_print_score()


opp_print_score(std1)
opp_print_score(std2)

print("============ 2. 封装 继承 ============")
younix = Student('Younix',22) # younix 为 Student 的一个 instance
print(younix)
print(Student)

# 封装 继承
class Student2(Student):
    def get_grade(self):
        if self.get_score() >= 90:
            return 'A'
        elif self.get_score() >= 60:
            return 'B'
        else:
            return 'C'

Linda = Student2('Linda',99)
print(Linda.get_name(), 'is' , Linda.get_grade())

# 多态
class Animal(object):
    def run(self):
        print("Animal is running ...")

class Dog(Animal):
    def __init__(self):
        print("I am dog ...")

    def run(self):
        print("Dog is running ...")

class Cat(Animal):
    def __init__(self):
        print("I am cat ...")


jerry = Dog()
jerry.run()

tom = Cat()
tom.run()

print(isinstance(jerry, Animal))
print(isinstance(jerry, Dog))
print(isinstance(jerry, Cat))


print("============ 3. 获取对象信息 ============")
print(type(123))
print(type('abcdefg'))
print(type(None))

# 判断是否为函数
import types
def fn():
    pass
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x+1)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

# 获取一个对象的所有属性和方法 dir()
print(dir('ABC'))
print(dir(jerry)) # 可以看到 run

# getattr() setattr() hasattr()

class NumberObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

mNumber = NumberObject()
print(hasattr(mNumber,'x')) #有属性x吗 True
print(hasattr(mNumber,'y')) #有属性y吗 False
setattr(mNumber,'y',99) #设置属性y
print(hasattr(mNumber,'y')) #有属性y吗 True
print(getattr(mNumber,'y')) #获取属性y 99
print(mNumber.y) #打印mNumber.y 99


class ImageObject(object):
    def read(self):
        print("ImageObject: I am read")

mImage = ImageObject()

def readData(io):
    print("I am reading data")

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    print("return None")
    return None

readImage(mImage)   # has read
readImage(mNumber)  # None

print("============ 4. 类和属性 ============")
class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试程序
if Student.count != 0:
    print('测试失败1!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败2!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败3!')
        else:
            print('Students:', Student.count)
            print('测试通过!')