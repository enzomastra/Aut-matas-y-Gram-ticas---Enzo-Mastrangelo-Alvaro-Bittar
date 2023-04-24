#b) URL (http-https://www……com)  (puede o no figurar el protocolo, y el www) puede terminar con la / o ?
# (query param “?clave=valor&clave=valor )

import re

url_pattern = re.compile(r'^(?:http[s]?://)?(?:www\.)?[\w.-]+\.[a-zA-Z]{2,}(?:/[\w.-]*)*(?:\?[\w=&]*)?$')

def validate_url():
    filename="urls.txt"
    with open(filename, "r") as f:
        lines = f.readlines()

    for line in lines:
        url = line.strip()
        print("Analizando:", url)
        if url_pattern.match(line):
            print("el url es valido")
        else:
            print("el url no es valido")
validate_url()