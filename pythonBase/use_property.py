class Screen(object):
	"""docstring for Screen"""
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, value):
		if value <= 0:
			raise ValueError('请输入大于0的数')    #'ValueError'首字母要大写，否则出错 
		else:
			self._width = value
		

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, value):
		if value <= 0:
			raise ValueError('请输入大于0的数')
		else:
			self._height = value
		
	@property
	def resolution(self):
		return self._width * self._height

screen = Screen()
screen.width = 30
screen.height = 40
print('resolution =',screen.resolution)
if screen.resolution == 1200:
	print('测试通过！')
else:
	print('测试失败！')