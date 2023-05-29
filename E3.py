def palindromo(palabra):
    pila = []
    for letra in palabra:
        pila.append(letra)
    palabra_invertida = ""
    while len(pila) > 0:
        palabra_invertida += pila.pop()
    return palabra == palabra_invertida

palabra = "reconocer"
if palindromo(palabra):
    print(f"La palabra: {palabra} es un palíndromo")
else:
    print(f"La palabra: {palabra} no es un palíndromo")
