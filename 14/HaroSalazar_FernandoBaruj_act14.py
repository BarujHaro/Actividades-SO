#codigo creado por Fernando Baruj Haro Salazar
#seminario de SO
from tkinter import *
root = Tk()
root.title('Act 14 (Banquero)- Haro Salzar Fernando Baruj')
root.geometry("500x620")
######
#Se definen el número de procesos y recursos en el sistema
n_processes = 5
n_resources = 3
#Se definen las matricez que tienen la cantidad de cada recurso asignada a cada proceso
allocated = [
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]
#Matriz que representa la cantidad maxima de cada recurso que un proceso puede solicitar
max_claim = [
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
#Listas qu erepresentan la cantidad disponible de cada recurso
available = [3, 3, 2]
#available = [4, 3, 5]
#available = [1, 1, 1]

#Se definen las imagenes y sus direcciones
imagenes_procesos = {
    'A': 'a.png',
    'B': 'b.png',
    'C': 'c.png',
    'D': 'd.png',
    'E': 'e.png'
}
#Se define la clase BankerAlgorithm para aplicar el algoritmo del banquero
class BankerAlgorithm:
    def __init__(self, root, n_processes, n_resources, allocated, max_claim, available, imagenes_procesos):
        #Se definen los atributos con informacion asociada al algoritmo
        self.root = root
        self.n_processes = n_processes
        self.n_resources = n_resources
        self.allocated = allocated
        self.max_claim = max_claim
        self.available = available
        self.need = [[max_claim[i][j] - allocated[i][j] for j in range(n_resources)] for i in range(n_processes)]
        self.safe_sequence = []
        self.imagenes_procesos = imagenes_procesos

        # Etiqueta para la tabla de "allocated"
        self.label_allocated = Label(root, text="Asignado:", font=("Arial", 13, "bold"))
        self.label_allocated.place(x=310, y=190)
        self.print_table(allocated, x=315, y=220)

        # Etiqueta para la tabla de "max_claim"
        self.label_max_claim = Label(root, text="Máximo:", font=("Arial", 13, "bold"))
        self.label_max_claim.place(x=120, y=190)
        self.print_table(max_claim, x=120, y=220)

        # Etiqueta para la lista de recursos disponibles "available"
        self.label_available = Label(root, text="Disponible:", font=("Arial", 13, "bold"))
        self.label_available.place(x=200, y=115)
        self.print_list(available, x=210, y=140)

    #Función para imprimir las tablas
    def print_table(self, table_data, x, y):
        #Bucle que itera sobre cada fila de la matriz, i es el indice de la fila actual
        for i, row in enumerate(table_data):
            row_str = "  ".join(str(num) + "  " for num in row)
            label = Label(self.root, text=row_str, font=("Arial", 12))
            n=i*45
            label.place(x=x, y=y+n)
            # Agregar la imagen del proceso a la izquierda de la tabla
        for imagen_path in imagenes_procesos.values():
            imagen = PhotoImage(file=imagen_path).subsample(15)
            imagen_label = Label(root, image=imagen)
            imagen_label.image = imagen
            imagen_label.place(x=x-45,y=y)
            y+=41   
    #Funcion para imprimir en lista de manera que no se maneja como matriz o tabla
    def print_list(self, data, x, y):
        data_str = " ".join(str(num) + "  " for num in data)
        label = Label(self.root, text=data_str, font=("Arial", 12))
        label.place(x=x, y=y)
    #Metodo que toma tres argumentos, itera sobre cada recurso en el sistema utilizando un bucle for
    def is_safe(self, process, work, finish):
        for i in range(self.n_resources):
            #Comprueba si la necesidad del proceso para el recurso i, es mayor a la cantidad actual de ese recurso disponible y regresa false si no se encuentra
            if self.need[process][i] > work[i]:
                return False
        return True
    
    # Función para procesar el resultado
    def procesar(self, resultado):
        # Mostramos la secuencia segura o la advertencia según el resultado
        if resultado:
            pos_x=120
            # Si todos los procesos están en un estado seguro, se muestra un mensaje de estado seguro
            self.label_safe = Label(root, text="Estado seguro", font=("Arial", 13, "bold"))
            self.label_safe.place(x=180, y=465)
            self.label_safe = Label(root, text="Secuencia:", font=("Arial", 13, "bold"))
            self.label_safe.place(x=200, y=495)
            #Se colocan las imágenes
            for proceso in self.safe_sequence:
                imagenes_path = imagenes_procesos.values()
                imagenes_path = list(imagenes_path)
                imagen_path=imagenes_path[proceso]
                imagen = PhotoImage(file=imagen_path).subsample(15)
                label = Label(root, image=imagen)
                label.image = imagen   
                label.place(x=pos_x, y=530) 
                pos_x+=50
        else:
                #Impresion de etiqueta de error
                self.label_safe = Label(root, text="ERROR estado no seguro", font=("Arial", 13, "bold"))
                self.label_safe.place(x=140, y=465)
                #Imagen de error
                error_imagen = PhotoImage(file='warning.png').subsample(10, 10)
                error_label = Label(root, image=error_imagen)
                error_label.image = error_imagen
                error_label.place(x=220, y=500)
    
#Funcion del algoritmo
    def execute_algorithm(self):
        #Se inicializan variables
        work = self.available.copy()#Copia de la lista de recursos disponibles
        finish = [False] * self.n_processes #Lista para rastreas si cada proceso ha finalizado
        count = 0 #Contador de procesos seguros
        #Se ejecuta un bucle hasta que todos los procesos esten en un estados eguro
        while count < self.n_processes:
            found = False #Bandera si se encuentra un proceso en seguro en esta iteracion
            #Se itera sobre todos los procesos para encontrar uno seguro
            for i in range(self.n_processes):
                ## Se verifica si el proceso i no ha finalizado y si es seguro asignarle recursos
                if not finish[i] and self.is_safe(i, work, finish):
                    #Se asigna recursos al proceso 1
                    for j in range(self.n_resources):
                        work[j] += self.allocated[i][j]
                        #Se registra el proceso como seguro
                    self.safe_sequence.append(i)
                    finish[i] = True
                    count += 1
                    found = True
                    break #Se sale del bucle for si se ecnontró un proceso seguro
                #SI no se encontró ningun proceso en esta iteración,  se muestra un error
            if not found:
                #Se retorna false para indicar un estado no seguro
                print("ERROR estado no seguro")
                return False
        #Se retorna True como estado seguro para continuar con la impresion de la secuencia
        print("Estado seguro:", self.safe_sequence)
        return True
    
    #
    
    
#funcion para iniciar el algoritmo
banker = BankerAlgorithm(root, n_processes, n_resources, allocated, max_claim, available, imagenes_procesos)
resultado=banker.execute_algorithm()
def iniciar():
    banker.procesar(resultado)

comenzar = Button(root, text="Iniciar Proceso", font=("Arial", 12, "bold"), padx=50, command=iniciar)
comenzar.place(x=130, y=50)
root.mainloop()