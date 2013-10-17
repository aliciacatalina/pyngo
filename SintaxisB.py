from pprint import pprint
from CuboSemantico import *
import sys
pointerdir = {1 : 100, 2: 2001, 3: 4001, 4: 6001, 5: 8001}
pointerdirlocal = {1 : 10001, 2: 12001, 3: 14001, 4: 16001, 5: 18001}
pointerdirtemp = {1 : 20001, 2: 22001, 3: 24001, 4: 26001, 5: 28001}
pointerdirconst = {1 : 30001, 2: 32001, 3: 34001, 4: 36001, 5: 38001}
dir_global = {}
dir_local = {}
dir_temp = {}
dir_cons = {}
cuadruplos = []
cuadruploactual = []
pilaO = []
pOper = []
class AutoVivification(dict):
	def __getitem__(self, item):
		try:
			return dict.__getitem__(self, item)
		except KeyError:
			value = self [item] = type(self)()
			return value


class Node(object):
	dir_int = 1
	dir_float = 5000
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
		class_dir = AutoVivification() 
		return self.semantic(class_dir)
		
	def semantic(self, result):
		#print "TYPE" ,self.type
		if self.type == 'main':
			#print "main"
			if self.args[2] is not None:
				self.args[2].semantic_body("main", "global", result)
			
		elif self.type == 'clase':
			#print "clase"
			if self.args[2] is not None:
				nombre = self.args[0]
				if nombre in result:
						raise Exception("Clase ya definida: " + nombre)
				else:
						self.args[2].semantic_body(nombre, "global", result)

		elif self.type == "programa":
			#print "programa"
			result = self.args[1].semantic(result)

		elif self.type == "codigo":
			#print "codigo"
			result = self.args[0].semantic(result)

		elif self.type == "prog2":
			#print "prog2"
			#print len(self.args)
			if len(self.args) > 1 :
				result = self.args[0].semantic(result)
				self.args[1].semantic(result)
			else:
				result = self.args[0].semantic(result)
		else:
			print "missing type" + self.type

		return result

	def expression(self, class_name, function_name, result):
		if self.type == "expresion":
			left_type, direccion = self.args[1].expression(class_name, function_name, result)
			lefty = direccion
			print direccion, "left"
			right_type, direccion = self.args[2].expression(class_name, function_name, result)
			print "ope", self.args[0], left_type, right_type, direccion
			pOper.append(self.args[0])
			numtipo = cubo(left_type, right_type, self.args[0])
			dir_temp[pointerdirtemp[numtipo]] = " " + str(lefty) + " - " + str(direccion)
			cuadruplos.append([self.args[0], lefty, direccion, pointerdirtemp[numtipo]])
			pointerdirtemp[numtipo] += 1
			return numtipo, pointerdirtemp[numtipo] - 1 
			#if self.args[1] is not None:
				#print "SIGN", self.args[1].type, "NEXT", self.args[1].args[0]
		elif self.type == "unario":
			left_type, direccion = self.args[1].expression(class_name, function_name, result)
			print "unario", self.args[0], left_type 
			return -1, 1
			#if self.args[1] is not None:
				#print "SIGN", self.args[1].type, "NEXT", self.args[1].args[0]
		elif self.type == "integer":
			#print "ENTERO"
			dir_cons[pointerdirconst[1]] = int(self.args[0])
			pilaO.append(pointerdirconst[1])
			pointerdirconst[1]+= 1
			return 1, pointerdirconst[1] - 1
		elif self.type == "float":
			dir_cons[pointerdirconst[2]] = float(self.args[0])
			pilaO.append(pointerdirconst[2])
			pointerdirconst[2]+= 1
			return 2, pointerdirconst[2] - 1
		elif self.type == "bool":
			print "BOLEANO"
			if self.args[0] == "true":
				valor = True
			else:
				valor = False
			dir_cons[pointerdirconst[3]] = valor
			pilaO.append(pointerdirconst[3])
			pointerdirconst[3]+= 1
			return 3, pointerdirconst[3] - 1
		elif self.type == "bit":
			dir_cons[pointerdirconst[4]] = self.args[0]
			pilaO.append(pointerdirconst[4])
			pointerdirconst[4]+= 1
			return 4, pointerdirconst[4] - 1
		elif self.type == "string":
			dir_cons[pointerdirconst[5]] = self.args[0]
			pilaO.append(pointerdirconst[5])
			pointerdirconst[5]+= 1
			return 5, pointerdirconst[5] - 1
		elif self.type == "identifier":
			table = result[class_name] if function_name == "global" else result[class_name][function_name]
			var_type = None
			pilaO.append(dir_global.keys()[dir_global.values().index(self.args[0])])
			for t in table:
				tableiter = result[class_name][t] if function_name == "global" else result[class_name][function_name][t]
				if self.args[0] in tableiter:
					var_type = t
					break
			if not var_type:
				raise Exception("Variable no declarada " + self.args[0])
			return var_type, dir_global.keys()[dir_global.values().index(self.args[0])]
		elif self.type == "llamarfuncion":
			clase = class_name
			funcion = self.args[0]
			if "." in self.args[0]:
				llamadafuncion = self.args[0].rsplit(".")
				clase = llamadafuncion[0]
				funcion = llamadafuncion[1]
			if clase not in result:
				raise Exception("Clase no definida " + clase)
			if funcion not in result[clase]:
				raise Exception("Funcion no definida " + funcion)
			var_tipos = {'int' : 1, 'float' : 2, 'bool' : 3, 'bit' : 4, 'String' : 5}
			return var_tipos[result[clase][funcion]["retorno"]], 1

		elif self.type == "asignacion":
			table = result[class_name] if function_name == "global" else result[class_name][function_name]
			if len(self.args) == 3:
				var_type = None
				for t in table:
					tableiter = result[class_name][t] if function_name == "global" else result[class_name][function_name][t]
					if self.args[1] in tableiter:
						var_type = t
						break
				if not var_type:
					raise Exception("Variable no declarada " + self.args[1])
				tipo, direccion = self.args[2].expression(class_name, function_name, result)
				print direccion, "asignn", 
				cuadruplos.append([16, direccion," " , dir_global.keys()[dir_global.values().index(self.args[1])]])
				print cubo(var_type, tipo, 16) == -1, var_type, tipo, "cubo"
				if cubo(var_type, tipo, 16) == -1:
					raise Exception("Tipo no compatible " + self.args[1])
			else:
				tipo, direccion = self.args[0].expression(class_name, function_name, result)
				print direccion, "asignn"
			return tipo, direccion
		print "missing", self.type


	def semantic_body(self, class_name, function_name, result):
		var_tipos = {'int' : 1, 'float' : 2, 'bool' : 3, 'bit' : 4, 'String' : 5}
		if self.type == "declaracion":
			table = result[class_name] if function_name == "global" else result[class_name][function_name]
			names = self.args[1]
			tipo = var_tipos[self.args[0].args[0]]
			#print "NAMES", names
			if tipo not in table:
				table[tipo] = names
				for i in range(len(names)):
					dir_global[pointerdir[tipo]] = names[i]
					pointerdir[tipo] = pointerdir[tipo] + 1
			else:
				for x in range(len(names)):
					variable = names.pop()
					if variable in table[tipo]:
						raise Exception("Variable ya declarada: " + variable)
					else:
						table[tipo].append(variable)
						dir_global[pointerdir[tipo]] = variable
						pointerdir[tipo] = pointerdir[tipo] + 1
		
		elif self.type == "escritura":
			names = self.args[1]
			for i in range(len(names)):
				tip, direccion = self.args[1][i].expression(class_name, function_name, result)
				print tip, direccion, "escritura"
				cuadruplos.append([30, " ", " ", direccion])

		elif self.type == "asignacion":
			self.expression(class_name, function_name, result)
		elif self.type == "accesibilidad":
			pass
		elif self.type == "for":
			if self.args[0] is not None:
				tipo, direccion = self.args[0].expression(class_name, function_name, result)
				antesexp = len(cuadruplos)
			if self.args[1] is not None:
				tipo2, direccion2 = self.args[1].expression(class_name, function_name, result)
				if tipo2 != 3:
					raise Exception("Condicion debe ser tipo bool")
				gotof = [31, direccion2, " ", " "]
				cuadruplos.append(gotof)
				lena = len(cuadruplos)
			if self.args[2] is not None:
				tipo3, direccion3 = self.args[2].expression(class_name, function_name, result)
			result = self.args[3].semantic_body(class_name, function_name, result)
			goto = [32, " ", " ", antesexp - len(cuadruplos)]
			cuadruplos.append(goto)
			gotof[3] = len(cuadruplos) - lena

			
			
		elif self.type == "condicion":
			tipo, direccion = self.args[0].expression(class_name, function_name, result)
			if tipo != 3:
				raise Exception("Condicion debe ser tipo bool")
			#GOTO en falso
			gotof = [31, direccion, " ", " "]
			cuadruplos.append(gotof)
			lena = len(cuadruplos)
			result = self.args[1].semantic_body(class_name, function_name, result)
			goto = [32, " ", " ", 0]
			cuadruplos.append(goto)
			gotof[3] = len(cuadruplos) - lena
			if self.args[2] is not None:
				lenelsea = len(cuadruplos)
				result = self.args[2].semantic_body(class_name, function_name,result)
				goto[3] = len(cuadruplos) - lenelsea
		elif self.type == "while":
			antesexpr = len(cuadruplos)
			tipo, direccion = self.args[0].expression(class_name, function_name, result)
			if tipo != 3:
				raise Exception("Condicion debe ser tipo bool")
			#GOTO en falso
			gotof = [31, direccion, " ", " "]
			cuadruplos.append(gotof)
			lena = len(cuadruplos)
			result = self.args[1].semantic_body(class_name, function_name, result)
			goto = [32, "", "", antesexpr - len(cuadruplos) - 1 ]
			cuadruplos.append(goto)
			gotof[3] = len(cuadruplos) - lena


		elif self.type == "funcion":
			nombrfunc = self.args[0]
			if nombrfunc in result[class_name]:
				raise Exception("Funcion ya definida: " + nombrfunc)
			else:
				if self.args[1] is not None:
					params = self.args[1].args[0]
					print params
					parametros = {}
					for x in range(len(params)):
						parametro = params.pop()
						tipo = var_tipos[parametro[0]]
						if tipo not in parametros:
							parametros[tipo] = [parametro[1]]
							result[class_name][self.args[0]][tipo] = [parametro[1]]
						else:
							parametros[tipo].append(parametro[1])
							result[class_name][self.args[0]][tipo].append(parametro[1])
					print parametros
					print self.args[2].args[0]
					result[class_name][self.args[0]]["parametros_func"] = parametros
				
				if self.args[2] is not None and self.args[2].args[0] > 0:
					result[class_name][self.args[0]]["retorno"] = self.args[2].args[0]
				if self.args[3] is not None:
					result = self.args[3].semantic_body(class_name, self.args[0], result)
		elif self.type == "bloque":
			if self.args[0] is not None:
				result = self.args[0].semantic_body(class_name, function_name, result)
		elif self.type == "estatuto":
			if self.args[0] is not None:
				result = self.args[0].semantic_body(class_name, function_name, result)
		elif self.type == "bloque2":
			if self.args[0] is not None:
				result = self.args[0].semantic_body(class_name, function_name, result)
			if len(self.args) > 1 and self.args[1] is not None:
				result = self.args[1].semantic_body(class_name, function_name, result)

		elif self.type == "clase22":
			if self.args[0] is not None:
				result = self.args[0].semantic_body(class_name, function_name, result)

			if len(self.args) > 1 and self.args[1] is not None:
				result = self.args[1].semantic_body(class_name, function_name, result)
		elif self.type == "clase2":


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

		
start = 'programa'

