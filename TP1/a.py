#a)Email  (nombre@dominio.com) (el nombre debe comenzar con letra y puede tener números, _, puntos y -)
# (definir 5 dominios y 5 países)

def valid_email(email):
    state=0
    valid_domains=["gmail", "yahoo", "hotmail", "outlook", "aol"]
    valid_dots=["com"]
    valid_subdomains=["us", "uk", "ca", "au", "in"]
    if state==0:
        if email.count("@")!=1 or email.startswith("@") or email.endswith("@"):
            print("el correo ingresado no es valido")
        else:
            state=1

    if state==1:
        username,domain=email.split("@")
        if not username[0].isalpha() or not all(c.isalnum() or c in (".", "_", "-") or c == "." or c == "-" or c == "_" for c in username[1:]):
            print("el correo ingresado no es valido")
        else:
            state=2

    if state==2:
        domain_parts = domain.split(".")
        if len(domain_parts)==2:
            if domain_parts[0] in valid_domains and domain_parts[1] in valid_dots:
                state=3
            else:
                print("el correo ingresado no es valido")
        elif len(domain_parts)==3:
            if domain_parts[0] in valid_domains and domain_parts[1] in valid_dots and domain_parts[2] in valid_subdomains:
                state=3
            else:
                print("el correo ingresado no es valido")
        else:
            print("el correo ingresado no es valido")
    if state==3:
        print("el correo ingresado es valido")

filename="emails.txt"
with open(filename, "r") as f:
    lines = f.readlines()

for line in lines:
    email = line.strip()
    print("Analizando:", email)
    valid_email(email)
