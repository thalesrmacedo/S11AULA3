#feito por thales
palavra = input("Digite uma palavra")
codificado = []
for letra in palavra:
    if letra == "a":
        letra = "b"
        codificado.append(letra)
    elif letra == "b":
        letra = "c"
        codificado.append(letra)
    elif letra = "c"
        letra = "d"
        codificado.append(letra)
texto = "".join(codificado)
print("Palavra criptografa:",texto)