def p_programa(t):
	'programa : imports prog2'
	t[0] = Node('programa',t[1], t[2])

def p_imports(t):
	"""imports : importar imports
	|
	"""
	if len(t) > 1:
		t[0] = Node('imports', t[1], t[2]) 

def p_prog2(t):
	"""prog2 : codigo prog2
	|  main
	"""
	if len(t) == 3:
		t[0] = Node('prog2',t[1],t[2])
	else:
		t[0] = Node('prog2', t[1])

def p_importar(t):
	'importar : IMPORT IDENTIFIER'
	t[0] = Node('importar', t[2])

def p_codigo(t):
	"""codigo : clase
	| funcion"""
	#| interfaz
	#"""
	t[0] = Node ('codigo', t[1])

def p_main(t):
	"""main : CLASS MAIN clase1 CURLY_A clase2 CURLY_C
	"""
	t[0] = Node('main', t[2], t[3], t[5])
	
def p_clase(t):
	"""clase : CLASS IDENTIFIER clase1 CURLY_A clase2 CURLY_C
	"""
	t[0] = Node('clase', t[2], t[3], t[5])

def p_clase1(t):
	"""clase1 : EXTENDS IDENTIFIER clase11
	|
	"""
	if len(t) > 1:
		t[0] = Node('clase1', t[1], t[2], t[3])

