#Realizado por Fernando Baruj Haro Salazar
from tkinter import *
from PIL import ImageTk, Image
import threading, time, random

root = Tk()
root.title('Act 11')
root.geometry("900x600")
##Se crea la imagen que representa al recurso compartido
book = Image.open("book.png")  
book = book.resize((120, 120))  
book = ImageTk.PhotoImage(book)
label_book = Label(root, image=book)
label_book.place(x=510, y=370)
######

class LectoresEscritores:
    def __init__(self, root):
        #Se inicializan los atributos
        self.root = root # Almacena una referencia al objeto Tk raiz
        self.mutex = threading.Lock() # Controla el acceso concurrente
        self.libreria = threading.Lock() #objeto lock, controla el acceso al recurso
        self.escritor_esperando = threading.Lock() #lock usado para que no entre los escritores mientras haya lectores
        self.lector_contador = 0
        self.escritor_contador = 0

        # Carga de la imagen del candado
        self.candado_imagen = Image.open("candado.png")  
        self.candado_imagen = self.candado_imagen.resize((50, 50))  
        self.candado_imagen = ImageTk.PhotoImage(self.candado_imagen)

        # Creación del label para mostrar el candado
        self.label_candado = Label(root, image=self.candado_imagen)
        self.label_candado_medio=Label(root, image=self.candado_imagen)
    

        # Etiqueta para mostrar el estado
        self.label_estado = Label(root, text="")
        self.label_estado.place(x=500, y=300)


    def mostrar_candado(self, es_lector):
        if es_lector:
            self.label_candado.place(x=300, y=20)# Coloca el candado a la izquierda
            self.label_candado_medio.place(x=450, y=370)  
        else:
            self.label_candado.place(x=800, y=20)
            self.label_candado_medio.place(x=450, y=370)  
        


    def iniciar_proceso(self):
        for _ in range(2):
            threading.Thread(target=self.lector).start()
            threading.Thread(target=self.escritor).start()

    def lector(self):
        while True:
            time.sleep(random.uniform(1, 3))  # Simula tiempo de lectura
            self.mutex.acquire()
            self.lector_contador += 1
            lector_actual = self.lector_contador  # Guardar el número del lector actual
            if self.lector_contador == 1:
                self.escritor_esperando.acquire()
            self.mutex.release()
            
            self.libreria.acquire()
            self.mostrar_candado(True)
            self.actualizar_estado(f"Lector {lector_actual}: Esperando para leer")
            print(f"Lector {lector_actual}: Acceso al cuarto de lectura concedido")
            
            self.actualizar_estado(f"Lector {lector_actual}: Acceso al cuarto de lectura concedido")
            time.sleep(random.uniform(1, 3))
            self.mutex.acquire()  # Adquirir el bloqueo para evitar que otros lectores modifiquen el contador
            self.mutex.release()
            self.libreria.release()  # Liberar el recurso compartido para que otros lectores puedan leer

            print(f"Lector {lector_actual}: Leyendo")
            self.actualizar_estado(f"Lector {lector_actual}: Leyendo")
            time.sleep(random.uniform(1, 5))
            print(f"Lector {lector_actual}: Lectura completada")
            self.actualizar_estado(f"Lector {lector_actual}: Lectura completada")
            
            self.mutex.acquire()
            self.lector_contador -= 1
            if self.lector_contador == 0:
                self.escritor_esperando.release()
                self.label_candado.place_forget()  # Si no hay más lectores, ocultar el candado
                self.label_candado_medio.place_forget()
            self.mutex.release()
            time.sleep(random.uniform(1, 5))

    def escritor(self):
        while True:
            time.sleep(random.uniform(1, 3))  # Simula tiempo de escritura
            self.escritor_esperando.acquire()  # Adquirir el bloqueo para escritores
            self.libreria.acquire()  # Adquirir el bloqueo para asegurar que no hay lectores
            self.mostrar_candado(False)
            self.actualizar_estado("Escritor: Esperando para escribir")
            print("Escritor: Esperando para escribir")
            time.sleep(random.uniform(1, 3))
            print("Escritor: Acceso al cuarto de escritura concedido")
            self.actualizar_estado("Escritor: Escribiendo")
            time.sleep(random.uniform(1, 5))
            print("Escritor: Escritura completada")
            self.actualizar_estado("Escritor: Escritura completada")
            
            self.libreria.release()  # Liberar el bloqueo después de escribir
            self.escritor_esperando.release()  # Liberar el bloqueo para escritores
            self.label_candado_medio.place_forget()
            time.sleep(random.uniform(1, 3))
                

    def actualizar_estado(self, estado):
        # Actualiza el estado en la interfaz gráfica
        self.label_estado.config(text=estado)
        self.label_estado.update()





############Creacion de imagen y sus label
        #Se crea la imagen de lector
lector1=Image.open("read.png")
lector1=lector1.resize((90,90))
lector1=ImageTk.PhotoImage(lector1)
label_lector1=Label(root,image=lector1)
label_lector1.place(x=320, y=120)
#Se crea la imagen de lector
lector2=Image.open("read.png")
lector2=lector2.resize((90,90))
lector2=ImageTk.PhotoImage(lector2)
label_lector2=Label(root,image=lector2)
label_lector2.place(x=450, y=120)
#Se crea la imagen de escritor
escritor2=Image.open("write.png")
escritor2=escritor2.resize((90,90))
escritor2=ImageTk.PhotoImage(escritor2)
label_escritor2=Label(root,image=escritor2)
label_escritor2.place(x=710, y=120)
#Se crea la imagen de escritor
escritor1=Image.open("write.png")
escritor1=escritor1.resize((90,90))
escritor1=ImageTk.PhotoImage(escritor1)
label_escritor1=Label(root,image=escritor1)
label_escritor1.place(x=580, y=120)
############Aquí se crea un objeto de la clase LectoresEscritores utilizando la instancia de la raíz de la ventana Tkinter (root). 
gestor_lectura_escritura = LectoresEscritores(root)
comenzar = Button(root, text="Iniciar Proceso", padx=50, command=gestor_lectura_escritura.iniciar_proceso)
comenzar.place(x=50, y=250)

root.mainloop()