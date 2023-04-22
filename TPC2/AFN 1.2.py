def verify (string):
    if string[0]==" ":
        string=string[1:]
    state=1
    for i in string:
        if state==1:
            if i=="a":
                state=2
            elif i=="b":
                state = 4
            elif i==" ":
                state=5
        elif state==2:
            if i=="a":
                state=3
            else:
                print("la cadena no es valida")
                break
        elif state==3 or state==4:
            state=5
        elif state==5:
            if i=="a":
                state=6
            elif i=="b":
                state=7
            elif i==" ":
                state=10
        elif state==6 or state==8:
            state=9
        elif state==7:
            if i=="b":
                state=8
            else:
                print("la cadena no es valida")
                break
        elif state==9:
            state=5
        elif state==10:
            if i=="a":
                state=6
            elif i=="b":
                state=7
            elif i==" ":
                state=11
        elif state==11:
            if i=="a":
                state=2
            elif i=="b":
                state=4
            elif i==" ":
                state=12
        elif state==12:
            if i=="a":
                state=6
            elif i=="b":
                state=7
            elif i==" ":
                state=13
        elif state==13:
            print("la cadena no es valida")
            break

string = str(input("Ingrese una cadena: "))
verify(string)