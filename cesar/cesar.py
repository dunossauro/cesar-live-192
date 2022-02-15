from string import ascii_lowercase


def encripta(frase, rot=13):
    """Encripta o texto."""
    encriptado = ''
    for letra in frase:
        letra = letra.lower()
        if letra == ' ':
            encriptado += letra
        elif letra not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(letra) + rot
            letra = ascii_lowercase[pos % 26]
            encriptado += letra
    return encriptado


def decripta(frase, rot=13):
    """Decripta o texto."""
    decriptado = ''
    for letra in frase:
        letra = letra.lower()
        if letra == ' ':
            decriptado += letra
        elif letra not in ascii_lowercase:
            ...
        else:
            pos = ascii_lowercase.find(letra) - rot
            letra = ascii_lowercase[pos % 26]
            decriptado += letra
    return decriptado
