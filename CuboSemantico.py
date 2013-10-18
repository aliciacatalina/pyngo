# Cubo semantico

col = int(4) # Cantidad de columnas en la lista
colc = int(27) # Cantidad columnas combinaciones
filc = int(25) # Cantidad filas combinaciones
com = colc * filc #Combinaciones en total
#Contadores para cada uno
icont = int(0)
icont1 = int(0)
icont2 = int(0)
icont3 = int(0)
icont4 = int(0)
icont5 = int(0)
icont6 = int(0)
icont7 = int(0)
icont8 = int(0)
icont9 = int(0)
icont10 = int(0)
icont11 = int(0)
icont12 = int(0)
icont13 = int(0)
icont14 = int(0)
icont15 = int(0)
icont16 = int(0)
icont17 = int(0)
icont18 = int(0)
icont19 = int(0)
icont20 = int(0)
icont21 = int(0)
icont22 = int(0)
icont23 = int(0)
icont24 = int(0)


# Creacion de las combinaciones.
# Tipos:
# 1. Int
# 2. Float
# 3. Bool
# 4. Bit
# 5. String

# Operadores:
# 1. Suma
# 2. Resta
# 3. Multiplicacion
# 4. Division
# 5. Residuo
# 6. Exponencial
# 7. Not
# 8. Or
# 9. And
# 10. Eq
# 11. Dif
# 12. Mayor
# 13. Menor
# 14. MayorQue
# 15. MenorQue
# 16. AsEq
# 17. SumaEq
# 18. MenEq
# 19. MultEq
# 20. DivEq
# 21. MasMas
# 22. MenosMenos
# 23. Xor
# 24. OrB
# 25. AndB
# 26. Shr
# 27. Shl

# Matriz de combinaciones
M = []


