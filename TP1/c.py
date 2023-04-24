import re

ip_pattern=r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

def validate_ip():
    filename="ips.txt"
    with open(filename, "r") as f:
        lines = f.readlines()

    for line in lines:
        ip=line.strip()
        print("Analizando:", ip)
        if re.match(ip_pattern, line):
            print("la ip es valida")
        else:
            print("la ip no es valida")
validate_ip()