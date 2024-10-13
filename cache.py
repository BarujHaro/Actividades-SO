#!/usr/bin/env python3
#Creado por Haro Salazar Fernando Baruj
import os

def clean_temporary_files():
    # Eliminar archivos temporales en /tmp
    os.system('rm -rf /tmp/*')

    # Limpiar cache de apt
    os.system('apt clean')

    # Limpiar la caché de página
    os.system('sync')
    os.system('echo 1 > /proc/sys/vm/drop_caches')

    # Limpiar la caché de I/O
    os.system('sync')
    os.system('echo 2 > /proc/sys/vm/drop_caches')

    # Limpiar tanto la caché de página como la caché de I/O
    os.system('sync')
    os.system('echo 3 > /proc/sys/vm/drop_caches')


if __name__ == "__main__":
    print("Eliminando archivos temporales y limpiando cache...")
    clean_temporary_files()
    print("Limpieza completada.")