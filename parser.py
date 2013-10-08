#--------
# parser.py
# PYNGO - Parser
# Alicia Gonzalez 1088149
# Ernesto Garcia 
# Creado : 05 de Octubre
#--------

import sys
import scanner
import ply.yacc as yacc

tokens = scanner.tokens
start = 'programa'

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

def p_declaravars(p):
	'''declaravars : vars
			| empty'''


def p_programa(p):
    '''programa : declaravars declarafuncion MODEL POINTS declaravarsdata bloque
         | empty'''
    if len(p) > 5 : p[0]= ('programa', p[2], p[4], p[5])
    else : p[0]= ('programa', p[2], p[4])
