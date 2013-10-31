#int 0-5000, float 5001-10000, bool 10001-15000
class Vartable(dict):
	def __init__(self, intpointer=0, floatpointer=5001, boolpointer=10000):
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
		if t == 1:
			self[t][self.intpointer] = name
			self.intpointer += 1
		elif t == 2:
			self[t][self.floatpointer] = name
			self.floatpointer += 1
		elif t == 3:
			self[t][self.boolpointer] = name
			self.boolpointer += 1
		else:
			raise Exception("No type")

#globaltable = Vartable()
#globaltable.add(1, 'a')
#globaltable.add(2, 'c')
#globaltable.add(2, 'd')
#globaltable.add(2, 'i')
#globaltable.add(2, 'b')
#globaltable.add(3, 'c')
#print globaltable
