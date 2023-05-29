class Cola:
    def __init__(self):
        self.items = []

    def vacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.append(item)
        print(f"Se ha agregado el elemento {item} al final de la cola.")
        print(f"La cola ahora es: {self.items}")

    def retirar(self):
        if not self.vacia():
            elemento_retirado = self.items.pop(0)
            print(f"Se ha retirado el elemento {elemento_retirado} del inicio de la cola.")
            print(f"La cola ahora es: {self.items}")
            return elemento_retirado
        else:
            print("La cola está vacía. No se puede retirar ningún elemento.")

    def tamano(self):
        return len(self.items)

# Ejemplo de uso
mi_cola = Cola()
mi_cola.agregar(1)
mi_cola.agregar(2)
mi_cola.agregar(3)
mi_cola.retirar()
mi_cola.retirar()
mi_cola.retirar()
mi_cola.retirar()
