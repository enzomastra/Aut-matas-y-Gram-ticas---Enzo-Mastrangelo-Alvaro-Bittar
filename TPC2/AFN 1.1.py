# ejercicio: (a|b)*

def verify(string):
    text=list(string)
    i=0
    for i in range(len(text)):
        if text[i]=="a" or text[i]=="b":
            i=i+1
            if i==len(text):
                print("la cadena es valida")
        else:
            print("la cadena no es valida")
            break
string = str(input("Ingrese una cadena: "))
verify(string)