#test 1
def outName(s):
	print(s)

outName("杨贤杰")

#test 2
def trueName(a):
	if a <= 5:
		print("杨杰")
	else:
	    print("杨贤杰")

trueName(10)


# def power(x, n):
#     b = 1
#     while n > 0:
#         n = n - 1
#         b = b * x
#     return b

# power(5,2)

#test 3
def girlInfo(name, gender = "female", city ="重庆" ):

	print("name :" , name)
	print("gender :" , gender)
	print("city :", city)

girlInfo("杨贤杰")
girlInfo("冉婷婷")
girlInfo("赖靖", city = "四川")

#test 4
class Student(object):

	def __init__(self, name, score):
		self.name =  name
		self.score = score


StudentA = Student("杨贤杰", 100)
print(StudentA.name , StudentA.score)
