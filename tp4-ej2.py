################
# Juan Ignacio Bruni - @Juanbruni
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def suma_lenta(numero, otro_numero):
    suma_en_pantalla=0
    numero_menor=0
    resultado_suma=numero+otro_numero


    if numero > otro_numero:
        numero_menor=otro_numero
        print(f"\nEmpezamos desde:  {numero_menor}")
    else:
        numero_menor=numero
        print(f"\nEmpezamos desde:  {numero_menor}")

        
    if resultado_suma < 0 and (numero < 0 > otro_numero):
        while suma_en_pantalla != resultado_suma:
            suma_en_pantalla = numero_menor - 1
            print(f"{numero_menor} + (-1)  =  {suma_en_pantalla}")
            numero_menor=numero_menor-1
            

            
    elif (numero == 0 or otro_numero == 0):
        print(f" {numero_menor} + {otro_numero}  = {suma_en_pantalla}")
        

        
    else:
        while suma_en_pantalla != resultado_suma:
            suma_en_pantalla = numero_menor + 1
            print(f"{numero_menor} + 1  = {suma_en_pantalla}")
            numero_menor=numero_menor+1


            
    print(f"El resultado final es:  {resultado_suma}")
def prueba():
    saludo="Suma lenta"
    saludo_titulo= saludo.upper()
    print(saludo_titulo+ "\n")
    
    numero = int(input("Ingrese el numero A: "))
    otro_numero= int(input("Ingrese el numero B: "))
    suma_lenta(numero, otro_numero)

if __name__ == "__main__":
    prueba()
