# Importamos librerías
import pandas as pd                    # pandas: para cálculos rápidos y manejo de datos (pd: alias de pandas)
import matplotlib.pyplot as plt        # matplotlib: para hacer gráficos (plt: pyplot)

# Creamos una lista de calificaciones (datos de ejemplo)
calificaciones = [7.5, 8.0, 6.5, 9.0, 8.5, 7.0, 9.5, 8.0, 6.0, 7.5] # aquí ya no se utilizo un archivo csv

# Convertimos la lista en una Serie de pandas
serie = pd.Series(calificaciones)# "pd.Series": aquí tenemos una clase de la libreria de Pandas 
#serie es una variable
#pd.Series, es una lista que te permite hacer calculos rapidamente, coloca indices, y tiene varias funciones como
#mean(), max(), min()
# entonces en este linea tenemos una variables que contiene una clase que como parametro tiene la lista de calificaciones esto nos permite manipular mejor los datos 

# Calculamos estadísticas básicas
promedio = serie.mean()      # promedio de la lista
maximo = serie.max()         # valor máximo
minimo = serie.min()         # valor mínimo

# Mostramos resultados en consola
print(f"Promedio: {promedio}") # promedio de la lista
print(f"Calificación más alta: {maximo}")  # valor máximo
print(f"Calificación más baja: {minimo}") # valor mínimo 

# Creamos una gráfica de línea
plt.figure(figsize=(8,4))   # tamaño del gráfico
plt.plot(serie, marker='o', linestyle='-', color='teal')  # línea con puntos
plt.title('Calificaciones de los alumnos') # el titulo de la grafica
plt.xlabel('Alumno')        # eje X va a ser de los alumnos 
plt.ylabel('Calificación')  # eje Y va a ser de calificaiones 
plt.grid(True)              # ponemos rejilla para que se vea mejor
plt.show()                  # mostramos el gráfico
