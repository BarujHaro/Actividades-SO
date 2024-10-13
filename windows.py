#Creado por Fernando Baruj Haro Salazar
import os
import shutil
import tempfile
#Os para interactuar con el sistema operativo
#shutil para operaciones con archivos

def clean_temporary_files():
    # Eliminar archivos temporales en la carpeta temporal predeterminada de Windows
    temp_dir = tempfile.gettempdir()
    #Se eliminan los archivos temporales en la carpeta predeterminadas
    for root, dirs, files in os.walk(temp_dir):
        for file in files:
            try:
                #Elimina al archivo
                os.remove(os.path.join(root, file))
            except Exception as e:
                #maneja errores durante la eliminacion
                print(f"No se pudo eliminar {os.path.join(root, file)}: {e}")

    # Limpiar la caché del sistema
    try:
        #Elimina de la carpeta temp en localappdata
        shutil.rmtree(os.path.join(os.getenv('LOCALAPPDATA'), 'Temp'), ignore_errors=True)
        #Elimina d ela carpeta cache en appdata
        shutil.rmtree(os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Caches'), ignore_errors=True)
    except Exception as e:
        print(f"No se pudo limpiar la caché del sistema: {e}")

if __name__ == "__main__":
    print("Eliminando archivos temporales y limpiando caché...")
    clean_temporary_files()
    print("Limpieza completada.")
