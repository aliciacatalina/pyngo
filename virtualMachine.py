#Virtual Machine
#coding:UTF-8

from math import *

quad = [['=', 34001, ' ', 4001], ['=', 30001, ' ', 100], ['=', 30002, ' ', 101], ['<=', 100, 101, 20001], ['=', 20001, ' ', 2002], ['/', 32001, 100, 22001], ['=', 22001, ' ', 2001], ['print', ' ', ' ', 2002], ['print', ' ', ' ', 2001]]
memory = [{4001: 'bo', 100: 'a', 101: 'b', 102: 'c', 103: 'g', 104: 'f', 105: 'e', 2001: 'd', 2002: 'h'},
        {34001: 'false', 30002: 4, 32001: 4.5, 30001: 3},
        {20001: ' 100 - 101', 22001: ' 32001 - 100'}]

countquads = 9;

def virtual_machine (quad):
    print "It's inside the machine"
    mglobal = memory[0]
    mcte = memory[1]
    mtemporal = memory[2]
    i = 0
    while i < countquads: 
        print "While were at it"      
        #Logic of this: We get a quad, in form of an array
        # quad[i][0] is the operator
        # quad[i][1] is the first operand
        # quad[i][2] is the second operand
        # quad[i][0] is the the result of operand 1 operator operand 2
        if quad[i][0] == "+":
            print "Addition"
            #Defining in which part of the memory we need to get the value from
            if(quad[i][1] <= 8001):
                op1 = mglobal[quad[i][1]]
            elif(quad[i][1] >= 12001 and quad[i][1] <= 28001):
                    op1 = mtemporal[quad[i][0]]
            elif(quad[i][1] >= 30001 and quad[i][1] <= 38001):
                    op1 = mcte[quad[i][1]]
                    
            if(quad[i][2] <= 8001):
                    op2 = mglobal[quad[i][2]]
            elif(quad[i][2] >= 12001 and quad[i][2] <= 28001):
                    op2 = mtemporal[quad[i][2]]
            elif(quad[i][2] >= 30001 and quad[i][2] <= 38001):
                    op2 = mcte[quad[i][2]]
            #Assing the result of the operation in a new variable    
            res = op1 + op2
                    
            #Store the variable with the result
            mtemporal[quad[i][3]] = res
            print mtemporal[quad[i][3]]
            i +=1
            
        
        elif quad[i][0] == "-":
            print "Substraction"
            if(quad[i][1] <= 8001):
                op1 = mglobal[quad[i][1]]
            elif(quad[i][1] >= 12001 and quad[i][1] <= 28001):
                op1 = mtemporal[quad[i][1]]
            elif(quad[i][1] >= 30001 and quad[i][1] <= 38001):
                op1 = mcte[quad[i][1]]
                
            if(quad[i][2] <= 8001):
                op2 = mglobal[quad[i][2]]
            elif(quad[i][2] >= 12001 and quad[i][2] <= 28001):
                op2 = mtemporal[quad[i][2]]
            elif(quad[i][2] >= 30001 and quad[i][2] <= 38001):
                op2 = mcte[quad[i][2]]
    
            res = op1 - op2

            mtemporal[quad[i][3]] = res
            print mtemporal[quad[i][3]]
            i +=1
                
        elif quad[i][0] == "*":
            print "Multiplication"
            if(quad[i][1] <= 8001):
                op1 = mglobal[quad[i][1]]
            elif(quad[i][1] >= 12001 and quad[i][1] <= 28001):
                op1 = mtemporal[quad[i][1]]
            elif(quad[i][1] >= 30001 and quad[i][1] <= 38001):
                op1 = mcte[quad[i][1]]
                
            if(quad[i][2] <= 8001):
                op2 = mglobal[quad[i][2]]
            elif(quad[i][2] >= 12001 and quad[i][2] <= 28001):
                op2 = mtemporal[quad[i][2]]
            elif(quad[i][2] >= 30001 and quad[i][2] <= 38001):
                op2 = mcte[quad[i][2]]
    
            res = op1 * op2
                
            mtemporal[quad[i][3]] = res
            print mtemporal[quad[i][3]]
            i +=1
            
        elif quad[i][0] == "/":
            print "Divition"
            if(quad[i][1] <= 8001):
                op1 = mglobal[quad[i][1]]
            elif(quad[i][1] >= 12001 and quad[i][1] <= 28001):
                op1 = mtemporal[quad[i][1]]
            elif(quad[i][1] >= 30001 and quad[i][1] <= 38001):
                op1 = mcte[quad[i][1]]
                
            if(quad[i][2] <= 8001):
                op2 = mglobal[quad[i][2]]
            elif(quad[i][2] >= 12001 and quad[i][2] <= 28001):
                op2 = mtemporal[quad[i][2]]
            elif(quad[i][2] >= 30001 and quad[i][2] <= 38001):
                op2 = mcte[quad[i][2]]
    
            res = op1 / op2
                
            mtemporal[quad[i][3]] = res
            print mtemporal[quad[i][3]]
            i +=1

        elif quad[i][0] == ">":
            print "Greater than"
            if(quad[i][1] <= 8001):
                op1 = mglobal[quad[i][1]]
            elif(quad[i][1] >= 12001 and quad[i][1] <= 28001):
                op1 = mtemporal[quad[i][1]]
            elif(quad[i][1] >= 30001 and quad[i][1] <= 38001):
                op1 = mcte[quad[i][1]]
                
            if(quad[i][2] <= 8001):
                op2 = mglobal[quad[i][2]]
            elif(quad[i][2] >= 12001 and quad[i][2] <= 28001):
                op2 = mtemporal[quad[i][2]]
            elif(quad[i][2] >= 30001 and quad[i][2] <= 38001):
                op2 = mcte[quad[i][2]]
    
            res = op1 > op2
                
            mtemporal[quad[i][3]] = res
            print mtemporal[quad[i][3]]
            i +=1

        elif quad[i][0] == "<":
            print "Less than"
            if(quad[i][1] <= 8001):
                op1 = mglobal[quad[i][1]]
            elif(quad[i][1] >= 12001 and quad[i][1] <= 28001):
                op1 = mtemporal[quad[i][1]]
            elif(quad[i][1] >= 30001 and quad[i][1] <= 38001):
                op1 = mcte[quad[i][1]]
                
            if(quad[i][2] <= 8001):
                op2 = mglobal[quad[i][2]]
            elif(quad[i][2] >= 12001 and quad[i][2] <= 28001):
                op2 = mtemporal[quad[i][2]]
            elif(quad[i][2] >= 30001 and quad[i][2] <= 38001):
                op2 = mcte[quad[i][2]]
    
            res = op1 < op2
                
            mtemporal[quad[i][3]] = res
            print mtemporal[quad[i][3]]
            i +=1
        elif quad[i][0] == ">=":
            print "Greater or equal to"
            if(quad[i][1] <= 8001):
                op1 = mglobal[quad[i][1]]
            elif(quad[i][1] >= 12001 and quad[i][1] <= 28001):
                op1 = mtemporal[quad[i][1]]
            elif(quad[i][1] >= 30001 and quad[i][1] <= 38001):
                op1 = mcte[quad[i][1]]
                
            if(quad[i][2] <= 8001):
                op2 = mglobal[quad[i][2]]
            elif(quad[i][2] >= 12001 and quad[i][2] <= 28001):
                op2 = mtemporal[quad[i][2]]
            elif(quad[i][2] >= 30001 and quad[i][2] <= 38001):
                op2 = mcte[quad[i][2]]
    
            res = op1 >= op2
                
            mtemporal[quad[i][3]] = res
            print mtemporal[quad[i][3]]
            i +=1

        elif quad[i][0] == "<=":
            print "Less or equal than"
            if(quad[i][1] <= 8001):
                op1 = mglobal[quad[i][1]]
            elif(quad[i][1] >= 12001 and quad[i][1] <= 28001):
                op1 = mtemporal[quad[i][1]]
            elif(quad[i][1] >= 30001 and quad[i][1] <= 38001):
                op1 = mcte[quad[i][1]]
                
            if(quad[i][2] <= 8001):
                op2 = mglobal[quad[i][2]]
            elif(quad[i][2] >= 12001 and quad[i][2] <= 28001):
                op2 = mtemporal[quad[i][2]]
            elif(quad[i][2] >= 30001 and quad[i][2] <= 38001):
                op2 = mcte[quad[i][2]]
    
            res = op1 <= op2
                
            mtemporal[quad[i][3]] = res
            print mtemporal[quad[i][3]]
            i +=1

        elif quad[i][0] == '%':
            print ""
            if(quad[i][1] <= 8001):
                op1 = mglobal[quad[i][1]]
            elif(quad[i][1] >= 12001 and quad[i][1] <= 28001):
                op1 = mtemporal[quad[i][1]]
            #Operador 1 del constante ...
            elif(quad[i][1] >= 30001 and quad[i][1] <= 38001):
                op1 = mcte[quad[i][1]]
                
            #Operador 2 del global ...
            if(quad[i][2] <= 8001):
                op2 = mglobal[quad[i][2]]
            elif(quad[i][2] >= 12001 and quad[i][2] <= 28001):
                op2 = mtemporal[quad[i][2]]
            elif(quad[i][2] >= 30001 and quad[i][2] <= 38001):
                op2 = mcte[quad[i][2]]

            res = op1 % op2
                
            mtemporal[quad[i][3]] = res
            print mtemporal[quad[i][3]]
            i +=1

        elif quad[i][0] == '^':
            print "Power"
            if(quad[i][1] <= 8001):
                op1 = mglobal[quad[i][1]]
            elif(quad[i][1] >= 12001 and quad[i][1] <= 28001):
                op1 = mtemporal[quad[i][1]]
            elif(quad[i][1] >= 30001 and quad[i][1] <= 38001):
                op1 = mcte[quad[i][1]]
                
            if(quad[i][2] <= 8001):
                op2 = mglobal[quad[i][2]]
            elif(quad[i][2] >= 12001 and quad[i][2] <= 28001):
                op2 = mtemporal[quad[i][2]]
            elif(quad[i][2] >= 30001 and quad[i][2] <= 38001):
                op2 = mcte[quad[i][2]]
    
            res = pow(op1,op2)
                
            mtemporal[quad[i][3]] = res
            print mtemporal[quad[i][3]]
            i +=1
        
        elif quad[i][0] == '!':
            print "Not"
            if(quad[i][1] <= 8001):
                op1 = mglobal[quad[i][1]]
            elif(quad[i][1] >= 12001 and quad[i][1] <= 28001):
                op1 = mtemporal[quad[i][1]]
            elif(quad[i][1] >= 30001 and quad[i][1] <= 38001):
                op1 = mcte[quad[i][1]]
    
            res = not op1
                
            mtemporal[quad[i][3]] = res
            print mtemporal[quad[i][3]]
            i +=1
                
        elif quad[i][0] == '=':
            print "Asign"
            if(quad[i][1] <= 8001):
                op1 = mglobal[quad[i][1]]
                if(quad[i][3] <= 8001):
                    mglobal[quad[i][3]] = op1
                    print mglobal[quad[i][3]]
                if(quad[i][3] >= 12001 and quad[i][3] <= 28001):
                    mtemporal[quad[i][3]] = op1
                    print mtemporal[quad[i][3]]
                if(quad[i][3] >= 30001 and quad[i][3] <= 38001):
                    mcte[quad[i][3]] = op1
                    print mcte[quad[i][3]]
    

            elif(quad[i][1] >= 12001 and quad[i][1] <= 28001):
                op1 = mtemporal[quad[i][1]]
                if(quad[i][3] <= 8001):
                    mglobal[quad[i][3]] = op1
                    print mglobal[quad[i][3]]
                if(quad[i][3] >= 12001 and quad[i][3] <= 28001):
                    mtemporal[quad[i][3]] = op1
                    print mtemporal[quad[i][3]]
                if(quad[i][3] >= 30001 and quad[i][3] <= 38001):
                    mcte[quad[i][3]] = op1
                    print mcte[quad[i][3]]
                    
            elif(quad[i][1] >= 30001 and quad[i][1] <= 38001):
                op1 = mcte[quad[i][1]]
                if(quad[i][3] <= 8001):
                    mglobal[quad[i][3]] = op1
                    print mglobal[quad[i][3]]
                if(quad[i][3] >= 12001 and quad[i][3] <= 28001):
                    mtemporal[quad[i][3]] = op1
                    print mtemporal[quad[i][3]]
            #Guarda resultado en constante ...
                if(quad[i][3] >= 30001 and quad[i][3] <= 38001):
                    mcte[quad[i][3]] = op1
                    print mcte[quad[i][3]]
            i +=1
    
        elif quad[i][0] == 'print':
            print "Print"
            if(quad[i][3] <= 8001):
                    print mglobal[quad[i][3]]
            if(quad[i][3] >= 12001 and quad[i][3] <= 28001):
                    print mtemporal[g]
            if(quad[i][3] >= 30001 and quad[i][3] <= 38001):
                    print mcte[quad[i][3]]
            i +=1

    def contenidogoto (casilla):
        #Obtener Valor de los globales
        if(num <= 8001):
            goto = mglobal[num]
            return goto
        #Obtener Valor de los locales
        if(num >= 10001 and num <= 18001):
            goto = mlocal[num]
            return goto
        #Obtener Valor de los temporales ...
        if(num >= 12001 and num <= 28001):
            goto = mtemporal[num]
            return goto
        #Obtener Valor de los constantes ...
        if(num >= 30001 and num <= 38001):
            goto = mcte[num]
            return goto
                
    i = 0

    while (i < len(completo[0])):
        cuadru = completo[0][i]

       operador = cuadru[0]
        num = cuadru[1]
                
            if(operador == 31):
                goto = contenidogoto(num)
                print "GOTO"
                print goto
                if(goto == False):
                    g = cuadru[3]
                    i += g
                    #print i
                    cuadru = completo[0][i+1]
                    #print cuadru
                    #Obtener accesos a mandar 1
                    op1 = cuadru[1] # Obtengo 104
                    #print op1
                    #Obtener accesos a mandar 2
                    op2 = cuadru[2] # Obtengo 103
                    #print op2
                    #Obtener accesos a mandar 3
                    guardo = cuadru[3] #Obtengo 20001
                    #print guardo
                    i+=1

                else:
                    op1 = cuadru[1] # Obtengo 104
                    #print op1
                    #Obtener accesos a mandar 2
                    op2 = cuadru[2] # Obtengo 103
                    #print op2
                    #Obtener accesos a mandar 3
                    guardo = cuadru[3] #Obtengo 20001
                    #print guardo
                    i+=1

        elif(operador == 32):
            g = cuadru[3]
            i += g
            #print i
            cuadru = completo[0][i+1]
            #print cuadru
            #Obtener accesos a mandar 1
            op1 = cuadru[1] # Obtengo 104
            #print op1
            #Obtener accesos a mandar 2
            op2 = cuadru[2] # Obtengo 103
            #print op2
            #Obtener accesos a mandar 3
            guardo = cuadru[3] #Obtengo 20001
            #print guardo
            i+=1

        else:
            #Obtener accesos a mandar 1
            op1 = cuadru[1] # Obtengo 104
            #print op1
            #Obtener accesos a mandar 2
            op2 = cuadru[2] # Obtengo 103
            #print op2
            #Obtener accesos a mandar 3
            guardo = cuadru[3] #Obtengo 20001
            #print guardo
            #Switch gigante para cada operador
            opcion[operador](op1, op2, guardo)
            i+=1
                
    print i

virtual_machine(quad)     
