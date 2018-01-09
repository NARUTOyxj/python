#test 1
# def outName(s):
# 	print(s)

# outName("杨贤杰")

# #test 2
# def trueName(a):
# 	if a <= 5:
# 		print("杨杰")
# 	else:
# 	    print("杨贤杰")

# trueName(10)


# def power(x, n):
#     b = 1
#     while n > 0:
#         n = n - 1
#         b = b * x
#     return b

# power(5,2)

#test 3
# def girlInfo(name, gender = "female", city ="重庆" ):

# 	print("name :" , name)
# 	print("gender :" , gender)
# 	print("city :", city)

# girlInfo("杨贤杰")
# girlInfo("冉婷婷")
# girlInfo("赖靖", city = "四川")

#test 4
# class Student(object):  /类名首字母大写

# 	def __init__(self, name, score):   
# 		self.name =  name
# 		self.score = score


# StudentA = Student("杨贤杰", 100)
# print(StudentA.name , StudentA.score)

#test 5
#数据封装
# class Student(object):
# 	"""docstring for Student"""
# 	def __init__(self, name, score):
# 		self.name = name
# 		self.score = score

# 	def  get_grade(self):
# 		if self.score >= 90:
# 			return 'A'
# 		elif self.score >= 60:
# 			return 'B'
# 		else:
# 			return 'C'
		
# StudentB = Student('Tom',90)
# print(StudentB.name, StudentB.get_grade())

#test 6
#访问限制
class StudentC(object):
	"""docstring for StudentC"""
	def __init__(self, name, gender):
		self.__name = name
		self.__gender = gender

	def get_name(self):
		return self.__name

	def get_gender(self):
		return self.__gender

	def set_name(self, name):
		self.__name = name

	def set_gender(self, gender):
		self.__gender = gender
		

Alice = StudentC('Alice','female')
Alice.set_gender('female')
print(Alice.get_gender())



     	





