from varTable import *
from CuboSemantico import *
import sys
cuadruplos = []
globaltable = Vartable()

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

		var_tipos = {'int' : 1, 'float' : 2, 'bool' : 3, 'bit' : 4, 'String' : 5}
		# start
		print "TYPE" ,self.type

		#Program
		if self.type == "program":
			print "This is a program"
			for elements in self.args:
				if elements is not None:
					elements.semantic(function_name, result)
			print globaltable, cuadruplos

		#TODO: functions
		elif self.type == "functions":
			print "funciones"
			result = self.args[0].semantic(function_name, result)

		#Vars
		elif self.type == "vars":
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
				if function_name in globaltable:
					for key in globaltable[function_name]:
						if i in globaltable[function_name][key].keys():
							raise Exception ("Variable " + i + " alreay in use")
						else :
							if dimensions == 1:
								globaltable.add(function_name, self.args[0].args[0], i)
							else:
								globaltable.addmany(function_name, self.args[0].args[0], i, dimensions)
				else :
					if dimensions == 1:
						globaltable.add(function_name, self.args[0].args[0], i)
					else:
						globaltable.addmany(function_name, self.args[0].args[0], i, dimensions)
			print "declaration", globaltable

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
			pointer = globaltable.getintpointer()
			globaltable.add(function_name, 'int', self.args[0])
			# i = 0
			cuadruplos.append(['=', 0 , '', globaltable[function_name]['int'][self.args[0]]])
			# length array id
			for key in globaltable[function_name]:
				if self.args[2] in globaltable[function_name][key].keys():
					cuadruplos.append(['length', globaltable[function_name][key][self.args[2]], "", ])
				else:
					raise Exception("The array is not defined")
			cuadruplos.append(['<',globaltable[function_name]['int'][self.args[0]] ,globaltable[function_name][key][self.args[2]], pointerdirtemp['int']+1])

			gotof = ['gotof', pointerdirtemp['int'], " ", " "]
			cuadruplos.append(gotof)
			lena = len(cuadruplos)
			result = self.args[3].semantic(function_name, result)
			cuadruplos.append(['+', 1, pointer, pointerdirtemp['int']])
			pointerdirtemp['int'] += 1
			goto = [32, back - len(cuadruplos), " ", ]
			cuadruplos.append(goto)
			gotof[3] = len(cuadruplos) - lena
			print cuadruplos

		elif self.type == "return" :
			print "returnnnnnnnnnn", result
			result, address = self.args[0].expression(function_name, result)

		# print
		elif self.type == "write" :
			result_type, address = self.args[0].args[0].expression(function_name, result)
			cuadruplos.append(["print", address, "", ""])

		elif self.type == "funcion":
			pass
			#result[self.args[1]] = {}
			#nombrfunc = self.args[1]
			#print "result", result
			#print "funciones", dir_func
			#if nombrfunc in dir_func:
			#	raise Exception("Funcion ya definida: " + nombrfunc)
			#else:
			#	globaltable[self.args[1]] = {}
			#	dir_func[self.args[1]] = {}
			#	if self.args[2] is not None:
			#		dir_func[self.args[1]] = {'params' : {} }
			#		dir_func[self.args[1]] = {'start' : len(cuadruplos)}
			#		params = self.args[2].args[0]
			#		parametros = {}
			#		print dir_func
			#		for x in range(len(params)):
			#			parametro = params.pop()
			#			tipo = parametro[0]
			#			if tipo not in globaltable[self.args[1]]:
			#				if tipo not in parametros:
			#					globaltable.add(self.args[1], tipo, parametro[1])
			#					parametros[tipo] = [parametro[1]]
			#					result[self.args[1]][tipo] = [parametro[1]]
			#				else:
			#					globaltable.add(self.args[1], tipo, parametro[1])
			#					parametros[tipo].append(parametro[1])
			#					result[self.args[1]][tipo].append(parametro[1])
			#			print parametros
			#			dir_func[self.args[1]]['params'] = parametros
			#			print globaltable
			#			print dir_func
			#			print self.args[0].args[0]
			#			result[self.args[1]]["parametros_func"] = parametros

			#	if self.args[0] is not None and self.args[0].args[0] > 0:
			#		result[self.args[1]]["retorno"] = self.args[0].args[0]
			#	if self.args[3] is not None:
			#		#dir_func[self.args[1]] = { 'return' : self.args[3].semantic(self.args[1], result)}
			#		print "selfargs5", self.args[5]
			#		result = self.args[5].semantic(self.args[1], result)
			#		print 'print result!!!', self.args[5].semantic(self.args[1],
		else:
			print "type not found"


	#Expression function to receive all expressions
	def expression(self, function_name, result):
		if function_name is None :
			function_name = "global"
		var_tipos = {'int' : 1, 'float' : 2, 'bool' : 3, 'bit' : 4, 'String' : 5}

		if self.type == "asign":
			varname = self.args[1].args[0]
			result_type, address = self.args[2].expression(function_name, result)

			for key in globaltable[function_name]:
				if self.args[1].args[0] in globaltable[function_name][key].keys():
					if result_type == key:
						cuadruplos.append([self.args[0], address, "", globaltable[function_name][result_type][varname]])
					else:
						raise Exception("You're asigning a different type of value")
				else:
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
			result_address = globaltable.add("Temp" + function_name, result_type, "temp")
			cuadruplos.append([self.args[0], left_address, right_address, result_address])
			return result_type, result_address

		elif self.type == "int" :
			return "int", globaltable.add(function_name, "int", self.args[0])

		elif self.type == "float" :
			return "float", globaltable.add(function_name, "float", self.args[0])

		elif self.type == "bool" :
			return "bool", globaltable.add(function_name, "int", self.args[0])

		elif self.type == "id":
			table = globaltable[function_name]
			for i in table:
				for j in table[i]:
					if j == self.args[0]:
						return i, table[i][j]
			raise Exception("Variable doesn't exist: " + self.args[0])

		elif self.type == "llamarfuncion" :
			return result[funcion]["retorno"], 1

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
