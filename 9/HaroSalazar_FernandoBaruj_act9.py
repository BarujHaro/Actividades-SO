from tkinter import *
from tkinter import ttk
import time

root = Tk()
root.title('Act 9')
root.geometry("900x500")
####################Iniciaización de variables para contar la memoria y el numero de filas
x = 1
y=1
total_memory = 0
virtual_memory = 0
#######################################FUNCIONES
#####Funcion para cambiar de color las etiquetas que miden la cantida dde espacio disponible en las memorias
def actualizar_colores():
    global total_memory, virtual_memory
    
    # Calcular el porcentaje de ocupación de la memoria
    porcentaje_ocupacion = (total_memory / 1024) * 100
    porcentaje_ocupacionv = (virtual_memory / 1024) * 100
    
    # Actualizar el estilo de la barra de progreso
    progress_bar.configure(style=progress_bar["style"])
    
    # Cambiar el color del texto de la memoria según el porcentaje de ocupación
    if porcentaje_ocupacion < 50:
        memory_label.config(fg="green")
    elif porcentaje_ocupacion < 80:
        memory_label.config(fg="orange")
    else:
        memory_label.config(fg="red")
    
        # Cambiar el color del texto de la memoria según el porcentaje de ocupación
    if porcentaje_ocupacionv < 50:
        virtual_label.config(fg="green")
    elif porcentaje_ocupacionv < 80:
        virtual_label.config(fg="orange")
    else:
        virtual_label.config(fg="red")
#########
        
###Funcion para agregar
def agregar():
    global x, total_memory, y, virtual_memory
    #Revisa si se escribio dentro de los espacios correspondientes para la creacion de procesos
    if entrada_proceso.get() and entrada_tam.get(): 
        nombre_proceso = entrada_proceso.get()
        tam_proceso = float(entrada_tam.get())
        
        # Si el tamaño total es menor a 1024 MB, se agrega a la memoria real
        if total_memory < 1024:
            # Verificar si el tamaño excede el límite de memoria real
            if total_memory + tam_proceso <= 1024:
                 # Crear etiqueta en memoria real
                etiqueta_proceso = Label(root, text=f"{nombre_proceso}  {tam_proceso} MB")
                etiqueta_proceso.grid(row=x, column=1)
                
                # Actualizar la barra de progreso y la etiqueta de memoria real
                total_memory += tam_proceso #Se suma el tamaño del nuevo proceso al tamaño de la memoria total
                increment_percentage_real = (total_memory / 1024) * 100 #Se calcula l porcentaje de ocupacion de la memoria en relacion a su limite
                current_value_real = progress_bar["value"] #Se obtiene el valor actual de la barra de progreso, siendo el porcentaje de ocupacion
                target_value_real = increment_percentage_real # se establece un valor objetivo de la barra de progreso
                while current_value_real < target_value_real:
                    current_value_real += 1
                    progress_bar["value"] = current_value_real #Se actualiza el valor de la barra de progreso con el nuevo valor actual
                    root.update() #Se actualiza la interfaz
                    time.sleep(0.03) #Se pausa la ejecucion para crear un efecto de animación
                memory_label.config(text=f"{total_memory} MB / 1024 MB (1GB)")
                actualizar_colores()
                
                # Incrementar el índice de fila para la siguiente etiqueta en memoria real
                x += 1
            else:
                # Calcular el tamaño para memoria real y virtual
                tam_real = 1024 - total_memory
                tam_virtual = tam_proceso - tam_real
                
                # Crear etiqueta en memoria real
                etiqueta_proceso_real = Label(root, text=f"{nombre_proceso}  {tam_real} MB")
                etiqueta_proceso_real.grid(row=x, column=1)
                
                # Actualizar la barra de progreso y la etiqueta de memoria real
                total_memory = 1024
                increment_percentage_real = (total_memory / 1024) * 100
                current_value_real = progress_bar["value"]
                target_value_real = increment_percentage_real
                while current_value_real < target_value_real:
                    current_value_real += 1
                    progress_bar["value"] = current_value_real
                    root.update()
                    time.sleep(0.03)
                memory_label.config(text="1024 MB / 1024 MB (1GB)")
                actualizar_colores()
                
                # Crear etiqueta en memoria virtual
                etiqueta_proceso_virtual = Label(root, text=f"{nombre_proceso}  {tam_virtual} MB")
                etiqueta_proceso_virtual.grid(row=y, column=2)
                
                # Actualizar la barra de progreso y la etiqueta de memoria virtual
                virtual_memory += tam_virtual
                increment_percentage_virtual = (virtual_memory / 1024) * 100
                current_value_virtual = progress_barvir["value"]
                target_value_virtual = increment_percentage_virtual
                while current_value_virtual < target_value_virtual:
                    current_value_virtual += 1
                    progress_barvir["value"] = current_value_virtual
                    root.update()
                    time.sleep(0.03)
                virtual_label.config(text=f"{virtual_memory} MB / 1024 MB (1GB)")
                actualizar_colores()
                
                # Incrementar el índice de fila para la siguiente etiqueta en memoria virtual
                y += 1
        else:
         # Verificar si el tamaño del proceso excede el espacio disponible en la memoria virtual
            if tam_proceso > (1024 - virtual_memory):
                print("No espacio")
        # Mostrar un mensaje indicando que no hay suficiente espacio en la memoria virtual
        
        # O tomar otra acción adecuada, como mostrar un mensaje de error en la interfaz gráfica
            else:
                etiqueta_proceso_virtual = Label(root, text=f"{nombre_proceso}  {tam_proceso} MB")
                etiqueta_proceso_virtual.grid(row=y, column=2)
        
        # Actualizar la barra de progreso y la etiqueta de memoria virtual
                virtual_memory += tam_proceso
                increment_percentage_virtual = (virtual_memory / 1024) * 100
                current_value_virtual = progress_barvir["value"]
                target_value_virtual = increment_percentage_virtual
                while current_value_virtual < target_value_virtual:
                    current_value_virtual += 1
                    progress_barvir["value"] = current_value_virtual
                    root.update()
                    time.sleep(0.03)
                virtual_label.config(text=f"{virtual_memory} MB / 1024 MB (1GB)")
                actualizar_colores()
        
        # Incrementar el índice de fila para la siguiente etiqueta en memoria virtual
                y += 1
        
        # Limpiar los campos de entrada
        entrada_proceso.delete(0, END)
        entrada_tam.delete(0, END)
