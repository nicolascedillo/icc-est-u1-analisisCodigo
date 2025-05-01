class MetodosOrdenamiento:
    def sortByBubble(self, arreglo):
        arreglo = arreglo.copy()
        n = len(arreglo)
        for i in range (n):
            for j in range (i+1,n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
        return arreglo
                    
    def sort_selection(self,array):
        array = array.copy()
        for i in range (len(array)-1):
            ind = i
            for j in range (i+1,len(array)):
                if array[ind]>array[j]:
                    ind = j
            if ind != i:
                array[ind],array[j] = array[j],array[ind]
        return array        
        
               