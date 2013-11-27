#Virtual Machine
#coding:UTF-8

from math import *
from copy import deepcopy
import opMatrices

#memory = dictvar
#quad = cuadruplos

memory = {'factorial': {'int': {0: 15003, 1: 15004, 'return': 30003, 'n': 15002}, 'functype': {'begin': 1, 'return': 'int', 'param1': 15002}}, 'global': {'int': {'a': 0, 3: 1}}, 'Temp': {'int': {'t6': 30006, 't7': 30007, 't4': 30004, 't5': 30005, 't2': 30002, 't3': 30003, 't1': 30001}, 'bool': {'t0': 40001}}}
quad = [['goto', '', '', 12], ['==', 15002, 15003, 40001], ['gotof', 40001, ' ', 2], ['return', 15004, '', ''], ['goto', ' ', ' ', 7], ['ERA', 'factorial', '', ''], ['-', 15002, 15004, 30001], ['Param', 30001, '', 'param1'], ['Gosub', 'factorial', '', ''], ['=', 30003, '', 30002], ['*', 15002, 30002, 30003], ['return', 30003, '', ''], ['ret', '', '', ''], ['*', 1, 1, 30004], ['+', 1, 30004, 30005], ['+', 1, 30005, 30006], ['=', 30006, '', 0], ['ERA', 'factorial', '', ''], ['Param', 0, '', 'param1'], ['Gosub', 'factorial', '', ''], ['=', 30003, '', 30007], ['print', 30007, '', '']]
#test arrays
memory = {'global': {'int': {'a': 0, 1: 8, 2: 9, 'b': 4, 4: 11, 5: 12, 3: 10, 'i': 13, 'a1': 1, 'a3': 3, 'a2': 2, 'b1': 5, 'b2': 6, 'b3': 7, 0: 14}, 'arrays': {'a': {'begin': 0, 'type': 'int', 'dimensions': [2, 2], 'size': 4}, 'b': {'begin': 4, 'type': 'int', 'dimensions': [2, 2], 'size': 4}}}, 'Temp': {'int': {'t4': 30005, 't2': 30003, 't3': 30004, 't0': 30001, 't1': 30002}}}
quad = [['=', 8, '', 0], ['=', 9, '', 1], ['=', 10, '', 2], ['=', 11, '', 3], ['=', 9, '', 4], ['=', 10, '', 5], ['=', 11, '', 6], ['=', 12, '', 7], ['*', 0, 4, 30001], ['print', 30001, '', ''], ['=', 14, '', 13], ['length', 0, '', 30002], ['<', 13, 30002, 30003], ['gotof', 30003, ' ', 5], ['*', 12, 12, 30004], ['+', 30004, 9, 30005], ['print', 30005, '', ''], ['+', 8, 13, 13], ['goto', ' ', ' ', -8]]
#quad = [['=', 8, '', 0], ['=', 9, '', 1], ['=', 10, '', 2], ['=', 11, '', 3], ['=', 9, '', 4], ['=', 10, '', 5], ['=', 11, '', 6], ['=', 12, '', 7], ['*', 0, 4, 30005], ['print', 30005, '', '']]
stackFunc = []
memoryFunc = {}
paramsFunc = {}
memoryERA = {}

#swap directions and values
for i in memory:
    if i == 'global' or i == 'Temp' or i == 'local':
        for j in memory[i]:
            if j != 'arrays':
                memory[i][j] = dict (zip(memory[i][j].values(),memory[i][j].keys()))
    else:
        for j in memory[i]:
            if j != 'functype':
                memory[i][j] = dict (zip(memory[i][j].values(),memory[i][j].keys()))

