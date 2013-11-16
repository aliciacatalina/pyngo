from varTable import *
from CuboSemantico import *
import sys

dir_global = {}
dir_local = {}
dir_temp = {}
dir_cons = {}
cuadruplos = []
cuadruploactual = []
pilaO = []
pOper = []

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
		# start
		print "TYPE" ,self.type
		if self.type == "program":	
			print "This is a program"
			# self.args[1] sends vars to resulf
			#self.args[2] sends data to result
			result = self.args[1].semantic(result)
			self.args[3].semantic(result)	
			
			#functions
		elif self.type == "functions":
			print "funciones"

			#sends a varblock
		elif self.type == "vars":
			result = self.args[0].semantic(result)

			#receives VARS { lvars }
			#sends lvars to semantics
		elif self.type == "varblock":
			result = self.args[0].semantic(result)

			# VARS { type : var; }
			# if it declares more than one variable, sends lvars again
		elif self.type == "lvars":
			print len(self.args)
			result = self.args[0].semantic(result)
			if self.args[1] is not None:
				result = self.args[1].semantic(result)

			# receives : type : var;
		elif self.type == "declaration":
			#self.args[0].args[0].args[0] is the type
			#self.args[1] is the id 
			print "las cosas:", "is this a type?", self.args[0].args[0].args[0], "this is an id", self.args[1]
			for i in self.args[1] :
				for key in globaltable:
					if i in globaltable[key].values():
						# Send the type and id to the function add to give them an address
						raise Exception("Variable " + i + " alreay in use")
					else:
						globaltable.add(self.args[0].args[0].args[0], self.args[1].args[0])
				print globaltable
				print "one"
			else:
				print "more than one", self.args[1]
				result = self.args[1].semantic(result)
	
		elif self.type == "data":
			print "data segment"
			result = self.args[0].semantic(result)
		elif self.type == "asignmany":
			print "asignmany"
			result = self.args[0].semantic(result)
			if self.args[1] is not None:
				result = self.args[1].semantic(result)
		elif self.type == "asign":
			print "asign"

			print self.args[0]
			result = self.args[1].semantic(result)
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
			left_type = ""
			print "expresion"
			print "arg1", self.args[0],"op", self.args[1],"arg2", self.args[2]
			#Verify type of arguments and send to semantic cube
			if isinstance(self.args[0], int):
				left_type = "int"
			elif isinstance(self.args[0], float):
				left_type = "float"
			elif isinstance(self.args[0], bool):
				left_type = "bool"

			if isinstance(self.args[2], int):
				right_type = "int"
			elif isinstance(self.args[2], float):
				right_type = "float"
			elif isinstance(self.args[2], bool):
				right_type = "bool"

			result_type = cubo_semantico[left_type][right_type][self.args[1]]
			print "result_type " + result_type
			# hacer un append de cuadruplos y ver que onda con dir_temp
			# creo que tendre que hacer un dictionary de tipos, {'int':1}
			# para ver que onda con el pointerdirtemp[numtipo]
			# return result_type, pointerdirtemp[result_type] - 1 WHY




	#Expression function to receive all expressions
	def expression(self, class_name, function_name, result):
		var_tipos = {'int' : 1, 'float' : 2, 'bool' : 3, 'bit' : 4, 'String' : 5}
		if self.type == "expresion":
			print "expresion"
			print "arg1", self.args[0],"op", self.args[1],"arg2", self.args[2]
			left_type, direccion = self.args[0].expression(class_name, function_name, result)
			lefty = direccion
			print direccion, "left"
			right_type, direccion = self.args[2].expression(class_name, function_name, result)
			print "operacion", self.args[1], left_type, right_type, direccion
			pOper.append(self.args[1])
			numtipo = cubo_semantico[left_type][right_type][self.args[1]]
			#result = self.args[0].semantic(result)
			if isinstance(self.args[2], Node):
				return self.args[2].semantic(result)

			cuadruplos.append([self.args[1], left_type, right_side, 'temporal'])

			print self.args[0]
		elif self.type == "write":
			result = self.args[0].semantic(result)
		elif self.type == "write2":
			result = self.args[0].semantic(result)


			#print "case2", self.args[0]
			if self.args[0] is not None:
				result = self.args[0].semantic_body(class_name, function_name, result)

			if len(self.args) > 1 and self.args[1] is not None:
				result = self.args[1].semantic_body(class_name, function_name, result)

		else:
			print "missing type: " + self.type

		return result

	def get_names(self, arg):
		result = []

		#if arg[1] is not None:
		#	print arg, arg[1].args
		while arg is not None:
			result.append(arg[0])
			#print arg[0], type(arg[0])
			if len(arg) < 2 or arg[1] is None:
				arg = None
			else:
				arg = arg[1].args

		return result

			


		return result