def p_clase11(t):
	"""clase11 : COMMA IDENTIFIER clase11
	|
	"""
	if len(t) > 1:
		t[0] = Node('clase11', t[2], t[3])

def p_clase2(t):
	"""clase2 :	estatuto clase2
	| accesibilidad clase22
	|
	"""
	if len(t) > 1:
		t[0] = Node('clase2', t[1], t[2])
	  
def p_clase22(t):
	"""clase22 : declaracion clase2 
	| funcion clase2
	"""
	t[0] = Node('clase22', t[1], t[2])
def p_estatuto(t):
	"""estatuto : declaracion
	 | asignacion 
	 | condicion
	 | escritura
	 | ciclo
	 | retorna
	 | BREAK
	 | CONTINUE
	"""
	t[0] = Node('estatuto', t[1])

def p_asignacion(t):
	"""asignacion : IDENTIFIER asignacion_signo expresion
	| expresion
	| identifier
	"""
	if len(t) == 4:
		t[0] = Node('asignacion',t[2],t[1],t[3])
	else:
		t[0] = Node('asignacion',t[1])

def p_asignacion_signo(t):
	"""asignacion_signo : ASEQ
	| PLUSEQ
	| MINEQ
	| MULTEQ
	| DIVEQ 
	"""
	t[0] = Node('asignacion_signo', t[1])

