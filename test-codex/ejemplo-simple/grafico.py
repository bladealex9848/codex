#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script que genera un gráfico de barras con datos aleatorios y lo guarda como 'grafico.png'
"""
import matplotlib.pyplot as plt
import numpy as np

# Generar datos aleatorios
categorias = ['A', 'B', 'C', 'D', 'E']
valores = np.random.randint(1, 100, size=len(categorias))

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(categorias, valores, color='skyblue')
plt.title('Gráfico de Barras con Datos Aleatorios')
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Añadir valores encima de las barras
for i, v in enumerate(valores):
    plt.text(i, v + 2, str(v), ha='center')

# Guardar el gráfico
plt.savefig('grafico.png')
print("Gráfico guardado como 'grafico.png'")

# Mostrar el gráfico (opcional)
# plt.show()
