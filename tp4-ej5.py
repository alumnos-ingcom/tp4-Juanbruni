################
# Juan Ignacio Bruni - @Juanbruni
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def prueba():
    saludo="Números positivos y negativos"
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    numero=int(input("Ingrese su número: "))
    
    signo(numero)
    
def signo(numero):
    if numero < 0:
        print(f"{numero} es negativo")
    elif numero==0:
        print(f"el numero {numero} es cero")
    else:
        print(f"el numero {numero} es positivo")

if __name__ == "__main__":
    prueba()