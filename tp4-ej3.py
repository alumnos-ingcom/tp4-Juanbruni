################
# Juan Ignacio Bruni - @Juanbruni
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

    
def convertir_a_fahrenheit(centigrados):
    fahrenheit= (centigrados * 9/5) + 32
    print(f"Farenheit: {fahrenheit}°")

def convertir_a_centigrados(fahrenheit):
    centigrados= (fahrenheit - 32) * 5/9
    print(f"Centigrados: {centigrados}°")
 
def prueba():
    saludo="Conversión de temperaturas"
    saludo_titulo= saludo.upper()
    print(saludo_titulo+ "\n")
    centigrados=float(input("ingrese el numero en fahrenheit: "))
    fahrenheit=float(input("ingrese el numero en centigrado: "))
    convertir_a_centigrados(fahrenheit)
    convertir_a_fahrenheit(centigrados)
    
if __name__ == "__main__":
    prueba()
