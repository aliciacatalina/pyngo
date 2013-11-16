from semantics import Node
start = 'program'

#Complete program
def p_program(p):
    '''program : functions MODEL LCURLY vars data model bloque2 RCURLY'''
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
    'varblock : VARS LCURLY lvars RCURLY'
    p[0]= Node('varblock', p[3])


def p_model(p):
	'''model : optimize
			 | optimize where
			 | bloque2
			 | empty'''
	if len(p) > 2 : p[0] = Node('model', p[1], p[2])
	else : p[0] = Node('model', p[1])

def p_optimize(p):
	'''optimize : MIN LCURLY statement where RCURLY
				| MAX LCURLY statement where RCURLY'''
	p[0] = Node('optimize', p[3], p[4])

def p_build(p):
	'''build : BUILD expresion SEMIC'''
	p[0] = Node('build', p[1], p[2])

def p_where(p):
	'''where : WHERE LCURLY bloque2 RCURLY'''
	p[0] = Node('where', p[3])

def p_wherecondition(p):
	'''wherecondition : CONDITION expresion SEMIC'''
	p[0] = Node('where', p[2])

def p_statement(p):
	"""statement : declaration
	 | asign 
	 | condition
	 | write
	 | ciclo
	 | return
	 | build
	 | wherecondition
	"""
	p[0] = Node('statement', p[1])

#Data
def p_data(p):
	'''data : DATA LCURLY asignmany RCURLY'''
	p[0] = Node('data', p[3])

def p_asignmany(p):
	'''asignmany : asign asignmany
				| empty'''
	if len(p) > 2 : p[0] =  Node('asignmany', p[1], p[2])
	else : p[0] =  p[1]

def p_asign(p):
	"""asign : id asign_signo expresiones SEMIC
			| expresiones"""
	if len(p) > 2 :
		p[0] = Node('asign',p[2],p[1],p[3])
	else : p[0] = Node('asign', p[1])


def p_expresiones(p):
	'''expresiones : expresion COMMA expresiones
					| expresion'''
	if len(p) > 2 : p[0] = Node ('expresiones', p[1], p[3])
	else : p[0] = p[1]

def p_asign_signo(p):
	"""asign_signo : ASEQ
	| PLUSEQ
	| MINEQ
	| MULTEQ
	| DIVEQ
	"""
	p[0] = Node('asign_signo', p[1])

def p_condition(p):
	"""condition : IF asign bloque condition1
	"""
	p[0] = Node('condition', p[2], p[3], p[4])

def p_condition1(p):
	"""condition1 : ELSE bloque
	| empty	
	"""
	if len(p) > 2:
		p[0] = p[2]
	else :
		p[0] = p[1]

def p_write(p):
	"""write : PRINT asign write2 SEMIC
	"""
	if p[3] is None: 
		p[0] = Node('write',[p[2]])
	else:
		p[0] = Node('write', [p[2]] + p[3])

def p_write2(p):
	"""write2 : COMMA asign write2
	| empty
	"""
	if len(p) > 2:
		if p[3] is None: 
			p[0] = [p[2]]
		else:
			p[0] = [p[2]] + p[3]
	else : p[0] = p[1]

#change loop
def p_ciclo(p):
	"""ciclo : FOR ID IN DOT ID bloque
	"""
	p[0] = Node('for', p[2], p[3], p[4], p[5])

# def p_ciclo1(p):
# 	"""ciclo1 : asign
# 	|
# 	"""
# 	if len(p) > 1:
# 		p[0] = p[1]

# def p_ciclo2(p):
# 	"""ciclo2 : asign
# 	|
# 	"""
# 	if len(p) > 1:
# 		p[0] = p[1]


# def p_ciclo3(p):
# 	"""ciclo3 : asign
# 	|
# 	"""
# 	if len(p) > 1:
# 		p[0] = p[1]


def p_funcion(p):
	"""funcion : FUNC ID LPAREN funcion1 RPAREN funcion3 bloque
	"""
	p[0] = Node('funcion', p[2], p[4], p[6], p[7])

