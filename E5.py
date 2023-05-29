def simetrica(lista):
    longitud = len(lista)
    mitad = longitud // 2

    # Compara la primera mitad con la segunda mitad invertida
    if longitud % 2 == 0:
        return lista[:mitad] == lista[mitad:][::-1]
    else:
        return lista[:mitad] == lista[mitad+1:][::-1]


# Ejemplo
lista1 = [1, 2, 3, 4, 3, 2, 1]
lista2 = [1, 2, 3, 4, 5, 6, 7]

if simetrica(lista1):
    print("La lista 1 es simétrica")
else:
    print("La lista 1 no es simétrica")

if simetrica(lista2):
    print("La lista 2 es simétrica")
else:
    print("La lista 2 no es simétrica")
