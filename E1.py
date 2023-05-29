def orden_ascendente(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

# Lista1
lista1 = [1, 2, 3, 4, 5]
if orden_ascendente(lista1):
    print("La lista 1 está ordenada de forma ascendente.")
else:
    print("La lista 1 no está ordenada de forma ascendente.")

# Lista2
lista2 = [5, 3, 2, 1]
if orden_ascendente(lista2):
    print("La lista 2 está ordenada de forma ascendente.")
else:
    print("La lista 2 no está ordenada de forma ascendente.")
