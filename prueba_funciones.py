#funciones

import random, time, os, csv

#Variables
aleatorio = random.randint(300000, 2500000)
trabajadores = ['Juan Pérez','María García','Carlos López','Ana Martínez','Pedro Rodríguez','Laura Hernández','Miguel Sánchez','Isabel Gómez','Francisco Díaz','Elena Fernández']
clasificador = []
report_sueldos = []

#OPC 1
def asignar_sueldo():
    print(aleatorio)
    
#OPC 2
def clasificar_sueldos():
    print(clasificador)
#OPC 3
def revisar_estadisticas():
    print
#OPC 4
def reporte_de_sueldos():
    report_sueldos
#OPC 5
def salir():
    print("Finalizando programa...")
    time.sleep(2)
    os.system('cls')
    print("Desarrollado por Jaime Rodriguez")
    time.sleep(1)
    print("RUT 22.129.883-7")
    exit()