#import benchmarking as Ben
from benchmarking import Benchmarking
from metodos_ordenamiento import MetodosOrdenamiento

if __name__ == "__main__":
    print ("Funciona")
    bench = Benchmarking()
    metodos = MetodosOrdenamiento()
    
    tam = 1000
    arreglo = bench.buildArreglo(tam)
    
    metodos = {"burbuja": metodos.sortByBubble,
               "seleccion": metodos.sort_selection}
    
    resultados = []
    for nombre, metodo in metodos.items():
        tiempo = bench.medir_tiempo(metodo,arreglo)
        tuplaResultado = (tam,nombre,tiempo)
        resultados.append(tuplaResultado)
        
    for resultado in resultados:
        tam, nombre, tiempo = resultado
        print (f"Tamaño: {tam}, Metodo: {metodo}, Tiempo: {tiempo:.6f} segundos")