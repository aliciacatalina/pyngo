#int 0-5000, float 5001-10000, bool 10001-15000
class Vartable(dict):
	def __init__(self, function_name, intpointer=0, 
				floatpointer=5001, boolpointer=10000):
		self.intpointer = intpointer
		self.floatpointer = floatpointer
		self.boolpointer = boolpointer

	def getintpointer(self):
		return self.intpointer

	def setintpointer(self):
		self.intpointer += 1

	def add(self, function_name, t, name):
		if function_name is None:
			function_name = "global"

		if function_name not in self:
			self[function_name] = {}

		if t not in self[function_name]:
			self[function_name][t] = {}
		if t == 'int':
			globalvartable = self.intpointer
			self[function_name][t][self.intpointer] = name
			self.intpointer += 1
		elif t == 'float':
			self[function_name][t][self.floatpointer] = name
			self.floatpointer += 1
		elif t == 'bool':
			self[function_name][t][self.boolpointer] = name
			self.boolpointer += 1
		else:
			raise Exception("No type")

globaltable = Vartable('global')
globaltable.add('a', 'int', 'a')
globaltable.add('global', 'float', 'c')
globaltable.add('global', 'float', 'd')
globaltable.add('global', 'float', 'i')
globaltable.add('a', 'float', 'b')
globaltable.add('global', 'bool', 'c')
print globaltable['global']