########Funcion para limpiar los espacios de memoria es decir, reiniciar todo
def limpieza():
    global x, total_memory, memory_label, y, virtual_label, virtual_memory
    
    # Eliminar el contenido de los campos de entrada
    entrada_proceso.delete(0, END)
    entrada_tam.delete(0, END)
    
    # Reiniciar el contador y el total de memoria
    x = 1
    y=1
    total_memory = 0
    virtual_memory=0
    # Eliminar todas las etiquetas de proceso, excepto "Memoria real" aqui ayudó CHATGPT
    for widget in root.grid_slaves():
        if isinstance(widget, Label) and widget.grid_info()["column"] == 1 and widget.cget("text") != "Memoria real":
            if widget != memory_label:  
                widget.grid_remove()

    for widget in root.grid_slaves():
        if isinstance(widget, Label) and widget.grid_info()["column"] == 2 and widget.cget("text") != "Memoria virtual":
            if widget != virtual_label:  
                widget.grid_remove()  
    # Reiniciar las barras de progreso
    progress_bar["value"] = 0
    progress_barvir["value"] = 0
    # Restaurar el texto y color de las etiquetas que muestran la memoria
    memory_label.config(text="0 MB / 1024 MB (1GB)", fg="green")
    virtual_label.config(text="0 MB / 1024 MB (1GB)", fg="green")

#######################################CREACIÓN DE BOTONES Y ETIQUETAS
#Se configuran las columnas para para que se expandan al tamaño de la ventana
root.columnconfigure((0, 1, 2), weight=1)
#Se crean las etiquetas
nombre_manejo = Label(root, text="Manejo procesos", font=("Arial", 14))
nombre_manejo.grid(row=0, column=0)
nombre_proceso = Label(root, text="Agregar procesos", font=("Arial", 10))
nombre_proceso.grid(row=1, column=0)
nombre_tam = Label(root, text="Agregar tamaño (MG)", font=("Arial", 10))
nombre_tam.grid(row=3, column=0)
mreal = Label(root, text="Memoria real", font=("Arial", 14))
mreal.grid(row=0, column=1)

mvirtual = Label(root, text="Memoria virtual", font=("Arial", 14))
mvirtual.grid(row=0, column=2)
#Se crean las entradas de texto para el nombre y tamaño del proceso
entrada_proceso = Entry(root, width=20)
entrada_proceso.grid(row=2, column=0)
entrada_proceso.insert(0, " ")

#
entrada_tam = Entry(root, width=20)
entrada_tam.grid(row=4, column=0)
entrada_tam.insert(0, " ")
#
memory_label = Label(root, text="0 MB / 1024 MB (1GB)", font=("Arial", 10))
memory_label.config(fg="green")
memory_label.grid(row=21, column=1)
#
#
virtual_label = Label(root, text="0 MB / 1024 MB (1GB)", font=("Arial", 10))
virtual_label.config(fg="green")
virtual_label.grid(row=21, column=2)
#Creacion de botones para agregar un proceso a la memoria o borrar los espacios en la memoria
processbutton = Button(root, text="Agregar proceso", padx=50, command=agregar)
processbutton.grid(row=5, column=0)

limpiarbutton = Button(root, text="Limpiar memoria", padx=50, command=limpieza)
limpiarbutton.grid(row=6, column=0)
#
style = ttk.Style()
style.configure("green.Horizontal.TProgressbar", foreground='green', background='green')
style.configure("orange.Horizontal.TProgressbar", foreground='orange', background='orange')
style.configure("red.Horizontal.TProgressbar", foreground='red', background='red')

progress_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_bar.grid(row=20, column=1, pady=10)
progress_barvir = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress_barvir.grid(row=20, column=2, pady=10)


root.mainloop()
