#codigo creado por Fernando Baruj Haro Salazar
#seminario de SO
from tkinter import *
import threading
import time
root = Tk()
root.title('Act 14 (Bloqueo mutuo) - Haro Salazar Fernando Baruj')
root.geometry("600x400")
# Creamos un objeto Lock para manejar el bloqueo mutuo
lock = threading.Lock()
###########Imagenes
#Imagen del plato
imagen_path='food.png'
imagen = PhotoImage(file=imagen_path).subsample(8)
label = Label(root, image=imagen)
label.image = imagen   
#imagen de mesero
imagen_w='waiter.png'
imagenw = PhotoImage(file=imagen_w).subsample(8)
labelw1 = Label(root, image=imagenw)
labelw1.image = imagenw  
labelw1.place(x=150, y=200) 
labelw2 = Label(root, image=imagenw)
labelw2.image = imagenw  
labelw2.place(x=400, y=200) 
#Imagen del recurso (Platillo principal donde se tomand los platos)
imagen_d='dinner.png'
imagend = PhotoImage(file=imagen_d).subsample(8)
labeld = Label(root, image=imagend)
labeld.image = imagend
labeld.place(x=280, y=200)
#########Texto
# Creamos una etiqueta para mostrar los mensajes del mesero
label_status1 = Label(root, text="", font=("Arial", 11))
label_status1.pack()
label_status1.place(x=40, y=300)
label_status2 = Label(root, text="", font=("Arial", 11))
label_status2.pack()
label_status2.place(x=320, y=300)
######## Función que simula al mesero 1 recogiendo platos
#Simula el proceso continuo de un mesero que recoge platos, los entrega al cliente y los regresa para repetir el proceso
#Con ayuda del lock se maneja el bloqueo mutuo
def mesero_1():
    time.sleep(2)
    global lock #Se accede a la variable del lock
    while True:
        #En un bucle se simula un trabajo continuo del mesero 
        print("Mesero 1 intentando recoger platos...")
        label_status1.config(text="Mesero 1 intentando recoger platos...") #Indica el estado de espera
        #Adquiere el bloqueo para realizar acciones criticas de manera exclusiva
        with lock:
            #Indica que el mesero recoge el plato
            print("Mesero 1 recogiendo plato")
            label_status1.config(text="Mesero 1 recogiendo plato")
            time.sleep(1)
            labeld.place_forget()
            time.sleep(1)
            #Indica que el mesero recogieo el plato y lo esta sirviendo al cliente
            label.place(x=50, y=200) 
            print("Mesero 1 sirviendo")
            label_status1.config(text="Mesero 1 sirviendo")
            time.sleep(2)  
            #Despues de servirlo lo que hace es regresar el plato para repetir el proceso y liberar el bloqueo
            label.place_forget()
            labeld.place(x=280, y=200)
            print("Mesero 1 regresando plato")
            label_status1.config(text="Mesero 1 regresando plato")
            time.sleep(2)
            labeld.place_forget()
        print("Mesero 1 intentando recoger platos...")
        label_status1.config(text="Mesero 1 intentando recoger platos...")
        time.sleep(2)  

# Función que simula al mesero 2 recogiendo platos
def mesero_2():
    time.sleep(2)
    global lock
    while True:
        print("Mesero 2 intentando recoger platos...")
        label_status2.config(text="Mesero 2 intentando recoger platos...")
        with lock:
            print("Mesero 2 recogiendo plato")  #Indica que el mesero recoge el plato
            label_status2.config(text="Mesero 2  recogiendo plato")
            time.sleep(1)
            labeld.place_forget()
            time.sleep(1)#Indica que el mesero recogieo el plato y lo esta sirviendo al cliente
            label.place(x=500, y=200) 
            print("Mesero 2 sirviendo")
            label_status2.config(text="Mesero 2 sirviendo")
            time.sleep(2) #Despues de servirlo lo que hace es regresar el plato para repetir el proceso y liberar el bloqueo
            label.place_forget()
            labeld.place(x=280, y=200)
            print("Mesero 2 regresando plato")
            label_status2.config(text="Mesero 2 regresando plato")
            time.sleep(2)
            labeld.place_forget()
        print("Mesero 2 intentando recoger platos...")
        label_status2.config(text="Mesero 2 intentando recoger platos...")
        time.sleep(2)  # Simulamos el tiempo entre recogida y entrega

# Creamos los hilos para cada mesero
thread_mesero_1 = threading.Thread(target=mesero_1)
thread_mesero_2 = threading.Thread(target=mesero_2)
#Funcion para iniciar los procesos
def iniciar():
    # Iniciamos los hilos
    thread_mesero_1.start()
    thread_mesero_2.start()
#Boton para iniciar los hilos
comenzar = Button(root, text="Iniciar Proceso", font=("Arial", 12, "bold"), padx=50, command=iniciar)
comenzar.place(x=200, y=50)
root.mainloop()