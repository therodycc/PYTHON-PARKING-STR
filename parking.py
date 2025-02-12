import threading
import time
import random

class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.occupied = {}
        self.available = list(range(1, capacity + 1))
        self.lock = threading.Lock()

    def register_entry(self, plate):
        with self.lock:
            if not self.available:
                print("🚫 Estacionamiento lleno. No hay espacios disponibles.")
                return
            if plate in self.occupied:
                print("⚠️ El vehículo ya está registrado en el estacionamiento.")
                return
            space = self.available.pop(0)
            self.occupied[plate] = space
            print(f"✅ Vehículo {plate} estacionado en el espacio {space}.")
            self.draw_parking_lot()

    def register_exit(self, plate):
        with self.lock:
            if plate not in self.occupied:
                print("⚠️ Este vehículo no está registrado en el estacionamiento.")
                return
            space = self.occupied.pop(plate)
            self.available.append(space)
            self.available.sort()
            print(f"🚗 Vehículo {plate} ha salido del estacionamiento (Espacio {space} liberado).")
            self.draw_parking_lot()

    def show_status(self):
        with self.lock:
            print("\n📊 Estado del Estacionamiento:")
            print(f"🚗 Capacidad total: {self.capacity} | 🚫 Ocupados: {len(self.occupied)} | 🟩 Disponibles: {len(self.available)}")
            if self.occupied:
                print("Vehículos estacionados:")
                for plate, space in self.occupied.items():
                    print(f" - {plate} en espacio {space}")
            else:
                print("🟢 No hay vehículos estacionados.")
            self.draw_parking_lot()

    def draw_parking_lot(self):
        print("\n🅿️ Estacionamiento:")
        for i in range(1, self.capacity + 1):
            if i in self.available:
                print("[🟩]", end=" ") 
            else:
                print("[🚗]", end=" ") 
            if i % 10 == 0:
                print()
        print("\n ---------------------------------------------------------------------------")

    def automatic_simulation(self):
        while True:
            time.sleep(random.randint(3, 5)) 
            if random.choice([True, False]):
                plate = f"ABC-{random.randint(100, 999)}"
                self.register_entry(plate)
                self.show_status()
            else:
                if self.occupied:
                    plate = random.choice(list(self.occupied.keys()))
                    self.register_exit(plate)
                    self.show_status()

def menu():
    parking_lot = ParkingLot(3)
    
    print("Starting simulation thread...")
    simulation_thread = threading.Thread(target=parking_lot.automatic_simulation, daemon=True)
    simulation_thread.start()

    time.sleep(60)

    print("\nFin del programa.")

menu()
