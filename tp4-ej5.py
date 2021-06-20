################
# Juan Ignacio Bruni - @Juanbruni
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

    
    
    
def signo(numero):
    if numero < 0:
        return -1
    elif numero==0:
        return 0
    else:
        return 1

def prueba():
    saludo="Números positivos y negativos"
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    numero=int(input("Ingrese su número: "))
    signo(numero)
    resultado=signo(numero)
    if resultado==-1:
        print (f"resultado negativo")
    elif resultado==0:
        print (f"reusltado cero")
    else:
        print(f"resultado postivo")
    
if __name__ == "__main__":
    prueba()