def p_condicion(t):
	"""condicion : IF asignacion bloque condicion1
	"""
	t[0] = Node('condicion', t[2], t[3], t[4])

def p_condicion1(t):
	"""condicion1 : ELSE bloque
	|	
	"""
	if len(t) > 1:
		t[0] = t[2]

def p_escritura(t):
	"""escritura : PRINT asignacion escritura2 
	"""
	if t[3] is None: 
		t[0] = Node('escritura', t[1], [t[2]])
	else:
		t[0] = Node('escritura', t[1], [t[2]] + t[3])



def p_escritura2(t):
	"""escritura2 : COMMA asignacion escritura2
	|
	"""
	if len(t) > 1:
		if t[3] is None: 
			t[0] = [t[2]]
		else:
			t[0] = [t[2]] + t[3]
#def p_escritura(t):
#	"""escritura : PRINT escritura1
#	"""
#	t[0] = Node('escritura', t[2])
#
#def p_escritura1(t):
#	"""escritura1 : asignacion escritura2
#	"""
#	t[0] = Node('escritura1', t[1], t[2])
#
#def p_escritura2(t):
#	"""escritura2 : COMMA escritura1
#	|
#	"""
#	if len(t) > 1:
#		t[0] = Node('escritura2', t[2])

def p_ciclo(t):
	"""ciclo : FOR asignacion bloque
	| FOR ciclo1 SEMICOLON ciclo2 SEMICOLON ciclo3 bloque
	"""
	print len(t), "tamanio"
	if len (t) == 4:
		t[0] = Node('while', t[2], t[3])
	else:
	 	t[0] = Node('for', t[2], t[4], t[6], t[7])

