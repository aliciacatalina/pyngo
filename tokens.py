# tokens.py | Lexico de PYNGO 
# Alicia Gonzalez 1088149 | Ernesto Garcia
import ply.lex as lex

# tokens
tokens = (
		'ID', 

		#control de flujo
		'IF', 
		'ELSE',
		'FOR',
		'IN',

		#operadores artimeticos
		'STAR', 
		'SLASH',
		'PLUS', 
		'MINUS', 
		'LESSTHAN', 
		'GREATERTHAN', 
		'BETWEEN',

		#separadores
		'LPAREN', 
		'RPAREN', 
		'LCURLY', 
		'RCURLY',
		'SEMIC',
		'LBRACKET', 
		'RBRACKET',
		'DOT',
		'COMMA',

		# asignaciones
		'POINTS',   
		'EQUALS',  
	 
		#variables	 
		'TBOOL', 
		'TINT', 
		'TFLOAT',

 		#accion
		'PRINT', 

		#constantes 
		'CTEI', 
		'CTEF',
		'CTEBOOL',
		'CTESTRING',

		#palabras reservadas
		'MAX', 
		'MIN', 
		'FUNC',
		'VARS', 
		'DATA', 
		'MODEL',
		'SUM', 
		'WHERE', 
		'RETURN' 
)

#tokens

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
t_COMMA			= r'\,'
t_DOT			= r'\.'
t_LBRACKET		= r'\['
t_RBRACKET		= r'\]'

reserved = {
	'if':	'IF', 
	'else':	'ELSE', 
	'for':	'FOR', 
	'func': 'FUNC', 
	'return': 'RETURN',
	'model': 'MODEL',
	'print': 'PRINT',
	'false': 'FALSE',
	'true': 'TRUE',
	'int' : 'TINT',
	'string': 'TSTRING',
	'float': 'TFLOAT',
	'bool': 'TBOOL',
	'where': 'WHERE',
	'sum': 'SUM',
	'return' : 'RETURN',
	'vars' : 'VARS',
	'data' : 'DATA', 
	'in'	: 'IN'
}

def t_ID(t):
	r"[a-zA-Z]([a-zA-Z0-9])*(\.[a-zA-Z]([a-zA-Z0-9])*)*"
	if t.value.lower() in reserved:
		t.type = reserved[t.value.lower()]
	return t

def t_CTESTRING(t):
	r"'([A-Z]|[a-z]|[0-9])*'"
	return t

def t_CTEF(t):
	r"[0-9]+(\.[0-9]*)"
	t.value = float(t.value)
	return t

def t_CTEI(t):
	r"[0-9]+"
	t.value = int(t.value)
	return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

t_ignore  = ' \r\t'

def t_error(t):
	print ("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

if __name__ == '__main__':
	# Build the lexer
	from ply import lex
	import sys 

	lex.lex()

	if len(sys.argv) > 1:
		f = open(sys.argv[1],"r")
		data = f.read()
		f.close()
	else:
		data = ""
		while 1:
			try:
				data += raw_input() + "\n"
			except:
				break

	lex.input(data)

	# Tokenize
	while 1:
	    tok = lex.token()
	    if not tok: break      # No more input
	    print tok
