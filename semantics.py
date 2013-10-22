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
		if self.type == "programa":	
			print "This is a program"
			result = self.args[2].semantic(result)
		elif self.type == "declaravarsdata":
			print "This is declaravarsdata"
			result = self.args[0].semantic(result)
		elif self.type == "vars":
			result = self.args[0].semantic(result)
		elif self.type == "listavars":
			print self.args[0].args[0], self.args[1].args[0]
			if not self.args[1].args[1].args[0]:
				print "one"
			else:
				print "more than one"


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