def p_funcion1(p):
	"""funcion1 : type ID funcion2
	|
	"""
	if len(p) > 1:
		if p[3] is None: 
			p[0] = Node('funcion1', [[p[1].args[0], p[2]]])
		else:
			p[0] = Node('funcion1', [[p[1].args[0], p[2]]] + p[3])

def p_funcion2(p):
	"""funcion2 : COMMA type ID funcion2
	|
	"""
	if len(p) > 1:
		if p[4] is None: 
			p[0] = [[p[2].args[0], p[3]]]
		else:
			p[0] = [[p[2].args[0], p[3]]] + p[4]

def p_funcion3(p):
	"""funcion3 : LPAREN type RPAREN
	|
	"""
	if len(p) > 1:
		p[0] = Node('funcion3', p[2].args[0])

def p_lvars(p):
	'''lvars : declaration lvars
			| empty'''
	if len(p) > 2 : p[0] = Node('lvars', p[1], p[2])
	else:  p[0] = p[1]

def p_declaration(p):
	"""declaration : typedeclaration POINTS ID dec22 SEMIC
	"""
	if p[4] is None: 
		p[0] = Node('declaration', p[1], [p[3]])
	else:
		p[0] = Node('declaration', p[1], [p[3]] + p[4])

def p_typedeclaration(p):
	'''typedeclaration : type dimensions'''
	p[0] = Node('typedeclaration', p[1], p[2])

def p_dimensions(p):
	'''dimensions : LBRACKET expresion RBRACKET dimensions
					| empty'''
	if len(p) > 2 : p[0] = Node('dimensions', p[2], p[4])
	else : p[0] = p[1]

def p_dec22(p):
	"""dec22 : COMMA ID dec22
	| empty
	"""
	if len(p) > 2:
		if p[3] is None: 
			p[0] = [p[2]]
		else:
			p[0] = [p[2]] + p[3]
	else : p[0] = p[1]


def p_bloque(p):
	"""bloque : LCURLY bloque2 RCURLY
	"""
	p[0] = Node('bloque', p[2])

def p_bloque2(p):
	"""bloque2 : statement bloque2
	| empty
	"""
	if len(p) > 2:
		p[0] = Node('bloque2', p[1], p[2])
	else : p[0] = p[1]

def p_return(p):
	"""return : RETURN asign
	"""
	p[0] = Node('return', p[2])

def p_expresion(p):
	"""expresion : expresion2 expresioni
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_expresioni(p):
	"""expresioni : OR expresion
	| empty
	"""
	if len(p) > 2:
		p[0] = (8, p[2])
	else : p[0] = p[1]

def p_expresion2(p):
	"""expresion2 : expresion3 expresion2i
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_expresion2i(p):
	"""expresion2i : AND expresion2
	| empty
	"""
	if len(p) > 2:
		p[0] = (9, p[2])
	else : p[0] = p[1]

def p_expresion3(p):
	"""expresion3 : expresion4 expresion3i
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_expresion3i(p):
	"""expresion3i : ORB expresion3
	| empty
	"""
	if len(p) > 2:
		p[0] = (24, p[2])
	else : p[0] = p[1]

def p_expresion4(p):
	"""expresion4 : expresion5 expresion4i
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_expresion4i(p):
	"""expresion4i : XOR expresion4
	| empty
	"""
	if len(p) > 2:
		p[0] = (23, p[2])
	else : p[0] = p[1]

