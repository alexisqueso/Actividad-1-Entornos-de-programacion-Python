class Vehículo:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f"El vehículo {self.marca} ha sido vendido.")
        else:
            print(f"El vehículo {self.marca} no está disponible.")

    def estado(self):
        return self.disponible

    def get_price(self):
        return self.precio

class Auto(Vehículo):
    def start(self):
        if self.disponible:
            return f"El motor del coche {self.marca} está en marcha."
        else:
            return f"El coche {self.marca} no está disponible."

    def stop(self):
        if self.disponible:
            return f"El motor del coche {self.marca} se ha detenido."
        else:
            return f"El coche {self.marca} no está disponible."

class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.autos = []

    def comprar_auto(self, auto):
        if auto.estado():
            self.autos.append(auto)
            auto.vender()
        else:
            print(f"Lo siento, el coche {auto.marca} {auto.modelo} no está disponible.")

class Concesionaria:
    def __init__(self):
        self.inventario = []
        self.clientes = []

    def añadir_auto(self, auto):
        self.inventario.append(auto)
        print(f"El coche {auto.marca} {auto.modelo} ha sido añadido al inventario.")

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"El cliente {cliente.nombre} ha sido registrado en la concesionaria.")

    def mostrar_disponibles(self):
        print("Coches disponibles en la concesionaria:")
        for auto in self.inventario:
            if auto.estado():
                print(f"- {auto.marca} {auto.modelo} por {auto.get_price()}")

# Crear autos
auto1 = Auto("Nissan", "Skyline", 20000)
auto2 = Auto("Honda", "Civic", 22000)
auto3 = Auto("Ford", "Mustang", 35000)

# Crear cliente
cliente = Cliente("Daniela")

# Crear concesionaria
concesionaria = Concesionaria()
concesionaria.añadir_auto(auto1)
concesionaria.añadir_auto(auto2)
concesionaria.añadir_auto(auto3)
concesionaria.registrar_cliente(cliente)

# Mostrar autos disponibles antes de la compra
print("\nCoches disponibles en la concesionaria antes de la compra:")
concesionaria.mostrar_disponibles()

# Comprar un auto
print(f"\nDaniela intenta comprar el coche {auto1.marca} {auto1.modelo} que cuesta {auto1.get_price()}.")
cliente.comprar_auto(auto1)

# Mostrar autos disponibles después de la compra
print("\nCoches disponibles en la concesionaria después de la compra:")
concesionaria.mostrar_disponibles()


