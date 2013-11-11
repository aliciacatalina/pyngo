#int 0-5000, float 5001-10000, bool 10001-15000
#global variables
globalints = 15000
globalfloats = 20000
globalbools = 25000

#local variables
localints = 30000
localfloats = 31000
localbools = 32000

#temporal variables
temporalints = 33000
temporalfloats = 34000
temporalbools = 35000

#constant variables (what)
constantints = 36000
constantfloats = 37000
constantbools = 38000

class possibleMemory(dict):
	def __init__(self, globalintpointer=15000, 
				globalfloatpointer=20000, globalboolpointer=10000, localintpointer=30000, localfloatpointer=31000, localboolpointer=32000, temporalintpointer=33000, temporalfloatpointer=34000, temporalboolpointer=35000, constantintpointer=36000, constantfloatpointer=37000, constantboolpointer=38000):
		self.globalintpointer = globalintpointer
		self.globalfloatpointer = globalfloatpointer
		self.globalboolpointer = globalboolpointer
		self.localintpointer = localintpointer
		self.localfloatpointer = localfloatpointer
		self.localboolpointer = localboolpointer
		self.temporalintpointer = temporalintpointer
		self.temporalboolpointer = temporalboolpointer
		self.temporalfloatpointer = temporalfloatpointer
		self.constantintpointer = constantintpointer
		self.constantfloatpointer = constantfloatpointer
		self.constantboolpointer = constantboolpointer

	def getglobalintpointer(self):
		return self.globalintpointer

	def setintpointer(self):
		self.intpointer += 1

	def add(self, address, value):
		if address >= 0:
			memory = self.globalintpointer
			self[address] = value
			self.globalintpointer += 1
		else:
			raise Exception("No valid address")

memory = possibleMemory()
memory.add('15000', '5')
memory.add('20000', '4.3')
memory.add('20001', '3.4')
memory.add('20002', '5.1')
memory.add('20003', '6.5')
memory.add('25000', 'true')
print memory