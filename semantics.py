from varTable import *
from possibleMemory import *
from collections import defaultdict

class Node(object):
	def __init__(self, t, *args):
		self.type = t
		self.args = args

	def __str__(self):
		return self.p()

	def p(self, n=0):
		s = " "* n + "type: " + str(self.type) + "\n"

		for i in self.args:
			if not isinstance(i, Node):
				s += str(i)
			else:
				s += i.p(n+1)
			s+= "\n"
		return s

	def semantic_all(self):
		class_dir = []
		return self.semantic(class_dir)
		
	def semantic(self, result):
		print "TYPE" ,self.type
		if self.type == "program":	
			print "This is a program"
			result = self.args[1].semantic(result)
			self.args[3].semantic(result)	
			# Send vars to semantic
			# result = self.args[1].semantic(result)
		elif self.type == "vars":
			result = self.args[0].semantic(result)
		elif self.type == "varblock":
			result = self.args[0].semantic(result)
		elif self.type == "lvars":
			print len(self.args)
			result = self.args[0].semantic(result)
			if self.args[1] is not None:
				result = self.args[1].semantic(result)
		elif self.type == "listofvars":
			print "las cosas:", "is this a type?", self.args[0].args[0].args[0], "this is an id", self.args[1].args[0]
			if not self.args[1].args[1]:
				test = globaltable.iteritems()
				for key, value in test:
					print globaltable.iteritems()
					for t, name in test:
						if self.args[1].args[0] == name:
							# Send the type and id to the function add to give them an address
							print "variable ya declarada"
						else:
							globaltable.add(self.args[0].args[0].args[0], self.args[1].args[0])
				print globaltable
				print "one"
			else:
				print "more than one", self.args[1].args[1]
				result = self.args[1].semantic(result)
		# elif self.type == "listofids":
		# 	print len(self.args)
		# 	print "many ids"
		# 	print self.args[0]
		# 	result = self.args[1].semantic(result)
		# elif self.type == "lid":
		# 	print len(self.args)
		# 	result = self.args[0].semantic(result)
		elif self.type == "data":
			print "data segment"
			result = self.args[0].semantic(result)
		elif self.type == "asignmany":
			print "asignmany"
			result = self.args[0].semantic(result)
		elif self.type == "asign":
			print "asign"
			#validate that it is not on the vartable already
			print self.args[1]
			# for t,name in globaltable.iteritems()
			# 	if self.args[0] == name


			#result = self.args[1].semantic(result)
			# asign self.args[1] to self.args[0] 
		elif self.type == "model":
			print "model"
			result = self.args[0].semantic(result)
		elif self.type == "statement":
			print "statement"
			result = self.args[0].semantic(result)
		elif self.type == "expresiones":
			print "expresiones"
			result = self.args[0].semantic(result)
			if self.args[1] is not None:
				result = self.args[1].semantic(result)
		elif self.type == "expresion":
			print "expresion"
			print "arg1", self.args[0],"op", self.args[1],"arg2", self.args[2],
			if isinstance(self.args[2], Node):
				return self.args[2].semantic(result)

		elif self.type == "write":
			result = self.args[0].semantic(result)
		elif self.type == "write2":
			result = self.args[0].semantic(result)

			

			#print "main"
#			cuadruplos.insert(0, [32, " ", "", len(cuadruplos)]	)
#			if self.args[2] is not None:
#				self.args[2].semantic_body("main", "global", result)
#			cuadruplos.append([37, " ", "", ""])
			
#		elif self.type == "clase":
			#print "clase"
#			if self.args[2] is not None:
#				nombre = self.args[0]
#				if nombre in result:
#						raise Exception("Clase ya definida: " + nombre)
#				else:
#						self.args[2].semantic_body(nombre, "global", result)
		return result


