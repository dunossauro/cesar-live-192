from string import ascii_lowercase
def encripta(frase,n=13):
    """encripta o texto"""
    encriptado = ""
    for l in frase:
        l = l.lower()
        if l == ' ':
            encriptado += l
        elif l not in ascii_lowercase: ...
        else:
            pos = ascii_lowercase.find(l) + n
            l = ascii_lowercase[pos % 26]
            encriptado += l
    return encriptado

def decripta(frase,n=13):
    """decripta o texto"""
    decriptado = ""
    for l in frase:
        l = l.lower()
        if l == ' ':
            decriptado += l
        elif l not in ascii_lowercase: ...
        else:
            pos = ascii_lowercase.find(l) - n
            l = ascii_lowercase[pos % 26]
            decriptado += l
    return decriptado
