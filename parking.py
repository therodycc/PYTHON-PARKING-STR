import threading
import time
import random

class Estacionamiento:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.ocupados = {}
        self.disponibles = list(range(1, capacidad + 1))
        self.lock = threading.Lock()

    def registrar_entrada(self, placa):
        with self.lock:
            if not self.disponibles:
                print("🚫 Estacionamiento lleno. No hay espacios disponibles.")
                return
            if placa in self.ocupados:
                print("⚠️ El vehículo ya está registrado en el estacionamiento.")
                return
            espacio = self.disponibles.pop(0)
            self.ocupados[placa] = espacio
            print(f"✅ Vehículo {placa} estacionado en el espacio {espacio}.")
            self.dibujar_estacionamiento()

    def registrar_salida(self, placa):
        with self.lock:
            if placa not in self.ocupados:
                print("⚠️ Este vehículo no está registrado en el estacionamiento.")
                return
            espacio = self.ocupados.pop(placa)
            self.disponibles.append(espacio)
            self.disponibles.sort()
            print(f"🚗 Vehículo {placa} ha salido del estacionamiento (Espacio {espacio} liberado).")
            self.dibujar_estacionamiento()

    def mostrar_estado(self):
        with self.lock:
            print("\n📊 Estado del Estacionamiento:")
            print(f"Capacidad total: {self.capacidad}")
            print(f"Espacios ocupados: {len(self.ocupados)}")
            print(f"Espacios disponibles: {len(self.disponibles)}")
            if self.ocupados:
                print("Vehículos estacionados:")
                for placa, espacio in self.ocupados.items():
                    print(f" - {placa} en espacio {espacio}")
            else:
                print("🟢 No hay vehículos estacionados.")
            self.dibujar_estacionamiento()

    def dibujar_estacionamiento(self):
        print("\n🅿️ Estacionamiento:")
        for i in range(1, self.capacidad + 1):
            if i in self.disponibles:
                print("[🟩]", end=" ")  # Espacio disponible
            else:
                print("[🚗]", end=" ")  # Espacio ocupado
            if i % 10 == 0:
                print()
        print("\n")

    def simulacion_automatica(self):
        while True:
            time.sleep(random.randint(5, 10))  # Simula una acción cada 5-10 segundos
            if random.choice([True, False]):
                # Registrar entrada
                placa = f"ABC-{random.randint(100, 999)}"
                self.registrar_entrada(placa)
            else:
                # Registrar salida si hay vehículos estacionados
                if self.ocupados:
                    placa = random.choice(list(self.ocupados.keys()))
                    self.registrar_salida(placa)

def menu():
    capacidad = int(input("Ingrese la capacidad del estacionamiento: "))
    estacionamiento = Estacionamiento(capacidad)
    
    # Iniciar simulación automática en un hilo
    hilo_simulacion = threading.Thread(target=estacionamiento.simulacion_automatica, daemon=True)
    hilo_simulacion.start()
    
    while True:
        print("\n=== Menú del Estacionamiento ===")
        print("1. Registrar entrada de vehículo")
        print("2. Registrar salida de vehículo")
        print("3. Mostrar estado del estacionamiento")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            placa = input("Ingrese la placa del vehículo: ")
            estacionamiento.registrar_entrada(placa)
        elif opcion == "2":
            placa = input("Ingrese la placa del vehículo a retirar: ")
            estacionamiento.registrar_salida(placa)
        elif opcion == "3":
            estacionamiento.mostrar_estado()
        elif opcion == "4":
            print("👋 Saliendo del sistema de estacionamiento. ¡Hasta pronto!")
            break
        else:
            print("❌ Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