def p_ciclo1(t):
	"""ciclo1 : asignacion
	|
	"""
	if len(t) > 1:
		t[0] = t[1]

def p_ciclo2(t):
	"""ciclo2 : asignacion
	|
	"""
	if len(t) > 1:
		t[0] = t[1]


def p_ciclo3(t):
	"""ciclo3 : asignacion
	|
	"""
	if len(t) > 1:
		t[0] = t[1]


def p_funcion(t):
	"""funcion : FUNCTION IDENTIFIER PARENTHESIS_A funcion1 PARENTHESIS_C funcion3 bloque
	"""
	t[0] = Node('funcion', t[2], t[4], t[6], t[7])

def p_funcion1(t):
	"""funcion1 : tipo IDENTIFIER funcion2
	|
	"""
	if len(t) > 1:
		if t[3] is None: 
			t[0] = Node('funcion1', [[t[1].args[0], t[2]]])
		else:
			t[0] = Node('funcion1', [[t[1].args[0], t[2]]] + t[3])

def p_funcion2(t):
	"""funcion2 : COMMA tipo IDENTIFIER funcion2
	|
	"""
	if len(t) > 1:
		if t[4] is None: 
			t[0] = [[t[2].args[0], t[3]]]
		else:
			t[0] = [[t[2].args[0], t[3]]] + t[4]

def p_funcion3(t):
	"""funcion3 : PARENTHESIS_A tipo PARENTHESIS_C
	|
	"""
	if len(t) > 1:
		t[0] = Node('funcion3', t[2].args[0])

#def p_interfaz(t):
#	"""interfaz : INTERFACE IDENTIFIER interfaz1 CURLY_A interfaz2 CURLY_C
#	"""
#	t[0] = Node('interfaz', t[2], t[3], t[5])
#
#def p_interfaz1(t):
#	"""interfaz1 : EXTENDS IDENTIFIER interfaz11
#	|
#	"""
#	if len(t) > 1:
#		t[0] = Node('interfaz1', t[1], t[2], t[3])
#
#def p_interfaz11(t):
#	"""interfaz11 : COMMA IDENTIFIER interfaz11
#	|
#	"""
#	if len(t) > 1:
#		t[0] = Node('interfaz11', t[2], t[3])
#
#def p_interfaz2(t):
#	"""interfaz2 :  accesibilidad interfaz22
#	|
#	"""
#	if len(t) > 1:
#		t[0] = Node('interfaz2', t[1], t[2])
#	  
#def p_interfaz22(t):
#	"""interfaz22 : funcion interfaz2
#	| declaracion interfaz2
#	"""
#	t[0] = Node('interfaz22', t[1], t[2])
#
def p_declaracion(t):
	"""declaracion : tipo IDENTIFIER dec22
	"""
	if t[3] is None: 
		t[0] = Node('declaracion', t[1], [t[2]])
	else:
		t[0] = Node('declaracion', t[1], [t[2]] + t[3])



def p_dec22(t):
	"""dec22 : COMMA IDENTIFIER dec22
	|
	"""
	if len(t) > 1:
		if t[3] is None: 
			t[0] = [t[2]]
		else:
			t[0] = [t[2]] + t[3]

def p_accesibilidad(t):
	"""accesibilidad : PUBLIC
	| PRIVATE
	"""
	t[0] = Node('accesibilidad', t[1])

def p_bloque(t):
	"""bloque : CURLY_A bloque2 CURLY_C
	"""
	t[0] = Node('bloque', t[2])

def p_bloque2(t):
	"""bloque2 : estatuto bloque2
	|
	"""
	if len(t) > 1:
		t[0] = Node('bloque2', t[1], t[2])

def p_retorna(t):
	"""retorna : RETURN asignacion
	"""
	t[0] = Node('retorna', t[2])

