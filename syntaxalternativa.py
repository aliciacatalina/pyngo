from semantics import Node
start = 'program'

#Complete program
def p_program(p):
    '''program : MODEL LCURLY vars data model bloque2 RCURLY'''
    p[0] = Node('program', p[1], p[4], p[5], p[6], p[7])

#Functions 
def p_functions(p):
	'''functions : funcion functions 
				| empty'''
	if len(p) > 2: p[0] = Node('functions', p[1], p[2])
	else : p[0] = p[1]

def p_vars(p):
	'''vars : varblock
			| empty'''
	p[0] = Node('vars', p[1])

def p_varblock(p):
    'varblock : VARS LCURLY declaracion RCURLY'
    p[0]= Node('varblock', p[3])

# def p_lvars(p):
# 	'''lvars : listofvars lvars
# 			| listofvars
# 			| empty'''
# 	if len(p) > 2 : p[0] = Node('lvars', p[1], p[2])
# 	else:  p[0] = p[1]

# def p_listofvars(p):
#     '''listofvars : typedeclaration POINTS listofids SEMIC'''
#     p[0]= Node('listofvars', p[1], p[3])

# #Declaration of types
# def p_typedeclaration(p):
# 	'''typedeclaration : tipo dimensions'''
# 	p[0] = Node('typedeclaration', p[1], p[2])

# def p_dimensions(p):
# 	'''dimensions : LBRACKET expresion RBRACKET dimensions
# 					| empty'''
# 	if len(p) > 2 : p[0] = Node('dimensions', p[1], p[3])
# 	else : p[0] = p[1]

def p_model(p):
	'''model : optimize
			 | optimize where
			 | bloque
			 | empty'''
	p[0] = Node('model', p[1])

def p_optimize(p):
	'''optimize : MIN LCURLY estatuto where RCURLY
				| MAX LCURLY estatuto where RCURLY'''
	p[0] = Node('optimize', p[3], p[4])

def p_build(p):
	'''build : BUILD expresion SEMIC'''
	p[0] = Node('build', p[1])

def p_where(p):
	'''where : WHERE LCURLY bloque2 RCURLY'''
	p[0] = Node('where', p[3])

def p_wherecondition(p):
	'''wherecondition : CONDITION expresion SEMIC'''
	p[0] = Node('where', p[2])

def p_estatuto(p):
	"""estatuto : declaracion
	 | asignacion 
	 | condicion
	 | escritura
	 | ciclo
	 | retorna
	 | build
	 | wherecondition
	"""
	p[0] = Node('estatuto', p[1])

#Data
def p_data(p):
	'''data : DATA LCURLY asignmany RCURLY'''
	p[0] = Node('data', p[3])

def p_asignmany(p):
	'''asignmany : asignacion asignmany
						| empty'''
	if len(p) > 2 : p[0] =  Node('asignmany', p[1], p[2])
	else : p[0] =  p[1]

def p_asignacion(p):
	"""asignacion : ID asignacion_signo expresion
	| expresion
	| id
	"""
	if len(p) == 4:
		p[0] = Node('asignacion',p[2],p[1],p[3])
	else:
		p[0] = Node('asignacion',p[1])

def p_asignacion_signo(p):
	"""asignacion_signo : ASEQ
	| PLUSEQ
	| MINEQ
	| MULTEQ
	| DIVEQ 
	"""
	p[0] = Node('asignacion_signo', p[1])

def p_condicion(p):
	"""condicion : IF asignacion bloque condicion1
	"""
	p[0] = Node('condicion', p[2], p[3], p[4])

def p_condicion1(p):
	"""condicion1 : ELSE bloque
	|	
	"""
	if len(p) > 1:
		p[0] = p[2]

def p_escritura(p):
	"""escritura : PRINT asignacion escritura2 
	"""
	if p[3] is None: 
		p[0] = Node('escritura', p[1], [p[2]])
	else:
		p[0] = Node('escritura', p[1], [p[2]] + p[3])



def p_escritura2(p):
	"""escritura2 : COMMA asignacion escritura2
	|
	"""
	if len(p) > 1:
		if p[3] is None: 
			p[0] = [p[2]]
		else:
			p[0] = [p[2]] + p[3]

def p_ciclo(p):
	"""ciclo : FOR asignacion bloque
	| FOR ciclo1 SEMIC ciclo2 SEMIC ciclo3 bloque
	"""
	print len(p), "tamanio"
	if len (p) == 4:
		p[0] = Node('while', p[2], p[3])
	else:
	 	p[0] = Node('for', p[2], p[4], p[6], p[7])

def p_ciclo1(p):
	"""ciclo1 : asignacion
	|
	"""
	if len(p) > 1:
		p[0] = p[1]

