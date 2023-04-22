def verify(string):
    if set(string)-set("ab"):
        print("la cadena es incorrecta")
    else:
        state = "A"
        for i in string:
            if state == "A":
                if i == "a":
                    state = "B"
                elif i == "b":
                    state = "C"
            elif state == "B":
                if i == "a":
                    state = "D"
                elif i == "b":
                    state = "C"
            elif state == "C":
                if i == "a":
                    state = "B"
                elif i == "b":
                    state = "C"
            elif state == "D":
                if i == "a":
                    state = "D"
                elif i == "b":
                    state = "C"
        print(state)

string = str(input("Ingrese una cadena: "))
verify(string)