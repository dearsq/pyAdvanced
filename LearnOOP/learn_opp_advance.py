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
class Student(object):
    __slots__ = ('name', 'age') #用tuple定义允许绑定的类型名称

s = Student() # 创建新的实例
s.name = 'Michael'
print(s.name) # 'Michael' # 绑定属性'name'
s.age = 25
print(s.age)  # 25 # 绑定属性'age'
s.score = 99
print(s.score) #无法成功 # 绑定属性'score'
# AttributeError: 'Student' object has no attribute 'score'