def p_ciclo2(p):
	"""ciclo2 : asignacion
	|
	"""
	if len(p) > 1:
		p[0] = p[1]


def p_ciclo3(p):
	"""ciclo3 : asignacion
	|
	"""
	if len(p) > 1:
		p[0] = p[1]


def p_funcion(p):
	"""funcion : FUNC ID LPAREN funcion1 RPAREN funcion3 bloque
	"""
	p[0] = Node('funcion', p[2], p[4], p[6], p[7])

def p_funcion1(p):
	"""funcion1 : tipo ID funcion2
	|
	"""
	if len(p) > 1:
		if p[3] is None: 
			p[0] = Node('funcion1', [[p[1].args[0], p[2]]])
		else:
			p[0] = Node('funcion1', [[p[1].args[0], p[2]]] + p[3])

def p_funcion2(p):
	"""funcion2 : COMMA tipo ID funcion2
	|
	"""
	if len(p) > 1:
		if p[4] is None: 
			p[0] = [[p[2].args[0], p[3]]]
		else:
			p[0] = [[p[2].args[0], p[3]]] + p[4]

def p_funcion3(p):
	"""funcion3 : LPAREN tipo RPAREN
	|
	"""
	if len(p) > 1:
		p[0] = Node('funcion3', p[2].args[0])

#def p_interfaz(p):
#	"""interfaz : INTERFACE ID interfaz1 LCURLY interfaz2 RCURLY
#	"""
#	p[0] = Node('interfaz', p[2], p[3], p[5])
#
#def p_interfaz1(p):
#	"""interfaz1 : EXTENDS ID interfaz11
#	|
#	"""
#	if len(p) > 1:
#		p[0] = Node('interfaz1', p[1], p[2], p[3])
#
#def p_interfaz11(p):
#	"""interfaz11 : COMMA ID interfaz11
#	|
#	"""
#	if len(p) > 1:
#		p[0] = Node('interfaz11', p[2], p[3])
#
#def p_interfaz2(p):
#	"""interfaz2 :  accesibilidad interfaz22
#	|
#	"""
#	if len(p) > 1:
#		p[0] = Node('interfaz2', p[1], p[2])
#	  
#def p_interfaz22(p):
#	"""interfaz22 : funcion interfaz2
#	| declaracion interfaz2
#	"""
#	p[0] = Node('interfaz22', p[1], p[2])
#
def p_declaracion(p):
	"""declaracion : tipo POINTS ID dec22 SEMIC
	"""
	if p[3] is None: 
		p[0] = Node('declaracion', p[1], [p[2]])
	else:
		p[0] = Node('declaracion', p[1], [p[2]] + p[3])



def p_dec22(p):
	"""dec22 : COMMA ID dec22
	|
	"""
	if len(p) > 1:
		if p[3] is None: 
			p[0] = [p[2]]
		else:
			p[0] = [p[2]] + p[3]


def p_bloque(p):
	"""bloque : LCURLY bloque2 RCURLY
	"""
	p[0] = Node('bloque', p[2])

def p_bloque2(p):
	"""bloque2 : estatuto bloque2
	|
	"""
	if len(p) > 1:
		p[0] = Node('bloque2', p[1], p[2])

def p_retorna(p):
	"""retorna : RETURN asignacion
	"""
	p[0] = Node('retorna', p[2])

def p_expresion(p):
	"""expresion : expresion2 expresioni
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_expresioni(p):
	"""expresioni : OR expresion
	|
	"""
	if len(p) > 1:
		p[0] = (8, p[2])

def p_expresion2(p):
	"""expresion2 : expresion3 expresion2i
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_expresion2i(p):
	"""expresion2i : AND expresion2
	|
	"""
	if len(p) > 1:
		p[0] = (9, p[2])

def p_expresion3(p):
	"""expresion3 : expresion4 expresion3i
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_expresion3i(p):
	"""expresion3i : ORB expresion3
	|
	"""
	if len(p) > 1:
		p[0] = (24, p[2])

def p_expresion4(p):
	"""expresion4 : expresion5 expresion4i
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_expresion4i(p):
	"""expresion4i : XOR expresion4
	|
	"""
	if len(p) > 1:
		p[0] = (23, p[2])

def p_expresion5(p):
	"""expresion5 : expresion6 expresion5i
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_expresion5i(p):
	"""expresion5i : ANDB expresion5
	|
	"""
	if len(p) > 1:
		p[0] = (25, p[2])

def p_expresion6(p):
	"""expresion6 : expresion7 expresion6i
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_expresion6i(p):
	"""expresion6i :  expresion6
	| DIF expresion6
	|
	"""
	if len(p) > 1:
		if p[1] == "==":
			p[0] = (10, p[2])
		if p[1] == "!=":
			p[0] = (11, p[2])
	