#Combinaciones (entero con entero)
for i in range(com):
       M.append([0] * col)
       
       #Combinaciones (entero con entero)
       if i < 27:
           M[i][0] = 1
           M[i][1] = 1
           M[i][2] = i+1
           if M[i][2] <= 6: #operadores de suma,resta,etc
            M[i][3] = 1
           elif (M[i][2] >= 10 and M[i][2] <= 15): #==!><>=<=
            M[i][3] = 3
           elif (M[i][2] >= 16 and M[i][2] <= 27): #Cambio de los bits a entero
            M[i][3] = 1
           else:
            M[i][3] = -1
       #Combinaciones (entero con flotante)
       if (i >= 27 and i < 54):
           icont = icont + 1
           M[i][0] = 1
           M[i][1] = 2
           M[i][2] = icont
           #icont = 1
           if M[i][2] <= 6: #operadores de suma,resta,etc
            M[i][3] = 2
           elif (M[i][2] >= 10 and M[i][2] <= 15): #==!><>=<=
            M[i][3] = 3
           elif (M[i][2] >= 17 and M[i][2] <= 22): #+=,-=,*=,/=
            M[i][3] = 2
           else:
            M[i][3] = -1
       
       #Combinaciones (entero con boolean)
       elif (i >= 54 and i < 81):          
           icont1 = icont1 + 1
           M[i][0] = 1
           M[i][1] = 3
           M[i][2] = icont1
           M[i][3] = -1
           
       #Combinaciones (entero con bit)
       elif (i >= 81 and i < 108):
           icont2 = icont2 + 1
           M[i][0] = 1
           M[i][1] = 4
           M[i][2] = icont2
           M[i][3] = -1

       #Combinaciones (entero con string)
       elif (i >= 108 and i < 135):
           icont3 = icont3 + 1
           M[i][0] = 1
           M[i][1] = 5
           M[i][2] = icont3
           M[i][3] = -1

       #Combinaciones (flotante con entero)
       elif (i >= 135 and i < 162):
           icont4 = icont4 + 1
           M[i][0] = 2
           M[i][1] = 1
           M[i][2] = icont4
           if M[i][2] <= 6: #operadores de suma,resta,etc
            M[i][3] = 2
           elif (M[i][2] >= 11 and M[i][2] <= 15): #==!><>=<=
            M[i][3] = 3
           elif (M[i][2] >= 16 and M[i][2] <= 22):
            M[i][3] = 2
           else:
            M[i][3] = -1

       #Combinaciones (flotante con flotante)
       elif (i >= 162 and i < 189):
           icont5 = icont5 + 1
           M[i][0] = 2
           M[i][1] = 2
           M[i][2] = icont5
           if M[i][2] <= 6: #operadores de suma,resta,etc
            M[i][3] = 2
           elif (M[i][2] >= 10 and M[i][2] <= 15): #==!><>=<=
            M[i][3] = 3
           elif (M[i][2] >= 16 and M[i][2] <= 22):
            M[i][3] = 2
           else:
            M[i][3] = -1

       #Combinaciones (flotante con boolean)
       elif (i >= 189 and i < 216):          
           icont6 = icont6 + 1
           M[i][0] = 2
           M[i][1] = 3
           M[i][2] = icont6
           M[i][3] = -1
           
       #Combinaciones (flotante con bit)
       elif (i >= 216 and i < 243):
           icont7 = icont7 + 1
           M[i][0] = 2
           M[i][1] = 4
           M[i][2] = icont7
           M[i][3] = -1

       #Combinaciones (flotante con string)
       elif (i >= 243 and i < 270):
           icont8 = icont8 + 1
           M[i][0] = 2
           M[i][1] = 5
           M[i][2] = icont8
           M[i][3] = -1

       #Combinaciones (bool con entero)
       elif (i >= 270 and i < 297):
           icont9 = icont9 + 1
           M[i][0] = 3
           M[i][1] = 1
           M[i][2] = icont9
           M[i][3] = -1
           
       #Combinaciones (bool con flotante)
       elif (i >= 297 and i < 324):
           icont10 = icont10 + 1
           M[i][0] = 3
           M[i][1] = 2
           M[i][2] = icont10
           M[i][3] = -1

       #Combinaciones (bool con bool)
       elif (i >= 324 and i < 351):
           icont11 = icont11 + 1
           M[i][0] = 3
           M[i][1] = 3
           M[i][2] = icont11
           if (M[i][2] >= 7 and M[i][2] <= 11):
            M[i][3] = 3
           elif (M[i][2] == 16):
            M[i][3] = 3
           else:
            M[i][3] = -1

       #Combinaciones (bool con bit)
       elif (i >= 351 and i < 378):
           icont12 = icont12 + 1
           M[i][0] = 3
           M[i][1] = 4
           M[i][2] = icont12
           M[i][3] = -1

       #Combinaciones (bool con string)
       elif (i >= 378 and i < 405):
           icont13 = icont13 + 1
           M[i][0] = 3
           M[i][1] = 5
           M[i][2] = icont13
           M[i][3] = -1

       #Combinaciones (bit con entero)
       elif (i >= 405 and i < 432):
           icont14 = icont14 + 1
           M[i][0] = 4
           M[i][1] = 1
           M[i][2] = icont14
           M[i][3] = -1

       #Combinaciones (bit con flotante)
       elif (i >= 432 and i < 459):
           icont15 = icont15 + 1
           M[i][0] = 4
           M[i][1] = 2
           M[i][2] = icont15
           M[i][3] = -1

       #Combinaciones (bit con bool)
       elif (i >= 459 and i < 486):
           icont16 = icont16 + 1
           M[i][0] = 4
           M[i][1] = 3
           M[i][2] = icont16
           M[i][3] = -1

       #Combinaciones (bit con bit)
       elif (i >= 486 and i < 513):
           icont17 = icont17 + 1
           M[i][0] = 4
           M[i][1] = 4
           M[i][2] = icont17
           if(M[i][2] == 16):
            M[i][3] = 4
           elif (M[i][2] >= 23 and M[i][2] <= 27):
            M[i][3] = 4
           else:
            M[i][3] = -1

        #Combinaciones (bit con string)
       elif (i >= 513 and i < 540):
           icont18 = icont18 + 1
           M[i][0] = 4
           M[i][1] = 5
           M[i][2] = icont18
           M[i][3] = -1

        #Combinaciones (string con entero)
       elif (i >= 540 and i < 567):
           icont19 = icont19 + 1
           M[i][0] = 5
           M[i][1] = 1
           M[i][2] = icont19
           if (M[i][2] == 16):
            M[i][3] = 1
           else:
            M[i][3] = -1

        #Combinaciones (string con float)
       elif (i >= 567 and i < 594):
           icont20 = icont20 + 1
           M[i][0] = 5
           M[i][1] = 2
           M[i][2] = icont20
           if (M[i][2] == 16):
            M[i][3] = 2
           else:
            M[i][3] = -1

        #Combinaciones (string con bool)
       elif (i >= 594 and i < 621):
           icont21 = icont21 + 1
           M[i][0] = 5
           M[i][1] = 3
           M[i][2] = icont21
           if (M[i][2] == 16):
            M[i][3] = 3
           else:
            M[i][3] = -1
            
        #Combinaciones (string con bit)
       elif (i >= 621 and i < 648):
           icont22 = icont22 + 1
           M[i][0] = 5
           M[i][1] = 4
           M[i][2] = icont22
           M[i][3] = -1

        #Combinaciones (string con string)
       elif (i >= 648 and i < 675):
           icont23 = icont23 + 1
           M[i][0] = 5
           M[i][1] = 5
           M[i][2] = icont23
           if (M[i][2] == 1 or M[i][2] == 16):
            M[i][3] = 5
           else:
            M[i][3] = -1
#print(M)

# Funcion para regresar valor correspondiente
def cubo(p1, p2, op):
    for i in range(com):
        if(M[i][0] == p1 and M[i][1] == p2 and M[i][2] == op):
            return (M[i][3])

#Prueba
print(cubo(1,1,16))

