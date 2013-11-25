#int 0-5000, float 5001-10000, bool 10001-15000
class Vartable(dict):
	def __init__(self, intpointer=0,
				floatpointer=5001, boolpointer=10000):
		self.intpointer = intpointer
		self.floatpointer = floatpointer
		self.boolpointer = boolpointer
		self.temp = 0
		self.lastpointer = 0

	def getintpointer(self):
		return self.intpointer

	def getfloatpointer(self):
		return self.floatpointer

	def getboolpointer(self):
		return self.boolpointer

	def getlastpointer(self):
		return self.last.pointer

	def add(self, function_name, t, name):
		if function_name not in self:
			self[function_name] = {}
		if t not in self[function_name]:
			self[function_name][t] = {}
		if name is "temp":
			name = "t" + str(self.temp)
			self.temp += 1
		if name in self[function_name][t]:
			return self[function_name][t][name]
		if t == 'int':
			self[function_name][t][name] = self.intpointer
			self.lastpointer = self.intpointer
			self.intpointer += 1
		elif t == 'float':
			self[function_name][t][name] = self.floatpointer
			self.lastpointer = self.floatpointer
			self.floatpointer += 1
		elif t == 'bool':
			self[function_name][t][name] = self.boolpointer
			self.lastpointer = self.boolpointer
			self.boolpointer += 1
		elif t == 'functype':
			self[function_name][t]["return"] = name
		elif t == 'array':
			self[function_name][t][name] = name
		else:
			raise Exception("No type")
		return self.lastpointer

	def addmany(self, function_name, t, name, size):
		if function_name not in self:
			self[function_name] = {}
		if t not in self[function_name]:
			self[function_name][t] = {}
		if name is "temp":
			name = "t" + str(self.temp)
			self.temp += 1
		if t == 'int':
			self[function_name][t][name] = [x+1 for x in range(self.intpointer, self.intpointer+size)]
			self.lastpointer = self.intpointer + size
			self.intpointer += size+1
		elif t == 'float':
			self[function_name][t][name] = self.floatpointer
			self.lastpointer = self.floatpointer
			self.floatpointer += 1
		elif t == 'bool':
			self[function_name][t][name] = self.boolpointer
			self.lastpointer = self.boolpointer
			self.boolpointer += 1
		else:
			raise Exception("No type")
		return self.lastpointer
#class Vartable(dict):
#	def __init__(self, function_name, intpointer=0,
#				floatpointer=5001, boolpointer=10000):
#		self.intpointer = intpointer
#		self.floatpointer = floatpointer
#		self.boolpointer = boolpointer
#
#	def getintpointer(self):
#		return self.intpointer
#
#	def setintpointer(self):
#		self.intpointer += 1
#
#	def add(self, function_name, t, name):
#		if function_name is None:
#			function_name = "global"
#
#		if function_name not in self:
#			self[function_name] = {}
#
#		if t not in self[function_name]:
#			self[function_name][t] = {}
#		if t == 'int':
#			globalvartable = self.intpointer
#			self[function_name][t][self.intpointer] = name
#			self.intpointer += 1
#		elif t == 'float':
#			self[function_name][t][self.floatpointer] = name
#			self.floatpointer += 1
#		elif t == 'bool':
#			self[function_name][t][self.boolpointer] = name
#			self.boolpointer += 1
#		else:
#			raise Exception("No type")

#globaltable = Vartable()
#globaltable.add('a', 'int', 'a')
#print globaltable
#globaltable.add('global', 'float', 'c')
#globaltable.add('global', 'float', 'd')
#globaltable.add('global', 'float', 'i')
#globaltable.add('a', 'float', 'b')
#globaltable.add('global', 'bool', 'c')
#print globaltable['global']
#