def virtual_machine (quad):
    print "It's inside the machine"

    #obtiene el valor a partir de una direccion de memoria
    def getVal(mem):
        #get functionId
        for key in memoryFunc:
            functionId = key

        if mem <= 5000: return globalInt[mem]
        if mem > 5000 and mem <= 10000: return globalFloat[mem]
        if mem > 10000 and mem <= 15000: return globalBool[mem]

        if mem > 15000 and mem <= 20000: return memoryFunc[functionId]['int'][mem]
        if mem > 20000 and mem <= 25000: return memoryFunc[functionId]['float'][mem]
        if mem > 25000 and mem <= 30000: return memoryFunc[functionId]['bool'][mem]

        if mem > 30000 and mem <= 35000: return tempInt[mem]
        if mem > 35000 and mem <= 40000: return tempFloat[mem]
        if mem > 40000 and mem <= 45000: return tempBool[mem]

    #guarda el valor en la direccion de memoria dada
    def setVal(mem, val):
        #get functionId
        for key in memoryFunc:
            functionId = key

        if mem <= 5000:                 globalInt[mem] = val
        if mem > 5000 and mem <= 10000: globalFloat[mem] = val
        if mem > 10000 and mem <= 15000: globalBool[mem] = val

        if mem > 15000 and mem <= 20000: memoryFunc[functionId]['int'][mem] = val
        if mem > 20000 and mem <= 25000: memoryFunc[functionId]['float'][mem] = val
        if mem > 25000 and mem <= 30000: memoryFunc[functionId]['bool'][mem] = val

        if mem > 30000 and mem <= 35000: tempInt[mem] = val
        if mem > 35000 and mem <= 40000: tempFloat[mem] = val
        if mem > 40000 and mem <= 45000: tempBool[mem] = val

    def isArray(mem):
        for key in memory:
            if memory[key].has_key('arrays'):
                for j in memory[key]['arrays']:
                    begin = memory[key]['arrays'][j]['begin']
                    if mem == begin:
                        return True
        return False

    def getDimensions(mem):
        for key in memory:
            if memory[key].has_key('arrays'):
                for j in memory[key]['arrays']:
                    dimensions = memory[key]['arrays'][j]['dimensions']
                    return dimensions
        return []

    def buildArray(mem, dimensions):
        #dimensions = [2, 2]
        #dimensions = [4]
        #mem = 0
        arrTemp1 = []
        arrTemp2 = []
        #array
        if len(dimensions) == 1:
            del arrTemp1[:]
            for k in range(dimensions[0]):
                arrTemp1.append(getVal(mem))
                mem +=1
            return arrTemp1
        #matrix
        if len(dimensions) == 2:
            del arrTemp1[:]
            del arrTemp2[:]
            for k in range(dimensions[0]):
                del arrTemp1[:]
                for j in range(dimensions[1]):
                    arrTemp1.append(getVal(mem))
                    mem +=1
                arrTemp2.append(deepcopy(arrTemp1))

            return arrTemp2


    for k in memory:
        if k == 'global':
            for j in memory[k]:
                if j == 'int':      globalInt = memory['global']['int']
                if j == 'float':    globalFloat = memory['global']['float']
                if j == 'bool':     globalBool = memory['global']['bool']
        if k == 'Temp':
            for j in memory[k]:
                if j == 'int':      tempInt = memory['Temp']['int']
                if j == 'float':    tempFloat = memory['Temp']['float']
                if j == 'bool':     tempBool = memory['Temp']['bool']
        if k == 'local':
            for j in memory[k]:
                if j == 'int':      localInt = memory['local']['int']
                if j == 'float':    localFloat = memory['local']['float']
                if j == 'bool':     localBool = memory['local']['bool']

    i = 0

    while i < len(quad): 
        print "While were at it"      
        #Logic of this: We get a quad, in form of an array
        # quad[i][0] is the operator
        # quad[i][1] is the first operand
        # quad[i][2] is the second operand
        # quad[i][3] is the the result of operand 1 operator operand 2
        if quad[i][0] == "+":
            print "Addition"
            arr1 = []
            arr2 = []
            if isArray(quad[i][1]) and isArray(quad[i][2]):
                arr1 = deepcopy(buildArray(quad[i][1], getDimensions(quad[i][1])))
                arr2 = deepcopy(buildArray(quad[i][2], getDimensions(quad[i][2])))
                print arr1
                print arr2
                res = opMatrices.suma(arr1, arr2)
                setVal(quad[i][3], res)

            else:
                op1 = getVal(quad[i][1])
                op2 = getVal(quad[i][2])
                res = op1+op2
                setVal(quad[i][3], res)
                print isArray(op1)
                print op1, '+', op2, '=', res
            i +=1

        elif quad[i][0] == '-':
            print "Substraction"
            arr1 = []
            arr2 = []
            if isArray(quad[i][1]) and isArray(quad[i][2]):
                arr1 = deepcopy(buildArray(quad[i][1], getDimensions(quad[i][1])))
                arr2 = deepcopy(buildArray(quad[i][2], getDimensions(quad[i][2])))
                print arr1
                print arr2
                res = opMatrices.resta(arr1, arr2)
                setVal(quad[i][3], res)

            else:
                op1 = getVal(quad[i][1])
                op2 = getVal(quad[i][2])
                res = op1-op2
                setVal(quad[i][3], res)
            i +=1

        elif quad[i][0] == '*':
            print "Multiplication"
            arr1 = []
            arr2 = []
            if isArray(quad[i][1]) and isArray(quad[i][2]):
                arr1 = deepcopy(buildArray(quad[i][1], getDimensions(quad[i][1])))
                arr2 = deepcopy(buildArray(quad[i][2], getDimensions(quad[i][2])))
                print arr1
                print arr2
                res = opMatrices.multiplica(arr1, arr2)
                setVal(quad[i][3], res)

            else:
                op1 = getVal(quad[i][1])
                op2 = getVal(quad[i][2])
                res = op1*op2
                print op1
                setVal(quad[i][3], res)
            i +=1

        elif quad[i][0] == "/":
            print "Divition"
            op1 = getVal(quad[i][1])
            op2 = getVal(quad[i][2])
            res = op1/op2
            setVal(quad[i][3], res)
            i +=1

        elif quad[i][0] == ">":
            print "Greater than"
            op1 = getVal(quad[i][1])
            op2 = getVal(quad[i][2])
            res = op1>op2
            setVal(quad[i][3], res)
            i +=1

        elif quad[i][0] == "<":
            print "Less than"
            op1 = getVal(quad[i][1])
            op2 = getVal(quad[i][2])
            res = op1<op2
            print op1 ,'<', op2, '=', res
            setVal(quad[i][3], res)
            i +=1

        elif quad[i][0] == "==":
            print "Equal"
            op1 = getVal(quad[i][1])
            op2 = getVal(quad[i][2])
            res = op1==op2
            setVal(quad[i][3], res)
            i +=1

        elif quad[i][0] == ">=":
            print "Greater or equal to"
            op1 = getVal(quad[i][1])
            op2 = getVal(quad[i][2])
            res = op1>=op2
            setVal(quad[i][3], res)
            i +=1

        elif quad[i][0] == "<=":
            print "Less or equal than"
            op1 = getVal(quad[i][1])
            op2 = getVal(quad[i][2])
            res = op1<=op2
            setVal(quad[i][3], res)
            i +=1

        elif quad[i][0] == '^':
            print "Power"
            op1 = getVal(quad[i][1])
            op2 = getVal(quad[i][2])
            res = pow(op1, op2)
            setVal(quad[i][3], res)
            i +=1

        elif quad[i][0] == '!':
            print "Not"
            op1 = getVal(quad[i][1])
            res = not op1
            setVal(quad[i][3], res)
            i +=1


        elif quad[i][0] == '%':
            print "residue"
            op1 = getVal(quad[i][1])
            op2 = getVal(quad[i][2])
            res = op1%op2
            setVal(quad[i][3], res)
            i +=1

        elif quad[i][0] == '=':
            print "Asign"
            op1 = getVal(quad[i][1])
            print op1
            setVal(quad[i][3], op1)
            i +=1

        elif quad[i][0] == 'goto':
            print "Goto"
            i += quad[i][3]
            if quad[i][3] == 0:
                i +=1
            else: i +=1

        elif quad[i][0] == 'gotof':
            print "GotoF"
            op1 = getVal(quad[i][1])
            print op1
            if op1 == False:
                i += quad[i][3]
                i +=1
            else:
                i +=1

        elif quad[i][0] == 'gotov':
            print 'GotoV'
            op1 = getVal(quad[i][1])
            if op1 == True:
                i += quad[i][3]
            else:
                i +=1

        elif quad[i][0] == 'print':
            print "Print"
            print '************************'
            if isArray(quad[i][1]):
                arr = []
                arr = deepcopy(buildArray(quad[i][1], getDimensions(quad[i][1])))
                print arr
            else:
                print getVal(quad[i][1])
            i +=1

        elif quad[i][0] == 'ERA':
            print "ERA"
            for j in memory:
                if j == quad[i][1]:
                    #fact{n,0,1}
                    memoryERA.update({quad[i][1]: memory[j]})
            i +=1

        elif quad[i][0] == 'Param':
            print "Param"
            val = getVal(quad[i][1])
            paramsFunc.update({quad[i][3]:val})
            i +=1

        elif quad[i][0] == 'Gosub':
            print "GOSUB"
            functionId = quad[i][1]
            #add current i and temp variables of the main memory
            if len(memoryFunc) == 0:
                memoryFunc.update({functionId: {'i': i, 'Temp': memory['Temp']}})
                print i
            else:
                memoryFunc[functionId].update({'i':i, 'Temp': memory['Temp']})

            #save state of currentFunc
            temporal = {}
            temporal = deepcopy(memoryFunc)
            stackFunc.append(temporal)

            #actualize memoryFunc
            memoryFunc.clear()
            memoryFunc.update(memoryERA)

            #actualize parameters
            for key in paramsFunc:
                param=0
                for j in memoryERA[functionId]['functype']:
                    if j == key:
                        #get the memory direction of parameter
                        mem = memoryERA[functionId]['functype'][j]
            
                setVal(mem, paramsFunc[key])

            paramsFunc.clear()
            
            #actualize i
            i = memoryFunc[functionId]['functype']['begin']
            
        elif quad[i][0] == 'return':
            print "return"
            res = getVal(quad[i][1])
            print res
            memoryFunc.clear()
            memoryFunc.update(stackFunc.pop())
            #get functionId
            for key in memoryFunc:
                functionId = key

            #change previous values
            memory.update({'Temp': memoryFunc[functionId]['Temp']})

            #get returnType
            if memoryFunc[functionId].has_key('functype'):
                returnType = ''
                for key in memoryFunc[functionId]['functype']:
                    if key == 'return':
                        returnType = memoryFunc[functionId]['functype'][key]
                
                #actualize return value
                for key in memory[functionId][returnType]:
                    if memory[functionId][returnType][key] == 'return':
                        mem = key

                setVal(mem, res)

            i = memoryFunc[functionId]['i']
            i +=1
            print getVal(mem)

        elif quad[i][0] == 'ret':
            print "RET"
            memoryFunc.clear()
            memoryFunc.update(stackFunc.pop())
            #get functionId
            for key in memoryFunc:
                functionId = key

            #change previous values
            memory.update({'Temp': memoryFunc[functionId]['Temp']})

            i = memoryFunc[functionId]['i']
            i +=1

        elif quad[i][0] == 'length':
            print "length"
            #memory where array starts
            op1 = quad[i][1]
            #size of array
            for key in memory:
                if memory[key].has_key('arrays'):
                    for j in memory[key]['arrays']:
                        if memory[key]['arrays'][j]['begin'] == op1:
                            size = memory[key]['arrays'][j]['size']
            
            print size
            setVal(quad[i][3], size)    
            i +=1

        elif quad[i][0] == 'col':
            print "col"
            #matrix
            
            #numero de columna
            op2 = quad[i][2]
            i +=1

        elif quad[i][0] == 'end':
            print "end"
            i +=1

virtual_machine(quad)