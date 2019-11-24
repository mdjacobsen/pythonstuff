class OO:
	def __init__(self):
		self.x = "test"
	def testfunc(self):
		self.x = "new"
		#return self.x
	def printfunc(self):
		self.testfunc()
		print(self.x)
newclass = OO()
newclass.printfunc()