def p_expresion5(p):
	"""expresion5 : expresion6 expresion5i
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_expresion5i(p):
	"""expresion5i : ANDB expresion5
	| empty
	"""
	if len(p) > 2:
		p[0] = (25, p[2])
	else : p[0] = p[1]

def p_expresion6(p):
	"""expresion6 : expresion7 expresion6i
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_expresion6i(p):
	"""expresion6i :  EQ expresion6
	| DIF expresion6
	| empty
	"""
	if len(p) > 2:
		if p[1] == "==":
			p[0] = (10, p[2])
		if p[1] == "!=":
			p[0] = (11, p[2])
	else : p[0] = p[1]
	
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
	| empty
	"""
	if len(p) > 2:
		if p[1] == ">>":
			p[0] = (26, p[2])
		if p[1] == "<<":
			p[0] = (27, p[2])
	else : p[0] = p[1]
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
	| empty	
	"""
	if len(p) > 2:
		if p[1] == ">":
			p[0] = (12, p[2])
		if p[1] == "<":
			p[0] = (13, p[2])
		if p[1] == ">=":
			p[0] = (14, p[2])
		if p[1] == "<=":
			p[0] = (15, p[2])
	else : p[0] = p[1]
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
	| empty
	"""
	if len(p) > 2:
		if p[1] == "+":
			p[0] = (1, p[2])
		if p[1] == "-":
			p[0] = (2, p[2])
	else : p[0] = p[1]
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
	| empty
	"""
	if len(p) > 2:
		if p[1] == "*":
			p[0] = (3, p[2])
		if p[1] == "/":
			p[0] = (4, p[2])
		if p[1] == "%":
			p[0] = (5, p[2])
	else : p[0] = p[1]

def p_factor(p):
	"""factor : exponencial factor2
	"""
	if p[2] is None:
		p[0] = p[1]
	else:
		p[0] = Node('expresion', p[2][0], p[1], p[2][1])

def p_factor2(p):
	"""factor2 : EXP factor
	| empty
	"""
	if len(p) > 2:
		if p[1] == "**":
			p[0] = (6, p[2])
	else: p[0] = p[1]

def p_exponencial(p):
	"""exponencial : LPAREN expresion RPAREN
	| exponencial2 valor 
	"""
	if len(p) == 2:
		p[0] = p[1]
	elif len(p) == 4:
		p[0] = p[2]
	else:
		if p[1] is None:
			p[0] = p[2]
		else:
			p[0] = Node('unario', p[2], p[1])

def p_exponencial2(p):
	"""exponencial2 : NOT
	| MM
	| PP
	| NEW
	| empty
	"""
	if len(p) > 2:
		if p[1] == "!":
			p[0] = 7
		if p[1] == "--":
			p[0] = 22
		if p[1] == "++":
			p[0] = 21
		if p[1] == "+":
			p[0] = 1
		if p[1] == "-":
			p[0] = 2
	else : p[0] = p[1]

def p_valor(p):
	"""valor : id
	| int
	| float
	"""
	p[0] = p[1]

def p_int(p):
	"""int : CTEI
	"""
	p[0] = Node('int', p[1])

def p_id(p):
	"""id : ID llamarfuncion
	| ID dimensions
	"""
	if len(p) == 3:
		p[0] = Node('llamarfuncion', p[1], p[2])
	else:
		p[0] = Node('id', p[1])

def p_float(p):
	"""float : CTEF
	"""
	p[0] = Node('float', p[1])
# def p_bool(p):
# 	"""bool : CTEBool
# 	"""
#	p[0] = Node('bool', p[1])

def  p_llamarfuncion(p):
	"""llamarfuncion : LPAREN llamarfuncion3 RPAREN
	"""
	if len(p) > 1:
		p[0] = p[2]
	# "." in string

def p_llamarfuncion3(p):
	"""llamarfuncion3 : asign llamarfuncion33
	| empty
	"""
	if len(p) > 2:
		if p[2] is None: 
			p[0] = Node('llamarfuncion3', [p[1]])
		else:
			p[0] = Node('llamarfuncion3', [p[1]] + p[2])
	else : p[0] = p[1]

def p_llamarfuncion33(p):
	"""llamarfuncion33 : COMMA asign llamarfuncion33
	| empty
	"""
	if len(p) > 2:
		if p[3] is None: 
			p[0] = [p[2]]
		else:
			p[0] = [p[2]] + p[3]
	else : p[0] = p[1]

def p_type(p):
	"""type : TINT
	| TBOOL
	| TFLOAT
	"""
	p[0] = Node('type', p[1])

def p_empty(p):
    'empty :'
    pass

def p_error(p):
	if p is None :
		print "Error de sintaxis !" 
	else : 
		print "error"	
		print p