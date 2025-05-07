import matplotlib
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

nombre_linea = "linea 1"
plt.plot(x,y,label=nombre_linea,color="blue" )
plt.title("Primer gráfico")
plt.xlabel("Datos de eje x")
plt.ylabel("Datos de eje y")
plt.legend()
plt.show()