from semantics import *
start = 'program'
def p_constant(p):
	'''constant : CTEI
		| CTEF
		| CTESTRING
		| CTEBOOL
		| ID
		| functioncall'''
	p[0] = Node('constant', p[1])

def p_functioncall(p):
	'''functioncall : ID LPAREN expresion RPAREN
						| ID LPAREN CTEI RPAREN
						| ID LPAREN CTEF RPAREN'''
	p[0] = Node('functioncall', p[3])

def p_data(p):
	'''data : DATA LCURLY asignmany RCURLY'''
	p[0] = Node('data', p[3])

def p_asignmany(p):
	'''asignmany : asign SEMIC asignlist
						| asign'''
	#p[0] = Node('asignmany', p[1], p[3])

def p_asignlist(p):
	'''asignlist : empty
				| asignmany'''
	p[0] = Node('asignlist', p[1])

def p_optimize(p):
	'''optimize : MIN EQUALS restrictions
							| MAX EQUALS restrictions'''
	p[0] = Node('optimize', p[3])

def p_restrictions(p):
	'''restrictions : WHERE restrictions2'''
	p[0]  = Node('restrictions', p[2])

def p_restrictions2(p):
	'''restrictions2 : expresion
					| sum SEMIC forlist'''
	if len(p) > 2 : p[0] = Node('restrictions2', p[1], p[3])
	else : p[0] = Node('restrictions2', p[1])

def p_for(p):
	'''for : FOR ID IN DOT ID LBRACKET statement RBRACKET'''
	p[0] = Node('for', p[7])

def p_forlist(p):
	'''forlist : for SEMIC lfor'''
	p[0] = Node('forlist', p[1], p[3])

def p_lfor(p):
	'''lfor : empty
			| forlist'''
	p[0] = Node('lfor', p[1])

def p_sum(p):
	'''sum : SUM LPAREN ID POINTS expresion RPAREN'''
	p[0] = Node('sum', p[5])

def p_factor(p):
    '''factor : PLUS constant
	 | MINUS constant
	 | constant
	 | LPAREN expresion RPAREN'''
    if len(p) > 2 : p[0]= Node('factor', p[2])
    else: p[0]= Node('factor', p[1])

def p_term(p):
	'''term : factor
		| factor STAR term
		| factor SLASH term'''
	if len(p) > 2 :
		p[0] = Node('term', p[1], p[2], p[3])
	else : p[0] = Node('term', p[1])

def p_condition(p):
	'''condition : 	IF LPAREN expresion RPAREN block SEMIC
				| IF LPAREN expresion RPAREN block ELSE block SEMIC'''
	if len(p) > 8 : p[0] = Node('condition', p[1], p[2], p[3], p[4], p[5], p[7], p[8])
	else : p[0] = Node('condition', p[1], p[2], p[3], p[4], p[5], p[6])

def p_expresiones(p):
	'''expresiones : expresion COMMA expresiones
					| expresion'''

def p_expresion(p):
	'''expresion : exp
			| exp LESSTHAN exp
			| exp GREATERTHAN exp
			| exp BETWEEN exp'''
	if len(p) > 2 :
		p[0] = Node('expresion', p[3])
	else : p[0] = Node('expresion', p[1])
					
def p_exp(p):
    '''exp : term
	 | term PLUS exp
	 | term MINUS exp'''
    if len(p) > 2 : p[0]= Node('exp', p[1], p[2], p[3])
    else: p[0]= Node('exp', p[1])

def p_write(p):
	'''write : PRINT LPAREN write2 RPAREN SEMIC'''
	p[0] = Node('write', p[3])

def p_write2(p):
	'''write2 : expresion
				| CTESTRING
				| expresion DOT write2
				| CTESTRING DOT write2'''
	if len(p) > 2 : p[0] = Node('write2', p[1], p[3])
	else : p[0] = Node('write2', p[1])


def p_asign(p):
	'asign : ID EQUALS expresiones SEMIC'
	p[0] = Node('asign', p[1], p[2], p[3], p[4])

def p_statement(p):
	'''statement : asign
				| condition
				| write
				| optimize
				| loop
				| return'''
	p[0] = Node('statement', p[1])

def p_loop(p):
	'''loop : for'''
	p[0] = Node('loop', p[1])

def p_return(p):
	'''return : RETURN asign'''
	p[0] = Node('return', p[2])

def p_function(p):
	'''function : FUNC ID LPAREN manyargs RPAREN LCURLY varsdata block2 RCURLY'''
	print "function"
	p[0] = Node('function', p[4], p[7], p[8])

def p_manyargs(p):
	'''manyargs : empty
				| tipo ID liargs'''
	if len(p) > 2 : p[0] = Node('manyargs', p[1], p[3])
	else : p[0] = Node('manyargs', p[1])

def p_liargs(p):
	'''liargs : empty
			| COMMA manyargs'''
	if len(p) > 2 : p[0] = Node('liargs', p[2])
	else : p[0] = Node('liargs', p[1])

def p_block(p):
	'''block : block2
				| LCURLY RCURLY'''
	if len(p) > 3 :
		p[0] = Node('block', p[2])
	else : p[0] = Node('block vacio')

def p_block2(p):
	'''block2 : statement block2
				| statement
				| empty'''
	if len(p) > 2 :
		p[0] = (p[2])
	else : p[0]= (p[1])

def p_tipo(p):
	'''tipo : TINT
			| TFLOAT
			| TBOOL'''
	p[0] = Node('tipo', p[1])

def p_vars(p):
    'vars : VARS LCURLY listofvars RCURLY'
    p[0]= Node('vars', p[3])


def p_matrix(p):
	'''matrix : LBRACKET CTEI RBRACKET LBRACKET CTEI RBRACKET'''
	p[0] = Node('matrix', p[2], p[5])

def p_array(p):
	'''array : LBRACKET CTEI RBRACKET'''
	p[0] = p[2]

def p_declaracion(p):
	'''declaracion : tipo array
					| tipo matrix
					| tipo'''
	p[0] = Node('declaracion', p[1])

def p_lid(p):
	'''lid : COMMA listofids
			| empty'''
	if len(p) > 2 : p[0] = Node('lid', p[2])
	else : p[0] = Node('lid', p[1])

def p_listofids(p):
	'''listofids : ID lid'''
	p[0] = Node('listofids', p[1], p[2])

def p_lvars(p):
	'''lvars : listofvars
			| empty'''
	p[0] = Node('lvars', p[1])

def p_listofvars(p):
    '''listofvars : declaracion POINTS listofids SEMIC lvars'''
    p[0]= Node('listofvars', p[1], p[3])

def p_varsdata(p):
	'''varsdata : vars data
			| empty
			| vars'''
	if len(p) > 2 : p[0] = Node('varsdata', p[1], p[2])
	else : p[0] = Node('varsdata', p[1])

def  p_declarefunc(p):
	'''declarefunc : function
			| empty'''
	p[0] = Node('declarefunc', p[1])

def p_declarevars(p):
	'''declarevars : vars
			| empty'''
	p[0] = Node('declarevars', p[1])

def p_program(p):
    '''program : declarevars declarefunc MODEL LCURLY varsdata block2 RCURLY'''
    p[0]= Node('program', p[1], p[2], p[5], p[6])

def p_empty(p):
    'empty :'
    pass

def p_error(t):
	if t is None :
		print "Syntax error" 
	else : 
		print "Syntax error:"	
		print t


