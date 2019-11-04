from collections import Counter
cadena= input("Ingrese una Cadena: ")


def step1(aux):
    for i in diccionario:
        if aux != diccionario[i]:
            print("False Step1")
            return False
        aux = diccionario[i]
    print("True Step1")
    return True

def step2(aux):
    flag=False
    valores= diccionario.values()
    print(aux)
    
    if min(valores)+1 != max(valores):
        print("False Step2", min(valores), max(valores))
        return False
    
    for i in diccionario:
        print(aux, diccionario[i])
        if aux+1 == diccionario[i] or aux == diccionario[i]+1:
            
            if flag:
                print("False Step2 Bandera")
                return False
            flag=True
        
    print("True Step2")
    return True

diccionario=dict(Counter(cadena))
c=cadena[0]
aux=diccionario[c]
if step1(aux) or step2(aux):
    print("YES")
else:
    print("NO")