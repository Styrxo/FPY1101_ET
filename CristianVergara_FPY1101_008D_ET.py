import os
import time
import random
import csv


Trabajadores = [
    "Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Diaz", "Elena Fernández"
]

def MenuPrincipal():
    PrimerMenu = 1
    while PrimerMenu == 1:
        try:
            print(" "*10, "Menu\n")
            print("1. Asignar sueldos aleatorios.")
            print("2. Clasificar sueldos.")
            print("3. Ver estadisticas.")
            print("4. Reporte de sueldos.")
            print("5. Salir del programa.\n")
            opc = int(input("Ingrese una opción del menu: "))
            if opc == 1:
                trabajo = MenuSueldos()
                print("Sueldos ya asignados de forma aleatoria.")
            elif opc == 2:
                print("Sueldos clasificados correctamente")
                sueldo, trabajo = ClasificarSueldos()
            elif opc == 3:
                print()
                VerEstadisticas()
            elif opc == 4:
                print()
            elif opc == 5:
                PrimerMenu += 1
                print("Finalizando el programa... \nDesarrollado por Cristian Vergara \nRUT 21.698.743-8")
        except ValueError:
            print("Ingrese una opción valida.")

trabajo = []
def MenuSueldos():
    for empleado in Trabajadores:
        sueldos = random.randint(300000, 2500000)
        trabajo.append({'Nombre': Trabajadores, 'Sueldo Base': sueldos})
    return sueldos

def ClasificarSueldos():
    if not trabajo:
        print("No hay informaación añadida")
        return
    men800k = []
    entre800k = []
    mayor2mill = []
    for sueldo in trabajo:
        sueldo = sueldo['Sueldo Base']
        if sueldo < 800000:
            men800k.append(sueldo['Sueldo Base'])
        elif sueldo >= 800000 and sueldo <= 2000000:
            entre800k.append(sueldo['Sueldo Base'])
        else:
            mayor2mill.append(sueldo['Sueldo Base'])
        
        print(f"Sueldos menores a $800.000 TOTAL: {len(men800k)}")
        print("Nombre del Empleado      Sueldo")
        for sueldo in men800k:
            print(f"{men800k[0]}\t{men800k[1]}")
        
        print(f"Sueldos entre $800.000 y $2.000.000 TOTAL: {len(entre800k)}")
        print("Nombre del Empleado      Sueldo")
        for sueldo in entre800k:
            print(f"{entre800k[0]}\t{entre800k[1]}")

        print(f"Sueldos mayores a $2.000.000 TOTAL: {len(mayor2mill)}")
        print("Nombre del Empleado      Sueldo")
        for sueldo in mayor2mill:
            print(f"{mayor2mill[0]}\t{mayor2mill[1]}")
        
        SueldoTotal = len(men800k) + len(entre800k) + len(mayor2mill)
        print(f"Total Sueldos: {SueldoTotal}")

        return men800k, entre800k, mayor2mill

def VerEstadisticas():
    for i in Trabajadores:
        MasAlto = max(Trabajadores)
        MasBajo = min(Trabajadores)
    print(f"El sueldo más alto es {MasAlto}")
    print(f"El sueldo más bajo es {MasBajo}")


def ReporteSueldos(archivo_csv):
    with open(archivo_csv, "a", newline="") as archivo_csv:
        campos = ["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Liquído"]
        escritor_csv = csv.DictWriter(fieldnames=campos)
    for i in Trabajadores:
        print()

MenuPrincipal()