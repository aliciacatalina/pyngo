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
			print "This is a program"
			for element in self.args:
				if element is not None:
					element.semantic(function_name, result)
			print dict(globaltable.items() + localtable.items() + temptable.items()), cuadruplos

		elif self.type == "functions":
			for element in self.args:
				if element is not None:
					element.semantic(function_name, result)

		elif self.type == "function":
			function_name = self.args[1]
			localtable.add(function_name, self.args[0], "return")
			localtable.add(function_name, "functype", self.args[0])
			localtable[function_name]["functype"]["begin"] = len(cuadruplos)

			for element in self.args[2:]:
				if element is not None:
					element.semantic(function_name, result)
			cuadruplos.append(["ret","","",""])

		elif self.type == "lparameters":
			print self.args[0]
			cont = 1;
			for i in self.args[0]:
				print 'lparams', i[0], i[1]
				currenttable.add(function_name, i[0], i[1])
				localtable[function_name]["functype"]["param"+str(cont)] = i[1]
				cont += 1
			print localtable

		#Vars
		elif self.type == "vars":
			if self.args[0] is not None:
				result = self.args[0].semantic(function_name, result)

		elif self.type == "lvars":
			result = self.args[0].semantic(function_name, result) #declaration
			if self.args[1] is not None:
				result = self.args[1].semantic(function_name, result) #lvars

		elif self.type == "declaration":

			dimensions = self.args[0].args[1]
			if dimensions is not None:
				dimensions = reduce(lambda x, y: x*y, dimensions.args[0])
			else:
				dimensions = 1
			for i in self.args[1]:
				if function_name in currenttable:
					for key in currenttable[function_name]:
						if i in currenttable[function_name][key].keys():
							raise Exception ("Variable " + i + " alreay in use")
						else :
							if dimensions == 1:
								currenttable.add(function_name, self.args[0].args[0], i)
							else:
								currenttable.addmany(function_name, self.args[0].args[0], i, dimensions)
				else :
					if dimensions == 1:
						currenttable.add(function_name, self.args[0].args[0], i)
					else:
						currenttable.addmany(function_name, self.args[0].args[0], i, dimensions)
			print "declaration", currenttable

		# receives asignmany
			#for i in globaltable[function_name]:
			#	varlookup[i] = ({v:k for k, v in globaltable[function_name][i].items()})

		elif self.type == "asignmany":
			result = self.args[0].expression(function_name, result)
			if self.args[1] is not None:
				result = self.args[1].semantic(function_name, result)

		elif self.type == "model":
			print "model"
			result = self.args[0].semantic(function_name, result)

		elif self.type == "bloque":
			if self.args[0] is not None:
				result = self.args[0].semantic(function_name, result)

		elif self.type == "statement":
			print "STAAAATE", result
			if self.args[0] is not None:
				result = self.args[0].semantic(function_name, result)

		elif self.type == "bloque2":
			print "BLOQUE", result
			if self.args[0] is not None:
				result = self.args[0].semantic(function_name, result)
			if len(self.args) > 1 and self.args[1] is not None:
				result = self.args[1].semantic(function_name, result)

		#conditions
		elif self.type == "condition":
			print 'args', self.args[0].args[0]
			tipo, direccion = self.args[0].args[0].expression(function_name, result)
			if tipo != 'bool':
				raise Exception("Condicion debe ser tipo bool")
			#GOTO en falso
			gotof = ['gotof', direccion, " ", " "]
			cuadruplos.append(gotof)
			lena = len(cuadruplos)
			result = self.args[1].semantic(function_name, result)
			goto = ['goto', " ", " ", 0]
			cuadruplos.append(goto)
			gotof[3] = len(cuadruplos) - lena
			if self.args[2] is not None:
				lenelsea = len(cuadruplos)
				result = self.args[2].semantic(function_name, result)
				goto[3] = len(cuadruplos) - lenelsea
			print cuadruplos

		elif self.type == "for" :
			print 'id', self.args[0], 'in', 'punto', self.args[1], 'otro id', self.args[2], 'bloque', self.args[3].args[0]
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
				else:
					raise Exception("The array is not defined")
			savebool = temptable.add("Temp", "int", "temp")
			cuadruplos.append(['<',currenttable[function_name]['int'][self.args[0]] ,currenttable[function_name][key][self.args[2]], savebool])
			gotof = ['gotof', savebool, " ", " "]
			cuadruplos.append(gotof)
			lena = len(cuadruplos)
			result = self.args[3].semantic(function_name, result)
			cuadruplos.append(['+', 1, currenttable[function_name]['int'][self.args[0]], currenttable[function_name]['int'][self.args[0]]])
			goto = ['goto', back - len(cuadruplos), " ", ]
			cuadruplos.append(goto)
			gotof[3] = len(cuadruplos) - lena
			print cuadruplos

		elif self.type == "return" :
			resulttype, address = self.args[0].expression(function_name, result)
			#TODO: check if types are compatible
			localtable[function_name][resulttype]["return"] = address
			cuadruplos.append(["return", address, "", ""])

		# print
		elif self.type == "write" :
			result_type, address = self.args[0].expression(function_name, result)
			cuadruplos.append(["print", address, "", ""])

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
			result_type, address = self.args[2].expression(function_name, result)

			for key in currenttable[function_name]:
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

		elif self.type == "expresion":
			left_type, left_address = self.args[1].expression(function_name, result)
			right_type, right_address = self.args[2].expression(function_name, result)
			result_type = cubo_semantico[left_type][right_type][self.args[0]]
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

		elif self.type == "llamarfuncion" :
			cuadruplos.append(["ERA", self.args[0], "",""])
			for i in self.args[1]:
				resulttype, resultaddress = i.expression(function_name, result)
				cuadruplos.append(["Param", resultaddress, "", ""])
			cuadruplos.append(["Gosub", self.args[0], "", ""])
			functype = localtable[self.args[0]]["functype"]["return"]
			tempaddress = temptable.add("Temp", functype, "temp")
			cuadruplos.append(["=", localtable[self.args[0]][functype]["return"], "", tempaddress])
			return functype, tempaddress

		return result
