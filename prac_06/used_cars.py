"""
CP1404/CP5632 Practical - The import statement includes a folder (module) structure.
This emphasizes the importance of naming folders with no spaces or capitals for valid module names.
"""
from prac_06.car import Car

def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My car", 180)
    my_car.drive(30)
    print(f"fuel: {my_car.fuel}")
    print(my_car)

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo)

main()