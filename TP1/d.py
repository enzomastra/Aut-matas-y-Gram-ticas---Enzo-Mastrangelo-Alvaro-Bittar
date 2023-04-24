
def cant(text):
    words = text.split()
    cant_words = len(words)
    print("La cantidad de palabras es:", cant_words)

def most_used(text):
    words = text.split()
    frecuencies = {}
    for word in words:
        if word in frecuencies:
            frecuencies[word]+=1
        else:
            frecuencies[word]=1

    most_common=None
    cant_rep=0
    for word, frecuency in frecuencies.items():
        if frecuency > cant_rep:
            most_common= word
            cant_rep=frecuency
    print("La palabra más repetida es: ", most_common, " con", cant_rep, "repeticiones.")

filename="textoejd.txt"
with open(filename, encoding="UTF-8") as f:
    text=f.read()
    cant(text)
    most_used(text)