################
# Juan Ignacio Bruni - @Juanbruni
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
def prueba():
    saludo="Palíndromo "
    saludo_titulo= saludo.upper()
    print(saludo_titulo+"\n")
    texto=input("Ingrese su palabra o texto: ")
    texto=texto.lower()
    es_palindromo(texto)
    
def es_palindromo(texto):
    reverse_txt= texto[::-1]
    if texto==reverse_txt:
        print("Verdadero")
    else:
        print("Falso")
    
if __name__ == "__main__":
    prueba()