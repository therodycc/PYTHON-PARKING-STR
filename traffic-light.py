import time
import os

def show_trafficLight(status):
    os.system('cls' if os.name == 'nt' else 'clear')

    red = "🔴" if status == "red" else "⚫️"
    amarillo = "🟡" if status == "amarillo" else "⚫️"
    verde = "🟢" if status == "verde" else "⚫️"

    print("┌─────────────┐")
    print("│             │")
    print(f"│     {red}      │")
    print("│             │")
    print(f"│     {amarillo}      │")
    print("│             │")
    print(f"│     {verde}      │")
    print("│             │")
    print("└─────────────┘")

def trafficLight():
    while True:
        show_trafficLight("verde")
        time.sleep(5)

        show_trafficLight("amarillo")
        time.sleep(2)

        show_trafficLight("red")
        time.sleep(5)

trafficLight()