def p_expresion(t):
	"""expresion : expresion2 expresioni
	"""
	if t[2] is None:
		t[0] = t[1]
	else:
		t[0] = Node('expresion', t[2][0], t[1], t[2][1])

def p_expresioni(t):
	"""expresioni : OR expresion
	|
	"""
	if len(t) > 1:
		t[0] = (8, t[2])

def p_expresion2(t):
	"""expresion2 : expresion3 expresion2i
	"""
	if t[2] is None:
		t[0] = t[1]
	else:
		t[0] = Node('expresion', t[2][0], t[1], t[2][1])

def p_expresion2i(t):
	"""expresion2i : AND expresion2
	|
	"""
	if len(t) > 1:
		t[0] = (9, t[2])

def p_expresion3(t):
	"""expresion3 : expresion4 expresion3i
	"""
	if t[2] is None:
		t[0] = t[1]
	else:
		t[0] = Node('expresion', t[2][0], t[1], t[2][1])

def p_expresion3i(t):
	"""expresion3i : ORB expresion3
	|
	"""
	if len(t) > 1:
		t[0] = (24, t[2])

def p_expresion4(t):
	"""expresion4 : expresion5 expresion4i
	"""
	if t[2] is None:
		t[0] = t[1]
	else:
		t[0] = Node('expresion', t[2][0], t[1], t[2][1])

def p_expresion4i(t):
	"""expresion4i : XOR expresion4
	|
	"""
	if len(t) > 1:
		t[0] = (23, t[2])

def p_expresion5(t):
	"""expresion5 : expresion6 expresion5i
	"""
	if t[2] is None:
		t[0] = t[1]
	else:
		t[0] = Node('expresion', t[2][0], t[1], t[2][1])

def p_expresion5i(t):
	"""expresion5i : ANDB expresion5
	|
	"""
	if len(t) > 1:
		t[0] = (25, t[2])

def p_expresion6(t):
	"""expresion6 : expresion7 expresion6i
	"""
	if t[2] is None:
		t[0] = t[1]
	else:
		t[0] = Node('expresion', t[2][0], t[1], t[2][1])

def p_expresion6i(t):
	"""expresion6i : EQ expresion6
	| DIF expresion6
	|
	"""
	if len(t) > 1:
		if t[1] == "==":
			t[0] = (10, t[2])
		if t[1] == "!=":
			t[0] = (11, t[2])
	
def p_expresion7(t):
	"""expresion7 : expresion8 expresion7i
	"""
	if t[2] is None:
		t[0] = t[1]
	else:
		t[0] = Node('expresion', t[2][0], t[1], t[2][1])

def p_expresion7i(t):
	"""expresion7i : SHR expresion7
	| SHL expresion7
	|
	"""
	if len(t) > 1:
		if t[1] == ">>":
			t[0] = (26, t[2])
		if t[1] == "<<":
			t[0] = (27, t[2])
def p_expresion8(t):
	"""expresion8 : expresion9 expresion8i 
	"""
	if t[2] is None:
		t[0] = t[1]
	else:
		t[0] = Node('expresion', t[2][0], t[1], t[2][1])

def p_expresion8i(t):
	"""expresion8i : MAY expresion8
	| MEN expresion8
	| MAYQ expresion8
	| MENQ expresion8
	|	
	"""
	if len(t) > 1:
		if t[1] == ">":
			t[0] = (12, t[2])
		if t[1] == "<":
			t[0] = (13, t[2])
		if t[1] == ">=":
			t[0] = (14, t[2])
		if t[1] == "<=":
			t[0] = (15, t[2])
def p_expresion9(t):
	"""expresion9 : termino expresion9i
	"""
	if t[2] is None:
		t[0] = t[1]
	else:
		t[0] = Node('expresion', t[2][0], t[1], t[2][1])

def p_expresion9i(t):
	"""expresion9i : PLUS expresion9
	| MINUS expresion9
	|
	"""
	if len(t) > 1:
		if t[1] == "+":
			t[0] = (1, t[2])
		if t[1] == "-":
			t[0] = (2, t[2])
