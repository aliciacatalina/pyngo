# -*- coding: utf-8 -*- 
import sys
import ply.lex as lex
import ply.yacc as yacc
from semantics import *
from syntaxalternativa import *
from tokens import *
lexer = lex.lex() 
program_file = str(sys.argv[1])
f = open(program_file, 'r').read()
print f
def test(input_string):
    lexer.input(input_string)
    print list(lexer)
    parser = yacc.yacc() 
    parse_tree = parser.parse(input_string, lexer=lexer) 
    print parse_tree
    print 'Success!'
    if isinstance(parse_tree, Node):
        print (parse_tree.semantic_all())
    else:
        print 'Failed program'

print test (f)
