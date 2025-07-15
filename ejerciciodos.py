# Importamos librerías
import pandas as pd                    # pandas: para cálculos rápidos y manejo de datos
import matplotlib.pyplot as plt        # matplotlib: para hacer gráficos

# Creamos una lista de calificaciones (datos de ejemplo)
calificaciones = [7.5, 8.0, 6.5, 9.0, 8.5, 7.0, 9.5, 8.0, 6.0, 7.5]

# Convertimos la lista en una Serie de pandas
serie = pd.Series(calificaciones)

# Calculamos estadísticas básicas
promedio = serie.mean()      # promedio de la lista
maximo = serie.max()         # valor máximo
minimo = serie.min()         # valor mínimo

# Mostramos resultados en consola
print(f"Promedio: {promedio}")
print(f"Calificación más alta: {maximo}")
print(f"Calificación más baja: {minimo}")

# Creamos una gráfica de línea
plt.figure(figsize=(8,4))   # tamaño del gráfico
plt.plot(serie, marker='o', linestyle='-', color='teal')  # línea con puntos
plt.title('Calificaciones de los alumnos')
plt.xlabel('Alumno')
plt.ylabel('Calificación')
plt.grid(True)              # ponemos rejilla para que se vea mejor
plt.show()                  # mostramos el gráfico
