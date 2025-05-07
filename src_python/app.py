#import benchmarking as Ben
from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento
import matplotlib
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print ("Funciona")
    bench = Benchmarking()
    metodos = MetodosOrdenamiento()
    
    tamanios = [500,1000,2000]
    resultados = []

    for tam in tamanios:
        arreglo = bench.buildArreglo(tam)
    
        metodosOrd = {"burbuja": metodos.sortByBubble,
               "seleccion": metodos.sort_selection}
    
        for nombre, metodo in metodosOrd.items():
            tiempo = bench.medir_tiempo(metodo,arreglo)
            tuplaResultado = (tam,nombre,tiempo)
            resultados.append(tuplaResultado)
        
        for resultado in resultados:
            tam, nombre, tiempo = resultado
            print (f"Tamaño: {tam}, Metodo: {nombre}, Tiempo: {tiempo:.6f} segundos")
        
    tiempos_by_method = {
        "burbuja" : [],
        "seleccion" : []
    }
    
    # clasificar los tiempos según el método
    for tam, nombre, tiempo in resultados:
        tiempos_by_method[nombre].append(tiempo)
        
    #crear una gráfica
    plt.figure(figsize=(10,6))
    for nombre, tiempo in tiempos_by_method.items():
        plt.plot(tamanios, tiempo, label =nombre,marker='o')
        
    #Agregar parametros
    plt.grid()
    plt.title("Gráfico")
    plt.xlabel("Tamaño")
    plt.ylabel("Tiempo")
    plt.legend()
    plt.show()