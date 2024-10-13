#Realizado por Fernando Baruj Haro Salazar 
from tkinter import *
from PIL import ImageTk, Image
import threading, time, random
#Se define la clase filosofo
class Filosofo(threading.Thread):
    #Se inicializan con nombre y dos semaforos para cada tenedor, dos imagenes y un label para mostrar la imagen
    def __init__(self, nombre, tenedor_izq, tenedor_der, imagen_comiendo, imagen_pensando, label):
        super().__init__()
        self.nombre = nombre
        self.tenedor_izq = tenedor_izq
        self.tenedor_der = tenedor_der
        self.imagen_comiendo = imagen_comiendo
        self.imagen_pensando = imagen_pensando
        self.imagen_actual = imagen_pensando
        self.label = label

#se ejecuta como un bucle infinito para alternar entre comer y pensar
    def run(self):
        while True:
            self.pensar()
            self.comer()

#Simula el estado pensar, actualiza la imagen y espera de 1 a 3 segundos
    def pensar(self):
        print(f"{self.nombre} está pensando.")
        self.actualizar_imagen(self.imagen_pensando)
        time.sleep(random.uniform(1, 3))

#simula la accion de comer, adquiriendo los semaforos de los tenedores, se agarran de izq a der, además de esperar de 1 a 3 segundos para soltarlos
    def comer(self):
        self.tenedor_izq.acquire()
        self.tenedor_der.acquire()
        print(f"{self.nombre} está comiendo.")
        self.actualizar_imagen(self.imagen_comiendo)
        time.sleep(random.uniform(1, 3))
        print(f"{self.nombre} ha terminado de comer.")
        self.tenedor_izq.release()
        self.tenedor_der.release()

#actualiza la imagen 
    def actualizar_imagen(self, imagen):
        self.imagen_actual = imagen
        self.label.config(image=self.imagen_actual)
        self.label.update()

root = Tk()
root.title('Act 10')
root.geometry("900x600")
filosofos_numero = 5


def iniciar_cena():
    # Tamaño para las imágenes de los filósofos
    tamano_deseado = (100, 100)
    
    # Cargar y redimensionar las imágenes de los filósofos
    imagen_comiendo_orig = Image.open('comiendo.png')
    imagen_pensando_orig = Image.open('pensando.png')
    imagen_comiendo = imagen_comiendo_orig.resize(tamano_deseado)
    imagen_pensando = imagen_pensando_orig.resize(tamano_deseado)
    
    # Convertir las imágenes redimensionadas a formato PhotoImage
    imagen_comiendo_tk = ImageTk.PhotoImage(imagen_comiendo)
    imagen_pensando_tk = ImageTk.PhotoImage(imagen_pensando)

    # Definir manualmente las posiciones de las etiquetas de los filósofos
    posiciones_filosofos = [
        (300, 200),  
        (500, 70),  
        (700, 200), 
        (600, 350),  
        (400, 350), 
    ]
#Crea lista de objetos semaforo, utilizada para controlar el acceso y se inicializa con 1 
    tenedores = [threading.Semaphore(1) for _ in range(filosofos_numero)]
    #Se crean las imagenes
    imagenes_comiendo = [imagen_comiendo_tk for _ in range(filosofos_numero)]
    imagenes_pensando = [imagen_pensando_tk for _ in range(filosofos_numero)]
    filosofos = []

    for i in range(filosofos_numero):
        tenedor_izq = tenedores[i]
        tenedor_der = tenedores[(i + 1) % filosofos_numero]
        
        # Crear una etiqueta para mostrar la imagen del filósofo
        label_filosofo = Label(root, image=imagenes_pensando[i], width=tamano_deseado[0], height=tamano_deseado[1])
        label_filosofo.place(x=posiciones_filosofos[i][0], y=posiciones_filosofos[i][1])
        
        # Crear un objeto Filosofo y pasarlo a la lista de filósofos
        filosofo = Filosofo(f"Filosofo {i+1}", tenedor_izq, tenedor_der, imagenes_comiendo[i], imagenes_pensando[i], label_filosofo)
        filosofos.append(filosofo)

    for filosofo in filosofos:
        filosofo.start()


####Creación de la imagen de la mesa
cena = Image.open("cena.png")  
cena = cena.resize((320, 220))  
cena = ImageTk.PhotoImage(cena)
label_cena = Label(root, image=cena)
label_cena.place(x=400, y=150)
####Boton para comenzar los procesos
comenzar = Button(root, text="Iniciar cena", padx=50, command=iniciar_cena)
comenzar.place(x=50, y=250)  

root.mainloop()
