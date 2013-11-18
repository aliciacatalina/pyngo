from varTable import *
from CuboSemantico import *
import sys

pointerdir = {'int' : 100, 'float': 2001, 'bool': 4001, 'string': 6001, 5: 8001}
pointerdirlocal = {'int' : 10001, 'float': 12001, 'bool': 14001, 'string': 16001, 5: 18001}
pointerdirtemp = {'int' : 20001, 'float': 22001, 'bool': 24001, 'string': 26001, 5: 28001}
pointerdirconst = {'int' : 30001, 'float': 32001, 'bool': 34001, 'string': 36001, 5: 38001}
dir_global = {}
dir_local = {}
dir_temp = {}
dir_cons = {}
varlookup = {}
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
		return self.semantic("global", class_dir)
		
	def semantic(self, function_name, result):
		if function_name is None :
			function_name = "global"

		var_tipos = {'int' : 1, 'float' : 2, 'bool' : 3, 'bit' : 4, 'String' : 5}
		# start
		print "TYPE" ,self.type
		if self.type == "program":	
			print "This is a program"
			self.args[0].semantic(function_name, result)
			# self.args[1] sends vars to resulf
			#self.args[2] sends data to result
			result = self.args[0].semantic(function_name, result)
			self.args[3].semantic(function_name, result)	
			
			#functions
		elif self.type == "functions":
			print "funciones"
			result = self.args[0].semantic(function_name, result)

			#sends a varblock
		elif self.type == "vars":
			result = self.args[0].semantic(function_name, result)

			#receives VARS { lvars }
			#sends lvars to semantics
		elif self.type == "varblock":
			result = self.args[0].semantic(function_name, result)

			# VARS { type : var; }
			# if it declares more than one variable, sends lvars again
		elif self.type == "lvars":
			print len(self.args)
			result = self.args[0].semantic(function_name, result)
			if self.args[1] is not None:
				result = self.args[1].semantic(function_name, result)

			# receives : type : var;
		elif self.type == "declaration":
			#self.args[0].args[0].args[0] is the type
			#self.args[1] is the id 
			print "las cosas:", "is this a type?", self.args[0].args[0].args[0],  "this is an id", self.args[1]
			if self.args[0].args[1] is not None:
				print "aqui", self.args[0].args[1]
				dimensions = reduce(lambda x, y: x*y, self.args[0].args[1].args[0])
			else:
				dimensions = 1
			print "dimensions", dimensions
			# for every element on the id array, check if it exists on array, if the id already exists on the table, raise Exception
			for i in self.args[1] :
				for key in globaltable:
					if i in globaltable[key].values():
						raise Exception("Variable " + i + " alreay in use")
				# Send the type and id to the function add to give them an address
				for j in range(dimensions):
					globaltable.add(self.args[0].args[0].args[0], i)
			print globaltable

		# receives asignmany
		elif self.type == "data":
			for i in globaltable:
				varlookup[i] = ({v:k for k, v in globaltable[i].items()})
			print "data segment"
			result = self.args[0].semantic(function_name, result)

		#receive a single asign or comes back to asign many
		elif self.type == "asignmany":
			print "asignmany"
			result = self.args[0].semantic(function_name, result)
			if self.args[1] is not None:
				result = self.args[1].semantic(function_name, result)

		#receives var = 1, 2;
		# or var = 3+3;
		elif self.type == "asign":
			print "asign"
			self.expression(function_name, result)
			
		elif self.type == "model":
			print "model"
			result = self.args[0].semantic(function_name, result)

		elif self.type == "bloque":
			if self.args[0] is not None:
				result = self.args[0].semantic(function_name, result)
		
		elif self.type == "statement":
			if self.args[0] is not None:
				result = self.args[0].semantic(function_name, result)
		
		elif self.type == "bloque2":
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
			gotof = [31, direccion, " ", " "]
			cuadruplos.append(gotof)
			lena = len(cuadruplos)
			result = self.args[1].semantic(function_name, result)
			goto = [32, " ", " ", 0]
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
			globaltable.add('int', self.args[0])
			cuadruplos.append(['=', 0 , '', pointer])
			cuadruplos.append(['length', self.args[2], "", pointerdirtemp['int']])
			cuadruplos.append(['<', pointer, pointerdirtemp['int'], pointerdirtemp['int']+1])
			pointerdirtemp['int'] += 1
			gotof = [31, pointerdirtemp['int'], " ", " "]
			cuadruplos.append(gotof)
			lena = len(cuadruplos)
			result = self.args[3].semantic(function_name, result)
			cuadruplos.append(['+', 1, pointer, pointerdirtemp['int']])
			pointerdirtemp['int'] += 1
			goto = [32, back - len(cuadruplos), " ", ]
			cuadruplos.append(goto)
			gotof[3] = len(cuadruplos) - lena
			print cuadruplos

		elif self.type == "funcion":
			nombrfunc = self.args[1]
			if nombrfunc in result:
				raise Exception("Funcion ya definida: " + nombrfunc)
			else:
				if self.args[2] is not None:
					params = self.args[2].args[0]
					print params
					parametros = {}
					for x in range(len(params)):
						parametro = params.pop()
						tipo = var_tipos[parametro[0]]
						if tipo not in parametros:
							parametros[tipo] = [parametro[1]]
							result[self.args[1]][tipo] = [parametro[1]]
						else:
							parametros[tipo].append(parametro[1])
							result[self.args[1]][tipo].append(parametro[1])
					print parametros
					print self.args[0].args[0]
					result[self.args[1]]["parametros_func"] = parametros
					
				if self.args[0] is not None and self.args[0].args[0] > 0:
					result[self.args[1]]["retorno"] = self.args[0].args[0]
				if self.args[3] is not None:
					result = self.args[3].semantic(self.args[0], result)


		# print
		elif self.type == "write" :
			result_type, address = self.args[0].args[0].expression(function_name, result)
			print cuadruplos
			print "write", address


	#Expression function to receive all expressions
	def expression(self, function_name, result):
		if function_name is None :
			function_name = "global"

		var_tipos = {'int' : 1, 'float' : 2, 'bool' : 3, 'bit' : 4, 'String' : 5}
		if self.type == "asign":
			print "asign dentro de expresiones"
			#print "operador", self.args[0].args[0], "id", self.args[1].args[0]	
			if self.args[2] is not None :
				print 'mas numeros', self.args[2]
				result_type, address = self.args[2].expression(function_name, result)

			result = self.args[0].expression(function_name, result)
			cuadruplos.append([self.args[0].args[0], address, '', varlookup[result_type][self.args[1].args[0]]])

		elif self.type == "expresiones":
			print "expresiones"
			print self.args[0], self.args[1]
			result = self.args[0].semantic(function_name, result)
			if self.args[1] is not None:
				result = self.args[1].semantic(function_name, result)

		elif self.type == "expresion":
			print 'expresion', self.args[1]
			left_type, direccion = self.args[1].expression(function_name, result)
			lefty = direccion
			print direccion, "left"
			right_type, direccion = self.args[2].expression(function_name, result)
			print "arg1", self.args[1],"op", self.args[0],"arg2", self.args[2]
			print "ope", self.args[0], left_type, right_type, direccion
			#Verify type of arguments and send to semantic cube
			if isinstance(self.args[1], int):
				left_type = "int"
			elif isinstance(self.args[1], float):
				left_type = "float"
			elif isinstance(self.args[1], bool):
				left_type = "bool"

			if isinstance(self.args[2], int):
				right_type = "int"
			elif isinstance(self.args[2], float):
				right_type = "float"
			elif isinstance(self.args[2], bool):
				right_type = "bool"

			result_type = cubo_semantico[left_type][right_type][self.args[0]]
			print result_type

			dir_temp[pointerdirtemp[result_type]] = " " + str(lefty) + " - " + str(direccion)
			cuadruplos.append([self.args[0], lefty, direccion, pointerdirtemp[result_type]])
			pointerdirtemp[result_type] += 1
			return result_type, pointerdirtemp[result_type] - 1 

		elif self.type == "int" : 
			dir_cons[pointerdirconst['int']] = int(self.args[0])
			pointerdirconst['int'] += 1
			return 'int', pointerdirconst['int'] - 1 

		elif self.type == "float" :
			dir_cons[pointerdirconst['float']] = float(self.args[0])
			pointerdirconst['float'] += 1
			return 'float', pointerdirconst['float'] - 1

		elif self.type == "bool" :
			if self.args[0] == "true" :
				valor = True 
			else :
				valor = False
			dir_cons[pointerdirconst['bool']] = valor
			pointerdirconst['bool'] += 1
			return 'bool', pointerdirconst['bool'] - 1

		elif self.type == "string" :
			dir_cons[pointerdirconst['string']] = self.args[0]
			pointerdirconst['string'] += 1
			return 'string', pointerdirconst['string'] - 1

		elif self.type == "id" :
			table = result if function_name == "global" else result[function_name]
			var_type = None
			for t in table :
				tableiter = result[t] if function_name == "global" else result[function_name][t]
				if self.args[1] in tableiter :
					var_type = t
					break
			if not var_type :
				raise Exception("Variable no declarada" + self.args[1])
			return var_type, dir_global.keys()[dir_global.values.index(self.args[0])]

		elif self.type == "llamarfuncion" :
			funcion = self.args[0]
			if "." in self.args[0]:
				llamadafuncion = self.args[0].rsplit(".")
				clase = llamadafuncion[0]
				funcion = llamadafuncion[1]
			if funcion not in result[clase]:
				raise Exception("Funcion no definida " + funcion)
			var_tipos = {'int' : 1, 'float' : 2, 'bool' : 3, 'bit' : 4, 'String' : 5}
			return var_tipos[result[funcion]["retorno"]], 1

		print cuadruplos

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

			


