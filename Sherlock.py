from collections import Counter

class solucion:
    def __init__(self, cadena):
        self.cadena= cadena
        self.diccionario=dict(Counter(cadena))
        self.c=self.cadena[0]
        self.aux=self.diccionario[self.c]


    def step1(self):
        for i in self.diccionario:
            if self.aux != self.diccionario[i]:
                return False
            self.aux = self.diccionario[i]
        return True

    def step2(self):
        flag=False
        valores= self.diccionario.values()
        if min(valores)+1 != max(valores):
            return False
        for i in self.diccionario:
            if self.aux+1 == self.diccionario[i] or self.aux == self.diccionario[i]+1:
                if flag:
                    return False
                flag=True
        return True

    def soluc(self):
        if self.step1() or self.step2():
            return "Validacion: YES"
        else:
            return "Validacion: NO"
