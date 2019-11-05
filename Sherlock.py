from collections import Counter
import re

class solucion:
    def __init__(self, cadena):
        self.cadena=cadena
        self.diccionario=dict(Counter(cadena))
        self.c=self.cadena[0]
        self.aux=self.diccionario[self.c]

    def verificacion(self): #Esta funcion verifica que la cadena ingresada sea valida
        if "!" in self.cadena:
            return "\nIngrese una cadena\n de letras minusculas"

        cadena = self.cadena + "!"

        if not re.match(r"^[a-z]{1,100000}!", cadena):
            return "\nIngresar una cadena\n de letras minusculas"
        else:
            return None

    def step1(self):    #Esta funcion valida todas las cadenas cuyas frecuencias de caracteres sean iguales
        for i in self.diccionario:
            if self.aux != self.diccionario[i]:
                return False
            self.aux = self.diccionario[i]
        return True

    def step2(self):
        flag=False
        valores= self.diccionario.values()

        # Con el siguiente IF descarto todas las cadenas cuyas frecuencia de caracter maxima y minima sea > 1. 
        # Ej: si s=abbccc entonces como la diferencia entre la frecuencia menor (a:1) y la frecuencia mayor (c:3) 
        # es > 1 entonces se descarta

        if min(valores)+1 != max(valores):
            return False

        #Este ciclo valida cadenas a las cuales si se les remueve un caracter, el cadena resultante tiene frecuencias 
        # de caracteres iguales

        for i in self.diccionario:      
            if max(valores) == self.diccionario[i]:
                if flag:
                    return False
                flag=True
        return True

    def soluc(self):    # Revisa si el paso 1 o el paso 2 son verdaderos
        if self.step1() or self.step2():
            return "Validacion: YES"
        else:
            return "Validacion: NO"
