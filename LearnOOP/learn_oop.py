
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
        self.name = name
        self.score = score
    def oop_print_score(self):
        print('OOP %s: %s' % (self.name, self.score))

# Test1
bart = Student('Bart Aiiage', 59)
lisa = Student('Lisa Aiiage',88)
bart.oop_print_score()
lisa.oop_print_score()


opp_print_score(std1)
opp_print_score(std2)

