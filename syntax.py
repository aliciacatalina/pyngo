from semantics import Node

#Complete program
def p_program(p):
    '''program : functions MODEL LCURLY vars data model statementblock RCURLY'''
    p[0] = Node('program', p[1], p[4], p[5], p[6])

#Functions 
def p_functions(p):
	'''functions : function functions 
				| empty'''
	if len(p) > 2: p[0] = Node('functions', p[1], p[2])
	else : p[0] = p[1]
	
def p_function(p):
	'''function : FUNC ID LPAREN lparameters RPAREN LCURLY vars data statementblock RCURLY'''
	p[0] = Node('function', p[4], p[7], p[8])

def p_lparameters(p):
	'''lparameters : parameter
					| parameter parameters
					| empty'''

def p_parameters(p):
	'''parameters : COMMA parameters
				| empty'''
	#if len(p) > 2 : p[0] = Node('parameters', p[1], p[3])
	#else : p[0] = Node('parameters', p[1])

def p_parameter(p):
	'''parameter : vartype ID'''
	p[0] = Node('parameter', p[1], p[2])

#Variable declaration
def p_vars(p):
	'''vars : varblock
			| empty'''
	p[0] = Node('vars', p[1])

def p_varblock(p):
    'varblock : VARS LCURLY lvars RCURLY'
    p[0]= Node('varblock', p[3])

def p_lvars(p):
	'''lvars : listofvars lvars
			| listofvars
			| empty'''
	if len(p) > 2 : p[0] = Node('lvars', p[1], p[2])
	else:  p[0] = p[1]

def p_listofvars(p):
    '''listofvars : typedeclaration POINTS listofids SEMIC'''
    p[0]= Node('listofvars', p[1], p[3])

#Declaration of types
def p_typedeclaration(p):
	'''typedeclaration : vartype dimensions'''
	p[0] = Node('typedeclaration', p[1])

def p_dimensions(p):
	'''dimensions : LBRACKET expresion RBRACKET dimensions
					| empty'''
	if len(p) > 2 : p[0] = Node('dimensions', p[1], p[3])
	else : p[0] = p[1]
					
def p_listofids(p):
	'''listofids : ID lid'''
	p[0] = Node('listofids', p[1], p[2])

def p_lid(p):
	'''lid : COMMA listofids
			| empty'''
	if len(p) > 2 : p[0] =  p[2]
	else : p[0] =  p[1]

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
	'asign : ID EQUALS expresiones SEMIC'
	p[0] = Node('asign', p[1], p[3])

def p_expresiones(p):
	'''expresiones : expresion COMMA expresiones
					| expresion'''
	if len(p) > 2 : p[0] = Node ('expresiones', p[1], p[3])
	else : p[0] = p[1] 
#Expresions

def p_expresion(p):
	'''expresion : exp
			| exp LESSTHAN exp
			| exp LESSEQUAL exp
			| exp GREATEREQUAL exp
			| exp GREATERTHAN exp
			| exp BETWEEN exp'''
	if len(p) > 2 :
		p[0] = Node('expresion', p[1], p[2], p[3])
	else : p[0] = Node('expresion', p[1])
					
def p_exp(p):
    '''exp : term 
	 | term PLUS exp
	 | term MINUS exp'''
    if len(p) > 2 : p[0]= Node('exp', p[1], p[2], p[3])
    else: p[0]= Node('exp', p[1])

def p_term(p):
	'''term : factor
		| factor STAR term
		| factor SLASH term'''
	if len(p) > 2 :
		p[0] = Node('term', p[1], p[2], p[3])
	else : p[0] = Node('term', p[1])

def p_factor(p):
    '''factor : PLUS constant
	 | MINUS constant
	 | constant
	 | LPAREN expresion RPAREN'''
    if len(p) > 2 : p[0]= Node('factor', p[2])
    else: p[0]= Node('factor', p[1])

#Model

def p_model(p):
	'''model : optimize
			 | optimize where
			 | statementblock
			 | empty'''
	p[0] = Node('model', p[1])

def p_optimize(p):
	'''optimize : MIN LCURLY statement where RCURLY
							| MAX LCURLY statement where RCURLY'''
	p[0] = Node('optimize', p[3], p[4])

#Statements
def p_statement(p):
	'''statement : asign
				| expresion
				| condition
				| write
				| optimize
				| for
				| return
				| build
				| wherecondition'''
	p[0] = Node('statement', p[1])

def p_build(p):
	'''build : BUILD expresion SEMIC'''
	p[0] = Node('build', p[1])

def p_where(p):
	'''where : WHERE LCURLY statementblock RCURLY'''
	p[0] = Node('where', p[3])

def p_wherecondition(p):
	'''wherecondition : CONDITION expresion SEMIC'''
	p[0] = Node('where', p[2])

#Tokens
def p_vartype(p):
	'''vartype : TINT
			| TFLOAT
			| TBOOL'''
	p[0] = Node('vartype', p[1])

def p_constant(p):
	'''constant : CTEI
		| CTEF
		| CTESTRING
		| CTEBOOL
		| id
		| functioncall'''
	p[0] = Node('constant', p[1])

def p_id(p):
	'''id : ID dimensions'''

######
def p_functioncall(p):
	'''functioncall : ID LPAREN expresion RPAREN
						| ID LPAREN CTEI RPAREN
						| ID LPAREN CTEF RPAREN'''
	p[0] = Node('functioncall', p[3])

def p_for(p):
	'''for : FOR ID IN DOT ID LCURLY statementblock RCURLY'''
	p[0] = Node('for', p[7])

def p_condition(p):
	'''condition : 	IF LPAREN expresion RPAREN statementblock SEMIC
				| IF LPAREN expresion RPAREN statementblock ELSE statementblock SEMIC'''
	if len(p) > 8 : p[0] = Node('condition', p[1], p[2], p[3], p[4], p[5], p[7], p[8])
	else : p[0] = Node('condition', p[1], p[2], p[3], p[4], p[5], p[6])

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

def p_return(p):
	'''return : RETURN asign'''
	p[0] = Node('return', p[2])

def p_statementblock(p):
	'''statementblock : statement statementblock
				| statement
				| empty'''
	if len(p) > 2 :
		p[0] = (p[2])
	else : p[0]= (p[1])

def p_empty(p):
    'empty :'
    pass

def p_error(t):
	if t is None :
		print "Syntax error" 
	else : 
		print "Syntax error:"	
		print t


start = 'program'
