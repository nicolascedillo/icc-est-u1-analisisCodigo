import random 
import time
from metodos_ordenamiento import MetodosOrdenamiento

class Benchmarking:
    
    def __init__(self):
        print('Bench inicializado')
        
    def ejemplo(self):
        self.mOrdenamiento = MetodosOrdenamiento()
        arreglo = self.buildArreglo(1000)
        tarea = lambda: self.mOrdenamiento.sortByBubble(arreglo)
        tiempoMillis = self.contar_con_current_time_milles(tarea)
        tiempoNano = self.contar_con_nano_time(tarea)
        print (f'Tiempo en mili {tiempoMillis}')
        print(f'Tiempo en nano {tiempoNano}')
        
        
    def buildArreglo(self, tam):
        array = []
        for i in range (tam):
            numero = random.randint(0,9999)
            array.append(numero)
        return array
    
    def contar_con_current_time_milles(self, tarea):
        x = time.time()
        tarea()
        y =time.time()
        return (y-x)
    
    def contar_con_nano_time(self,tarea):
        x =time.time_ns()
        tarea()
        y = time.time_ns()
        return(y-x)/1000000000.0
    
    def medir_tiempo(self,tarea,array):
        inicio = time.perf_counter()
        tarea(array)
        fin=time.perf_counter()
        return fin-inicio
    
 