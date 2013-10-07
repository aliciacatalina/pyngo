# patitolex.ply | Lexico de Lenguaje Patito 
# Alicia Gonzalez 1088149 | Compiladores

import ply.lex as lex
import ply.yacc as yacc

start = 'programa' 



def p_error(p):
        raise SyntaxError

tokens = (
		'ID', 
		'STRING',   
		'EQUALS', 
		'STAR', 
		'SLASH', 
		'LPAREN', 
		'RPAREN', 
		'LCURLY', 
		'RCURLY', 
		'POINTS', 
		'LESSTHAN', 
		'GREATERTHAN', 
		'BETWEEN', 
		'PLUS', 
		'MINUS',
		'DOT', 
		'INTEGER', 
		'FLOAT',  
		'IF', 
		'ELSE', 
		'PRINT', 
		'CTEI', 
		'CTEF', 
		'SEMIC', 
		'MAX', 
		'MIN', 
		'FUNC',
		'VARS', 
		'DATA', 
		'MODEL',
		'FOR',
		'SUM', 
		'LBRACKET', 
		'RBRACKET',
		'WHERE', 
		'RETURN' 
)

def t_STRING(t):
	r"'([A-Z]|[a-z]|[0-9])*'"
	return t

def t_FLOAT(t):
	r"[0-9]+(\.[0-9]*)"
	return t

def t_INTEGER(t):
	r"[0-9]+"
	t.value = int(t.value)
	return t

def t_MODEL(t):
	r"model"
	return t

def t_IF(t):
	r"if"
	return t

def t_ELSE(t):
	r"else"
	return t

def t_PRINT(t):
	r"print"
	return t

def t_VARS(t):
	r"vars"
	return t

def t_CTEI(t):
	r"int"
	return t

def t_CTEF(t):
	r"float"
	return t

def t_DATA(t):
	r"data"
	return t

def t_FUNC(t):
	r"func"
	return t

def t_MAX(t):
	r"max"
	return t

def t_MIN(t):
	r"min"
	return t

def t_FOR(t):
	r"for"
	return t

def t_SUM(t):
	r"sum"
	return t

def t_WHERE(t):
	r"where"
	return t



t_EQUALS		= r'='
t_STAR			= r'\*'
t_SLASH			= r'/'
t_LPAREN		= r'\('
t_RPAREN		= r'\)'
t_LCURLY		= r'\{'
t_RCURLY		= r'\}'
t_POINTS		= r':'
t_LESSTHAN		= r'<'
t_GREATERTHAN	= r'>'
t_BETWEEN		= r'<>'
t_PLUS			= r'\+'
t_MINUS			= r'-'
t_SEMIC			= r';'
t_DOT			= r'\.'
t_LBRACKET		= r'\['
t_RBRACKET		= r'\]'
t_ignore        = ' \t\v\r'

def t_ID(t):
        r"[a-z]([A-Z]|[a-z]|[0-9])*"
        return t


def t_error(t):
	print "Caracter no identificado '%s'" % t.value[0]
	t.lexer.skip(1)

# start of CFE grammar

def p_varcte(p):
	'''varcte : INTEGER
		| FLOAT
		| ID'''
	p[0] = ('var', p[1])

def p_factor(p):
    '''factor : PLUS varcte
	 | MINUS varcte
	 | varcte
	 | LPAREN expresion RPAREN'''
    if len(p) > 2 : p[0]= ('factor', p[2])
    else: p[0]= ('factor', p[1])

def p_termino(p):
	'''termino : factor
		| factor STAR termino
		| factor SLASH termino'''
	if len(p) > 2 :
		p[0] = ('termino', p[1], p[2], p[3])
	else : p[0] = ('termino', p[1])

def p_condicion(p):
	'''condicion : 	IF LPAREN expresion RPAREN bloque SEMIC
				| IF LPAREN expresion RPAREN bloque ELSE bloque SEMIC'''
	if len(p) > 8 : p[0] = ('condicion', p[1], p[2], p[3], p[4], p[5], p[7], p[8])
	else : p[0] = ('condicion', p[1], p[2], p[3], p[4], p[5], p[6])

def p_expresion(p):
	'''expresion : exp
			| exp LESSTHAN exp
			| exp GREATERTHAN exp
			| exp BETWEEN exp'''
	if len(p) > 2 :
		p[0] = ('expresion', p[3])
	else : p[0] = ('expresion', p[1])
					
def p_exp(p):
    '''exp : termino
	 | termino PLUS exp
	 | termino MINUS exp'''
    if len(p) > 2 : p[0]= ('exp', p[1], p[2], p[3])
    else: p[0]= ('exp', p[1])

def p_escritura(p):
	'''escritura : PRINT LPAREN escritura2 RPAREN SEMIC'''
	p[0] = ('escritura', p[3])

def p_escritura2(p):
	'''escritura2 : expresion
				| STRING
				| expresion DOT escritura2
				| STRING DOT escritura2'''
	if len(p) > 2 :
		p[0] = (p[3])
	else : p[0] = ( p[1])


def p_asignacion(p):
	'asignacion : ID EQUALS expresion SEMIC'
	p[0] = ('asignacion', p[1], p[2], p[3], p[4])

def p_estatuto(p):
	'''estatuto : asignacion
				| condicion
				| escritura'''
	p[0] = ('estatuto', p[1])

def p_bloque(p):
	'''bloque : LCURLY bloque2 RCURLY
				| LCURLY RCURLY'''
	if len(p) > 3 :
		p[0] = ('bloque', p[2])
	else : p[0] = ('bloque vacio')

def p_bloque2(p):
	'''bloque2 : estatuto bloque2
				| estatuto'''
	if len(p) > 2 :
		p[0] = (p[2])
	else : p[0]= (p[1])

def p_tipo(p):
	'''tipo : CTEI
			| CTEF'''
	p[0] = ('tipo', p[1])

def p_vars(p):
    'vars : VAR vars3'
    p[0]= ('vars', p[2])

def p_vars2(p):
    '''vars2 : ID DOT vars2
         | ID'''
    p[0]= p[1]

def p_vars3(p):
    '''vars3 : vars2 POINTS tipo SEMIC
         | vars2 POINTS tipo SEMIC vars3'''
    p[0]= p[1]

def p_programa(p):
    '''programa : PROGRAM ID POINTS vars bloque
         | PROGRAM ID POINTS bloque'''
    if len(p) > 5 : p[0]= ('programa', p[2], p[4], p[5])
    else : p[0]= ('programa', p[2], p[4])


# Pruebas
lexer = lex.lex() 

def test(input_string):
  lexer.input(input_string)
  print list(lexer)
  parser = yacc.yacc() 
  try: 
    parse_tree = parser.parse(input_string, lexer=lexer) 
    print 'SUCCESS!'
    return parse_tree 
  except:
    return "ERROR" 

print 'Caso 1'
print test('program caso1 : { print (\'test\') ;}')

print '\nCaso 2'
print test('program condicion : { if (5 > 3) {} ;}')

print '\nCaso 3'
print test('program asignacion : { if (3 > 4) { a = 5;} ;}')

print '\nCaso 4'
print test('program completo : var primer . compilador: int; otra . hi: float; { if (3 > 4) {print (\'caso4\') ;};} ')

print '\nCaso 5: Con error'
print test('program error : var yamequierograduar . compis: int otra . hi: float; { if (3 > 4) {print (\'caso5\' ;};} ')
