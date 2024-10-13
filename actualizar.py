#!/usr/bin/env python3
#Creado Fernando Baruj Haro Salazar
import os

def update_software():
    #ejecuta el comando para actualizar la lista de paquetes disponibles
    os.system('apt update')
    #Actualiza todos los paquetes instalados -y para responder si a todo
    os.system('apt upgrade -y')
#Funcion que inicia el programa
if __name__ == "__main__":
    print("Actualizando el software...")
    update_software()
    print("Actualización completada.")