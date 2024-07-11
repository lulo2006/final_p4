import msvcrt
from prueba_funciones import *

while True:
    print("1. asignar sueldo a trabajadores")
    print("2. Clasificar sueldos")
    print("3. Revisar estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir")
    opc=input("Ingrese opción: ")
    if opc=="1":
        asignar_sueldo()
    elif opc=="2":
        clasificar_sueldos()
    elif opc=="3":
        revisar_estadisticas()
    elif opc=="4":
        reporte_de_sueldos()
    elif opc=="5":
        salir()
    else:
        print("ERROR, opción no existente")
        print("...presione una tecla para reintentar...")
        msvcrt.getch()