# Clase base Vehicle
class Vehicle:
    # Constructor de la clase Vehicle. Define los atributos iniciales del vehículo.
    def __init__(self, brand, model, price):
        # Atributo para la marca del vehículo (ej. Toyota, Ford)
        self.brand = brand
        # Atributo para el modelo del vehículo (ej. Corolla, Mustang)
        self.model = model
        # Atributo para el precio del vehículo
        self.price = price
        # Atributo para verificar si el vehículo está disponible (por defecto True)
        self.is_available = True
    
    # Método para vender el vehículo
    def sell(self):
        # Verifica si el vehículo está disponible para la venta
        if self.is_available:
            # Cambia el estado del vehículo a no disponible
            self.is_available = False
            print(f"El vehículo {self.brand} ha sido vendido.")
        else:
            # Mensaje si el vehículo ya no está disponible
            print(f"El vehículo {self.brand} no está disponible.")
    
    # Método para verificar si el vehículo está disponible
    def check_available(self):
        return self.is_available
    
    # Método para obtener el precio del vehículo
    def get_price(self):
        return self.price
    
    # Método abstracto para iniciar el motor del vehículo
    def start_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
    # Método abstracto para detener el motor del vehículo
    def stop_engine(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")

# Subclase Car que hereda de Vehicle
class Car(Vehicle):
    # Método para iniciar el motor del coche
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} está en marcha."
        else:
            return f"El coche {self.brand} no está disponible."
        
    # Método para detener el motor del coche
    def stop_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} se ha detenido."
        else:
            return f"El coche {self.brand} no está disponible."

# Subclase Bike que hereda de Vehicle
class Bike(Vehicle):
    # Método para iniciar el motor de la bicicleta
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} está en marcha."
        else:
            return f"La bicicleta {self.brand} no está disponible."
        
    # Método para detener el motor de la bicicleta
    def stop_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} se ha detenido."
        else:
            return f"La bicicleta {self.brand} no está disponible."

# Subclase Truck que hereda de Vehicle
class Truck(Vehicle):
    # Método para iniciar el motor del camión
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} está en marcha."
        else:
            return f"El camión {self.brand} no está disponible."
        
    # Método para detener el motor del camión
    def stop_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} se ha detenido."
        else:
            return f"El camión {self.brand} no está disponible."

# Clase Customer para manejar los clientes
class Customer:
    # Constructor de la clase Customer
    def __init__(self, name):
        # Atributo para el nombre del cliente
        self.name = name
        # Lista para almacenar los vehículos comprados por el cliente
        self.purchased_vehicles = []

    # Método para que el cliente compre un vehículo
    def buy_vehicle(self, vehicle: Vehicle):
        # Verifica si el vehículo está disponible
        if vehicle.check_available():
            # Si está disponible, lo vende y lo añade a la lista de vehículos comprados
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} no está disponible.")

    # Método para consultar la disponibilidad de un vehículo
    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availablity = "Disponible"
        else:
            availablity = "No disponible"
        # Muestra el estado de disponibilidad y el precio del vehículo
        print(f"El {vehicle.brand} está {availablity} y cuesta {vehicle.get_price()}.")

# Clase Dealership para manejar la concesionaria
class Dealership:
    # Constructor de la clase Dealership
    def __init__(self):
        # Lista para almacenar el inventario de vehículos
        self.inventory = []
        # Lista para almacenar los clientes registrados
        self.customers = []

    # Método para añadir vehículos al inventario
    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario.")

    # Método para registrar clientes
    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido.")

    # Método para mostrar los vehículos disponibles en el inventario
    def show_available_vehicle(self):
        print("Vehículos disponibles en la tienda:")
        for vehicle in self.inventory:
            if vehicle.check_available():
                # Muestra los vehículos disponibles y sus precios
                print(f" - {vehicle.brand} por {vehicle.get_price()}.")

#EJEMPLO PARA EL CODIGO:
# Creamos instancias de vehículos
car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "YZF-R3", 5000)
truck1 = Truck("Ford", "F-150", 30000)

# Creamos una instancia de Dealership (Concesionaria)
dealership = Dealership()

# Agregamos los vehículos al inventario de la concesionaria
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

# Creamos una instancia de Customer (Cliente)
customer1 = Customer("Juan")

# Registramos al cliente en la concesionaria
dealership.register_customers(customer1)

# Mostramos los vehículos disponibles en la concesionaria
dealership.show_available_vehicle()

# El cliente consulta el precio y disponibilidad de un vehículo
customer1.inquire_vehicle(car1)

# El cliente decide comprar el vehículo 'car1'
customer1.buy_vehicle(car1)

# Verificamos si el vehículo se ha vendido, intentamos encender el motor
print(car1.start_engine())  # Debe mostrar que el motor está en marcha si fue vendido

# Intentamos vender nuevamente el mismo vehículo para mostrar el manejo de disponibilidad
customer1.buy_vehicle(car1)  # Debería indicar que ya no está disponible

# Mostramos nuevamente los vehículos disponibles en la concesionaria después de la venta
dealership.show_available_vehicle()

# El cliente intenta encender y apagar el motor de la bicicleta
print(bike1.start_engine())  # No está vendido aún, debería decir "no disponible"
customer1.buy_vehicle(bike1)  # Ahora compra la bicicleta
print(bike1.start_engine())  # Ahora debería decir que el motor de la bicicleta está en marcha
print(bike1.stop_engine())    # Apagamos el motor de la bicicleta

# El cliente intenta encender y apagar el motor del camión
print(truck1.start_engine())  # No está vendido aún, debería decir "no disponible"
customer1.buy_vehicle(truck1) # Ahora compra el camión
print(truck1.start_engine())  # Ahora debería decir que el motor del camión está en marcha
print(truck1.stop_engine())   # Apagamos el motor del camión