def p_expresion7(p):
	"""expresion7 : expresion8 expresion7i
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_expresion7i(p):
	"""expresion7i : SHR expresion7
	| SHL expresion7
	|
	"""
	if len(p) > 1:
		if p[1] == ">>":
			p[0] = (26, p[2])
		if p[1] == "<<":
			p[0] = (27, p[2])
def p_expresion8(p):
	"""expresion8 : expresion9 expresion8i 
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_expresion8i(p):
	"""expresion8i : GREATERTHAN expresion8
	| LESSTHAN expresion8
	| GREATEREQUAL expresion8
	| LESSEQUAL expresion8
	|	
	"""
	if len(p) > 1:
		if p[1] == ">":
			p[0] = (12, p[2])
		if p[1] == "<":
			p[0] = (13, p[2])
		if p[1] == ">=":
			p[0] = (14, p[2])
		if p[1] == "<=":
			p[0] = (15, p[2])
def p_expresion9(p):
	"""expresion9 : termino expresion9i
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_expresion9i(p):
	"""expresion9i : PLUS expresion9
	| MINUS expresion9
	|
	"""
	if len(p) > 1:
		if p[1] == "+":
			p[0] = (1, p[2])
		if p[1] == "-":
			p[0] = (2, p[2])
def p_termino(p):
	"""termino : factor termino2
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_termino2(p):
	"""termino2 : STAR termino
	| SLASH termino
	| MOD termino
	|
	"""
	if len(p) > 1:
		if p[1] == "*":
			p[0] = (3, p[2])
		if p[1] == "/":
			p[0] = (4, p[2])
		if p[1] == "%":
			p[0] = (5, p[2])

def p_factor(p):
	"""factor : exponencial factor2
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_factor2(p):
	"""factor2 : EXP factor
	|
	"""
	if len(p) > 1:
		if p[1] == "**":
			p[0] = (6, p[2])
def p_exponencial(p):
	"""exponencial : LPAREN expresion RPAREN 
	| id
	"""
	if len(p) == 2:
		p[0] = p[1]
	else:
		p[0] = p[2]
	# else:
	# 	if p[1] is None:
	# 		p[0] = p[2]
	# 	else:
	# 		p[0] = Node('unario', p[2], p[1])
# def p_exponencial2(p):
# 	"""exponencial2 : NOT
# 	| MM
# 	| PP
# 	| NEW
# 	|
# 	"""
# 	if len(p) > 1:
# 		if p[1] == "!":
# 			p[0] = 7
# 		if p[1] == "--":
# 			p[0] = 22
# 		if p[1] == "++":
# 			p[0] = 21
# 		if p[1] == "+":
# 			p[0] = 1
# 		if p[1] == "-":
# 			p[0] = 2
def p_valor(p):
	"""valor : id
	| int
	| float
	| bool
	"""
	p[0] = p[1]
def p_int(p):
	"""int : TINT
	"""
	p[0] = Node('int', p[1])
def p_id(p):
	"""id : ID llamarfuncion
	| ID
	"""
	if len(p) == 3:
		p[0] = Node('llamarfuncion', p[1], p[2])
	else:
		p[0] = Node('id', p[1])
def p_float(p):
	"""float : TFLOAT
	"""
	p[0] = Node('float', p[1])
def p_bool(p):
	"""bool : TBOOL
	"""
	p[0] = Node('bool', p[1])

def  p_llamarfuncion(p):
	"""llamarfuncion : LPAREN llamarfuncion3 RPAREN
	"""
	if len(p) > 1:
		p[0] = p[2]
	# "." in string

def p_llamarfuncion3(p):
	"""llamarfuncion3 : asignacion llamarfuncion33
	|
	"""
	if len(p) > 1:
		if p[2] is None: 
			p[0] = Node('llamarfuncion3', [p[1]])
		else:
			p[0] = Node('llamarfuncion3', [p[1]] + p[2])

def p_llamarfuncion33(p):
	"""llamarfuncion33 : COMMA asignacion llamarfuncion33
	|
	"""
	if len(p) > 1:
		if p[3] is None: 
			p[0] = [p[2]]
		else:
			p[0] = [p[2]] + p[3]
def p_tipo(p):
	"""tipo : TINT
	| TBOOL
	| TFLOAT
	"""
	p[0] = Node('tipo', p[1])

def p_empty(p):
    'empty :'
    pass

def p_error(p):
	if p is None :
		print "Error de sintaxis !" 
	else : 
		print "error"	
		print p