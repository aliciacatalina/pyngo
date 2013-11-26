from varTable import *
from CuboSemantico import *
import sys
cuadruplos = []
globaltable = Vartable()
localtable = Vartable(15001, 20001, 25001)
temptable = Vartable(30001, 35001, 40001)

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
		return self.semantic("global", class_dir)

	def semantic(self, function_name, result):
		result = {}
		if function_name is None :
			function_name = "global"
		if function_name == "global":
			currenttable = globaltable
		else:
			currenttable = localtable

		# start
		print "TYPE" ,self.type

		#Program
		if self.type == "program":
			if self.args[0] is not None:
				gotomain = ["goto", '', '', '']
				cuadruplos.append(gotomain)
				self.args[0].semantic(function_name, result)
				gotomain[3] = len(cuadruplos)

			for element in self.args[1:]:
				if element is not None:
					element.semantic(function_name, result)
			print dict(globaltable.items() + localtable.items() + temptable.items()), cuadruplos
		#receives type functions ans sends a function
		elif self.type == "functions":
			for element in self.args:
				if element is not None:
					element.semantic(function_name, result)
		#receives a function
		elif self.type == "function":
			function_name = self.args[1]
			#stores the function name and its return type
			localtable.add(function_name, self.args[0], "return")
			localtable.add(function_name, "functype", self.args[0])
			#stores the quad where the array starts
			localtable[function_name]["functype"]["begin"] = len(cuadruplos)
			#creates a ret quad
			for element in self.args[2:]:
				if element is not None:
					element.semantic(function_name, result)
			cuadruplos.append(["ret","","",""])
		#receives the parameteres inside a function
		elif self.type == "lparameters":
			print self.args[0]
			cont = 1;
			#saves the number of parameters and the name of the variable
			for i in self.args[0]:
				print 'lparams', i[0], i[1]
				paramaddress = currenttable.add(function_name, i[0], i[1])
				localtable[function_name]["functype"]["param"+str(cont)] = paramaddress
				cont += 1
			print localtable

		#Vars block
		elif self.type == "vars":
			if self.args[0] is not None:
				result = self.args[0].semantic(function_name, result)
		# list of vars
		elif self.type == "lvars":
			result = self.args[0].semantic(function_name, result) #declaration
			if self.args[1] is not None:
				result = self.args[1].semantic(function_name, result) #lvars
		# receives type[] : id or type : id
		elif self.type == "declaration":
			# if it is an array, stores its dimension
			dimension = self.args[0].args[1]
			if dimension is not None:
				size = reduce(lambda x, y: x*y, dimension.args[0])
				#validate that the variable is not in use
				for i in self.args[1]:
					if function_name in currenttable:
						for key in currenttable[function_name]:
							if i in currenttable[function_name][key].keys():
								raise Exception ("Variable " + i + " already in use")
					for j in range(size):
						name = i if j == 0 else i + str(j)
						currenttable.add(function_name, self.args[0].args[0], name)
					currenttable.addarray(function_name, self.args[0].args[0], i,
										currenttable[function_name][self.args[0].args[0]][i], size, dimension.args[0])
			#not arrays
			else:
				size = 1
				for i in self.args[1]:
					if function_name in currenttable:
						for key in currenttable[function_name]:
							if i in currenttable[function_name][key].keys():
								raise Exception ("Variable " + i + " already in use")
					currenttable.add(function_name, self.args[0].args[0], i)

		elif self.type == "asignmany":
			result = self.args[0].expression(function_name, result)
			if self.args[1] is not None:
				result = self.args[1].semantic(function_name, result)
		# receives the model, that works as a main
		elif self.type == "model":
			print "model"
			result = self.args[0].semantic(function_name, result)
		# this can receive several statements between { }
		elif self.type == "bloque":
			if self.args[0] is not None:
				result = self.args[0].semantic(function_name, result)
		#statements
		elif self.type == "statement":
			print "STAAAATE", result
			if self.args[0] is not None:
				result = self.args[0].semantic(function_name, result)
		# may receive several statements
		elif self.type == "bloque2":
			print "BLOQUE", result
			if self.args[0] is not None:
				result = self.args[0].semantic(function_name, result)
			if len(self.args) > 1 and self.args[1] is not None:
				result = self.args[1].semantic(function_name, result)

		#conditions
		elif self.type == "condition":
			print 'args', self.args[0]
			tipo, direccion = self.args[0].expression(function_name, result)
			if tipo != 'bool':
				raise Exception("Condicion debe ser tipo bool")
			#GOTO when the condition is false
			gotof = ['gotof', direccion, " ", " "]
			cuadruplos.append(gotof)
			lena = len(cuadruplos)
			result = self.args[1].semantic(function_name, result)
			goto = ['goto', " ", " ", 0]
			cuadruplos.append(goto)
			# set quad in gotof to skip until the block inside
			gotof[3] = len(cuadruplos) - lena
			if self.args[2] is not None:
				lenelsea = len(cuadruplos)
				result = self.args[2].semantic(function_name, result)
				goto[3] = len(cuadruplos) - lenelsea
			print cuadruplos
		#receives a for loop
		elif self.type == "for" :
			#saves the first for quad
			back = len(cuadruplos)
			pointer = currenttable.getintpointer()
			currenttable.add(function_name, 'int', self.args[0])
			# i = 0
			cuadruplos.append(['=', 0 , '', currenttable[function_name]['int'][self.args[0]]])
			# length array id
			for key in currenttable[function_name]:
				if self.args[2] in currenttable[function_name][key].keys():
					savelength = temptable.add("Temp", "int", "temp")
					cuadruplos.append(['length', currenttable[function_name][key][self.args[2]], "",savelength ])
					break
				else:
					raise Exception("The array is not defined")
			#saves the result of a boolean expression
			savebool = temptable.add("Temp", "int", "temp")
			cuadruplos.append(['<',currenttable[function_name]['int'][self.args[0]] ,currenttable[function_name][key][self.args[2]], savebool])
			#gotof when the result of the expression is not true
			gotof = ['gotof', savebool, " ", " "]
			cuadruplos.append(gotof)
			lena = len(cuadruplos)
			result = self.args[3].semantic(function_name, result)
			cuadruplos.append(['+', 1, currenttable[function_name]['int'][self.args[0]], currenttable[function_name]['int'][self.args[0]]])
			goto = ['goto', back - len(cuadruplos), " ", ]
			cuadruplos.append(goto)
			#adds the forth item on the list, where to go when it is false
			gotof[3] = len(cuadruplos) - lena
			print cuadruplos

		elif self.type == "return" :
			resulttype, address = self.args[0].expression(function_name, result)
			#Verifies that the return type is compatible
			if resulttype != currenttable[function_name]["functype"]["return"] :
				raise Exception("The return type is different than the asigned one")
			else :
				localtable[function_name][resulttype]["return"] = address
				cuadruplos.append(["return", address, "", ""])

		# print
		elif self.type == "write" :
			result_type, address = self.args[0].expression(function_name, result)
			cuadruplos.append(["print", address, "", ""])

		elif self.type == "optimize" :
			print "optimization"

			cuadruplos.append([self.args[0], '', '', ''])
			result = self.args[1].semantic(function_name, result)
		elif self.type == "build" :
			print "builing"
		elif self.type == "where" :
			print "these are my conditions"
		else:
			print "type not found"


	#Expression function to receive all expressions
	def expression(self, function_name, result):
		if function_name == "global":
			currenttable = globaltable
		else:
			currenttable = localtable

		var_tipos = {'int' : 1, 'float' : 2, 'bool' : 3, 'bit' : 4, 'String' : 5}

		if self.type == "asign":
			varname = self.args[1].args[0]
			array_asign = self.args[2]
			#validate that arrays exists
			if "arrays" in currenttable[function_name].keys():
				#asigning arrays
				#validates that the array is on the array table
				if varname in currenttable[function_name]["arrays"].keys() :
					#saves the array size
					array_size = currenttable[function_name]["arrays"][varname]["size"]
					#saves the address where the array begins
					array_address = currenttable[function_name]['int'][varname]
					#for every item on the array, it asigns them the value given
					for i in range(array_size):
						result_type, address = array_asign[i].expression(function_name, result)
						cuadruplos.append([self.args[0], address , "", array_address+i])

			else :
				#asigns a simple variable
				result_type, address = self.args[2][0].expression(function_name, result)
				for key in currenttable[function_name]:
					#verifies that the variable has been declared
					if self.args[1].args[0] in currenttable[function_name][key].keys():
						if result_type == key:
							cuadruplos.append([self.args[0], address, "", currenttable[function_name][result_type][varname]])
							break
						else:
							raise Exception("You're asigning a different type of value")
					else:
						print self.args[1].args[0], currenttable[function_name][key].keys()
						raise Exception("You're trying to asign '" + self.args[1].args[0]+ "' a value and it has not been declared in vars")


		elif self.type == "expresiones":
			print "expresiones"
			result = self.args[0].semantic(function_name, result)
			if self.args[1] is not None:
				result = self.args[1].semantic(function_name, result)
		#handles an expression
		elif self.type == "expresion":
			#left operator type
			left_type, left_address = self.args[1].expression(function_name, result)
			#right operator type
			right_type, right_address = self.args[2].expression(function_name, result)
			#result type
			result_type = cubo_semantico[left_type][right_type][self.args[0]]
			#temp addresses
			result_address = temptable.add("Temp", result_type, "temp")
			cuadruplos.append([self.args[0], left_address, right_address, result_address])
			return result_type, result_address

		elif self.type == "int" :
			return "int", currenttable.add(function_name, "int", self.args[0])

		elif self.type == "float" :
			return "float", currenttable.add(function_name, "float", self.args[0])

		elif self.type == "bool" :
			return "bool", currenttable.add(function_name, "int", self.args[0])

		elif self.type == "id":
			table = currenttable[function_name]
			for i in table:
				for j in table[i]:
					if j == self.args[0]:
						return i, table[i][j]
			raise Exception("Variable doesn't exist: " + self.args[0])
		#call function. Receives id(params)
		elif self.type == "llamarfuncion" :
			#separates a space for the function call
			cuadruplos.append(["ERA", self.args[0], "",""])
			contp = 1
			for i in self.args[1]:
				resulttype, resultaddress = i.expression(function_name, result)
				cuadruplos.append(["Param", resultaddress, "", "param"+str(contp)])
				contp += 1
			cuadruplos.append(["Gosub", self.args[0], "", ""])
			functype = localtable[self.args[0]]["functype"]["return"]
			tempaddress = temptable.add("Temp", functype, "temp")
			cuadruplos.append(["=", localtable[self.args[0]][functype]["return"], "", tempaddress])
			return functype, tempaddress

		return result
