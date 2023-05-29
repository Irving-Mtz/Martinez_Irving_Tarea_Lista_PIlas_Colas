class Pila:
    def __init__(self):
        self.items = []

    def vacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.append(item)
        print(f"Se ha agregado el elemento {item} a la pila. La pila ahora es: {self.items}")

    def retirar(self):
        if not self.vacia():
            elemento_retirado = self.items.pop()
            print(f"Se ha retirado el elemento {elemento_retirado} de la pila. La pila ahora es: {self.items}")
            return elemento_retirado
        else:
            print("La pila está vacía. No se puede retirar ningún elemento.")

    def ver(self):
        if not self.vacia():
            return self.items[len(self.items)-1]
        else:
            print("La pila está vacía.")

    def tamano(self):
        return len(self.items)


pila = Pila()
print("Pila creada.")
print("Agregando elementos a la pila...")
pila.agregar(1)
pila.agregar(2)
pila.agregar(3)
print(f"El tamaño de la pila es: {pila.tamano()}")
print("Retirando elementos de la pila...")
pila.retirar()
pila.retirar()
pila.retirar()

