class Student(object):        #Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
    __slot__ = ('name', 'score')
s = Student()
s.name = 'Bob'
s.score = '90'
s.gender = 'male'
print(s.score)
#print(s.male)       #会提示'AttributeError: 'Student' object has no attribute 'male''

class NewStudent1(Student):
	pass

news1 = NewStudent1()
news1.name = 'Tina'
news1.gender = 'female'
print(news1.name)
print(news1.gender)        #打印正常，子类的属性不受父类slots的影响

class NewStudent2(Student):
	__slot__ = 'gender'

new2 = NewStudent2()
new2.name = 'Candy'
new2.score = '100'
new2.gender = 'female'
print(new2.name)        #打印正常，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__
print(new2.score)
print(new2.gender)
