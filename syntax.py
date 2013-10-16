start = 'programa'
def p_varcte(p):
	'''varcte : CTEI
		| CTEF
		| CTESTRING
		| CTEBOOL
		| ID
		| llamadafuncion'''
	p[0] = ('varcte', p[1])

def p_llamadafuncion(p):
	'''llamadafuncion : ID LPAREN expresion RPAREN
						| ID LPAREN CTEI RPAREN
						| ID LPAREN CTEF RPAREN'''
	p[0] = ('llamadafuncion', p[3])

def p_data(p):
	'''data : DATA LCURLY listaasignacion RCURLY'''
	p[0] = ('data', p[3])

def p_listaasignacion(p):
	'''listaasignacion : asignacion SEMIC lasignacion'''
	p[0] = ('listaasignacion', p[1], p[3])

def p_lasignacion(p):
	'''lasignacion : empty
				| listaasignacion'''
	p[0] = ('lasignacion', p[1])

def p_funcionoptimizacion(p):
	'''funcionoptimizacion : MIN EQUALS restricciones
							| MAX EQUALS restricciones'''
	p[0] = ('funcionoptimizacion', p[3])

def p_restricciones(p):
	'''restricciones : WHERE restricciones2'''
	p[0]  = ('restricciones', p[2])

def p_restricciones2(p):
	'''restricciones2 : expresion
					| suma SEMIC listafor'''
	if len(p) > 2 : p[0] = ('restricciones2', p[1], p[3])
	else : p[0] = ('restricciones2', p[1])

def p_for(p):
	'''for : FOR ID IN DOT ID LBRACKET estatuto RBRACKET'''
	p[0] = ('for', p[7])

def p_listafor(p):
	'''listafor : for SEMIC lfor'''
	p[0] = ('listafor', p[1], p[3])

def p_lfor(p):
	'''lfor : empty
			| listafor'''
	p[0] = ('lfor', p[1])

def p_suma(p):
	'''suma : SUM LPAREN ID POINTS expresion RPAREN'''
	p[0] = ('suma', p[5])

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
				| CTESTRING
				| expresion DOT escritura2
				| CTESTRING DOT escritura2'''
	if len(p) > 2 : p[0] = ('escritura2', p[1], p[3])
	else : p[0] = ('escritura2', p[1])


def p_asignacion(p):
	'asignacion : ID EQUALS expresion SEMIC'
	p[0] = ('asignacion', p[1], p[2], p[3], p[4])

def p_estatuto(p):
	'''estatuto : asignacion
				| condicion
				| escritura
				| funcionoptimizacion
				| ciclo
				| retorno'''
	p[0] = ('estatuto', p[1])

def p_ciclo(p):
	'''ciclo : for'''
	p[0] = ('ciclo', p[1])

def p_retorno(p):
	'''retorno : RETURN asignacion'''
	p[0] = ('retorno', p[2])

def p_funcion(p):
	'''funcion : FUNC ID LPAREN listaargs RPAREN LCURLY declaravarsdata RCURLY'''
	print "funcion"
	p[0] = ('funcion', p[4], p[7], p[8])

def p_listaargs(p):
	'''listaargs : empty
				| tipo ID liargs'''
	if len(p) > 2 : p[0] = ('listaargs', p[1], p[3])
	else : p[0] = ('listaargs', p[1])

def p_liargs(p):
	'''liargs : empty
			| COMMA listaargs'''
	if len(p) > 2 : p[0] = ('liargs', p[2])
	else : p[0] = ('liargs', p[1])

def p_bloque(p):
	'''bloque : bloque2
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
	'''tipo : TINT
			| TFLOAT
			| TBOOL'''
	p[0] = ('tipo', p[1])

def p_vars(p):
    'vars : VARS LCURLY listavars RCURLY'
    p[0]= ('vars', p[3])


def p_matriz(p):
	'''matriz : LBRACKET CTEI RBRACKET LBRACKET CTEI RBRACKET'''
	p[0] = ('matriz', p[2], p[5])

def p_arreglo(p):
	'''arreglo : LBRACKET CTEI RBRACKET'''
	p[0] = p[2]

def p_declaracion(p):
	'''declaracion : arreglo
					| matriz
					| tipo'''
	p[0] = ('declaracion', p[1])

def p_lid(p):
	'''lid : COMMA listaids
			| empty'''
	if len(p) > 2 : p[0] = ('lid', p[2])
	else : p[0] = ('lid', p[1])

def p_listaids(p):
	'''listaids : ID lid'''
	p[0] = ('listaids', p[2])

def p_lvars(p):
	'''lvars : listavars
			| empty'''
	p[0] = ('lvars', p[1])

def p_listavars(p):
    '''listavars : declaracion POINTS listaids SEMIC'''
    p[0]= ('listavars', p[1], p[3])

def p_declaravarsdata(p):
	'''declaravarsdata : vars data
			| empty
			| vars'''
	if len(p) > 2 : p[0] = ('declaravarsdata', p[1], p[2])
	else : p[0] = ('declaravarsdata', p[1])

def  p_declarafuncion(p):
	'''declarafuncion : funcion
			| empty'''
	p[0] = ('declarafuncion', p[1])

def p_declaravars(p):
	'''declaravars : vars
			| empty'''
	p[0] = ('declaravars', p[1])

def p_programa(p):
    '''programa : declaravars declarafuncion MODEL LCURLY declaravarsdata bloque2 RCURLY'''
    p[0]= ('programa', p[1], p[2], p[5], p[6])

def p_empty(p):
    'empty :'
    pass

def p_error(t):
	if t is None :
		print "Syntax error" 
	else : 
		print "Syntax error:"	
		print t