def p_termino(t):
	"""termino : factor termino2
	"""
	if t[2] is None:
		t[0] = t[1]
	else:
		t[0] = Node('expresion', t[2][0], t[1], t[2][1])

def p_termino2(t):
	"""termino2 : MULT termino
	| DIVISION termino
	| MOD termino
	|
	"""
	if len(t) > 1:
		if t[1] == "*":
			t[0] = (3, t[2])
		if t[1] == "/":
			t[0] = (4, t[2])
		if t[1] == "%":
			t[0] = (5, t[2])

def p_factor(t):
	"""factor : exponencial factor2
	"""
	if t[2] is None:
		t[0] = t[1]
	else:
		t[0] = Node('expresion', t[2][0], t[1], t[2][1])

def p_factor2(t):
	"""factor2 : EXP factor
	|
	"""
	if len(t) > 1:
		if t[1] == "**":
			t[0] = (6, t[2])
def p_exponencial(t):
	"""exponencial : PARENTHESIS_A expresion PARENTHESIS_C
	| exponencial2 valor 
	| identifier
	"""
	if len(t) == 2:
		t[0] = t[1]
	elif len(t) == 4:
		t[0] = t[2]
	else:
		if t[1] is None:
			t[0] = t[2]
		else:
			t[0] = Node('unario', t[2], t[1])
def p_exponencial2(t):
	"""exponencial2 : NOT
	| MM
	| PP
	| NEW
	|
	"""
	if len(t) > 1:
		if t[1] == "!":
			t[0] = 7
		if t[1] == "--":
			t[0] = 22
		if t[1] == "++":
			t[0] = 21
		if t[1] == "+":
			t[0] = 1
		if t[1] == "-":
			t[0] = 2
def p_valor(t):
	"""valor : identifier
	| integer
	| float
	| bool
	| string
	| bit
	| read
	"""
	t[0] = t[1]
def p_integer(t):
	"""integer : INTEGER
	"""
	t[0] = Node('integer', t[1])
def p_identifier(t):
	"""identifier : IDENTIFIER llamarfuncion
	| IDENTIFIER
	"""
	if len(t) == 3:
		t[0] = Node('llamarfuncion', t[1], t[2])
	else:
		t[0] = Node('identifier', t[1])
def p_float(t):
	"""float : FLOAT
	"""
	t[0] = Node('float', t[1])
def p_bool(t):
	"""bool : TRUE
	| FALSE
	"""
	t[0] = Node('bool', t[1])
def p_bit(t):
	"""bit : BIT
	"""
	t[0] = Node('bit', t[1])
def p_read(t):
	"""read : READ
	"""
	t[0] = Node('read', t[1])
def  p_llamarfuncion(t):
	"""llamarfuncion : PARENTHESIS_A llamarfuncion3 PARENTHESIS_C
	"""
	if len(t) > 1:
		t[0] = t[2]
	# "." in string

def p_llamarfuncion3(t):
	"""llamarfuncion3 : asignacion llamarfuncion33
	|
	"""
	if len(t) > 1:
		if t[2] is None: 
			t[0] = Node('llamarfuncion3', [t[1]])
		else:
			t[0] = Node('llamarfuncion3', [t[1]] + t[2])

def p_llamarfuncion33(t):
	"""llamarfuncion33 : COMMA asignacion llamarfuncion33
	|
	"""
	if len(t) > 1:
		if t[3] is None: 
			t[0] = [t[2]]
		else:
			t[0] = [t[2]] + t[3]
def p_tipo(t):
	"""tipo : NINTEGER
	| NSTRING
	| NBOOL
	| NFLOAT
	| NBIT
	"""
	t[0] = Node('tipo', t[1])
def p_string(t):
	"""string : TRIPLEQUOTE STRING TRIPLEQUOTE
	"""
	t[0] = Node('string', t[2])

def p_error(t):
	if t is None :
		print "Error de sintaxis !" 
	else : 
		print "error"	
		print t


