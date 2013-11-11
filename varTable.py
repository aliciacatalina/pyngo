#int 0-5000, float 5001-10000, bool 10001-15000
class Vartable(dict):
	def __init__(self, intpointer=0, 
				floatpointer=5001, boolpointer=10000):
		self.intpointer = intpointer
		self.floatpointer = floatpointer
		self.boolpointer = boolpointer

	def getintpointer(self):
		return self.intpointer

	def setintpointer(self):
		self.intpointer += 1

	def add(self, t, name):
		if not t in self:
			self[t] = {}
		if t == 'int':
			globalvartable = self.intpointer
			self[t][self.intpointer] = name
			self.intpointer += 1
		elif t == 'float':
			self[t][self.floatpointer] = name
			self.floatpointer += 1
		elif t == 'bool':
			self[t][self.boolpointer] = name
			self.boolpointer += 1
		else:
			raise Exception("No type")

globaltable = Vartable()
globaltable.add('int', 'a')
globaltable.add('float', 'c')
globaltable.add('float', 'd')
globaltable.add('float', 'i')
globaltable.add('float', 'b')
globaltable.add('bool', 'c')
print globaltable



