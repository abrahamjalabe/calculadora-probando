print("elija una opcion: ")
print("1- SUMA")
print("2- RESTA")
print("3- DIVICION")
print("4- MULTIPLICACION")

opcion=int(input("elija una opcion"))

def SUMA(a, b):
    return(a+b)
    
def RESTA(a,b):
    return(a-b)
    
def DIVISION(a,b):
    return(a/b)
        
    
def MULTIPLICACION(a,b):
    return(a*b)

if(opcion==1):
    a=int(input("ingrese el primer num"))
    b=int(input("ingrese el segundo num"))
    print(SUMA(a,b))
elif(opcion==2):
     a=int(input("ingrese el primer num"))
     b=int(input("ingrese el segundo num"))
     print(RESTA(a,b))
elif(opcion==3):
    a=int(input("ingrese el primer num"))
    b=int(input("ingrese el segundo num"))
    if(b==0):
        print("no se puede dividir entre 0")
    else:
        print(DIVISION(a,b))
elif(opcion==4):
    a=int(input("ingrese el primer num"))
    b=int(input("ingrese el segundo num"))
    print(MULTIPLICACION(a,b))
else:
    print("elija un numero del 1 al 4")  
