#Realizado por Fernando Baruj Haro Salazar 
#Seminario de SO
#Actividad 12 3.- Optimización   
from tkinter import *
from PIL import ImageTk, Image
import threading, time, random

BUFFER_SIZE = 5  # Tamaño máximo del buffer
buffer = []

root = Tk()
root.title('Act 12')
root.geometry("1000x600")
####Imagen del productor
iproductor = Image.open("productor.png")  
iproductor = iproductor.resize((120, 120))  
iproductor = ImageTk.PhotoImage(iproductor)
label_iproductor = Label(root, image=iproductor)
label_iproductor.place(x=300, y=200)
####Imagen de consumidor
iconsumidor = Image.open("consumidor.png")  
iconsumidor = iconsumidor.resize((120, 120))  
iconsumidor = ImageTk.PhotoImage(iconsumidor)
label_iconsumidor = Label(root, image=iconsumidor)
label_iconsumidor.place(x=810, y=200)
#####

# Imagen de la flecha
iflecha = Image.open("flecha.png")  
iflecha = iflecha.resize((80, 80))  
iflecha = ImageTk.PhotoImage(iflecha)
label_iflecha = Label(root, image=iflecha)

label_iflecha.place_forget()
# Creamos semáforos

# Cargar imagen de la manzana
imanzana = Image.open("manzana.png")  
imanzana = imanzana.resize((80, 80))  
imanzana = ImageTk.PhotoImage(imanzana)

# Lista de etiquetas para las imágenes de manzanas en el buffer
label_manzanas = []

# Creamos semáforos
mutex = threading.Semaphore(1)  # controla el acceso al buffer
items = threading.Semaphore(0)  # cuenta los elementos en el buffer

# Función para actualizar la posición de las imágenes de manzanas en el buffer
# Función para actualizar las imágenes de las manzanas en la interfaz gráfica
def actualizar_imagenes_manzanas():
    # Limpiar las imágenes actuales de manzanas
    for label in label_manzanas:
        label.destroy()
    
    # Crear nuevas imágenes de manzanas según el tamaño actual del buffer
    for i in range(len(buffer)):
        label = Label(root, image=imanzana)
        label_manzanas.append(label)
        label.place(x=580, y=20 + i * 100)  # Ajustar posición verticalmente

# Función para el productor
def productor():
    global buffer
    while True:
        
        item = imanzana  # imagen de la manzana
        mutex.acquire()  # adquirimos el mutex
        
        if len(buffer) < BUFFER_SIZE:
            buffer.append(item)
            root.after(0, lambda: label_iflecha.place(x=450, y=220))
              # Mostrar flecha para el productor
            # Actualizar las imágenes de las manzanas en la interfaz gráfica
            root.after(0, actualizar_imagenes_manzanas)
            print(f'Productor produjo una manzana. Buffer: {len(buffer)} / {BUFFER_SIZE}')
            
            
            
            mutex.release()  # liberamos el mutex
            items.release()  # incrementamos el contador de items
            time.sleep(random.uniform(1, 2))
            
        else:
            print("Buffer lleno. Productor espera.")
            mutex.release()  # liberamos el mutex
            time.sleep(random.uniform(8, 10))# espera antes de intentar producir de nuevo

# Función para el consumidor
def consumidor():
    global buffer
    while True:
        items.acquire()  # decrementa el contador de items
        mutex.acquire()  # adquirimos el mutex
        if buffer:
            buffer.pop(0)  # consumimos el primer elemento del buffer
            root.after(0, lambda: label_iflecha.place(x=700, y=220))
            # Actualizar las imágenes de las manzanas en la interfaz gráfica
            root.after(0, actualizar_imagenes_manzanas)
            print(f'Consumidor consumió una manzana. Buffer: {len(buffer)} / {BUFFER_SIZE}')
            
            
            mutex.release() 
            
            # Pausar el programa durante el tiempo aleatorio calculado
            time.sleep(random.uniform(1, 3))
            
        else:
            print("Buffer vacío. Consumidor espera.")
            mutex.release()  # liberamos el mutex
            time.sleep(random.uniform(8, 9))# espera un antes de intentar consumir de nuevo

# Creamos los hilos para productor y consumidor
productor_thread = threading.Thread(target=productor)
consumidor_thread = threading.Thread(target=consumidor)

def iniciar():
    # Iniciamos los hilos
    productor_thread.start()
    time.sleep(5)
    consumidor_thread.start()

# Creamos las etiquetas de las imágenes de manzanas iniciales en el buffer
for i in range(BUFFER_SIZE):
    label = Label(root, image=imanzana)
    label_manzanas.append(label)

# Mostrar las imágenes de manzanas inicialmente en la interfaz gráfica

comenzar = Button(root, text="Iniciar Proceso", padx=50, command=iniciar)
comenzar.place(x=50, y=50)
root.mainloop()