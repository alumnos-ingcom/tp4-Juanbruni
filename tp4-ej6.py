################
# Juan Ignacio Bruni - @Juanbruni
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def prueba():
    saludo="Máximo / Mínimo "
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    lista=[]
    ingreso=0
    
    while ingreso != "":
        ingreso=input("Ingrese un numero: ")
        lista.append(ingreso)
    else:
        lista.pop()
        lista.sort()
        minimo(lista)
        maximo(lista)

def minimo(lista):
    minimo=lista[0]
    print(f"Minimo es: {minimo}")

def maximo(lista):
    lista.reverse()
    maximo=lista[0]
    print(f"Máximo es: {maximo}")
    
if __name__ == "__main__":
    prueba()