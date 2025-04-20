#!/usr/bin/env python3
"""
Script para generar un gráfico de barras con datos aleatorios de ventas mensuales
y guardar la imagen como 'ventas.png'.
"""

import random
import matplotlib.pyplot as plt

def generar_datos_ventas():
    """
    Genera una lista de ventas mensuales aleatorias.
    Retorna:
        meses (list of str): Nombres de los meses.
        ventas (list of int): Valores de ventas para cada mes.
    """
    meses = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]
    # Ventas aleatorias entre 1000 y 5000 unidades monetarias
    ventas = [random.randint(1000, 5000) for _ in meses]
    return meses, ventas

def crear_grafico_barras(meses, ventas, archivo_salida='ventas.png'):
    """
    Crea y guarda un gráfico de barras de ventas mensuales.
    Args:
        meses (list of str): Nombres de los meses.
        ventas (list of int): Valores de ventas para cada mes.
        archivo_salida (str): Nombre del archivo de imagen de salida.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(meses, ventas, color='skyblue')
    plt.title('Ventas Mensuales')
    plt.xlabel('Mes')
    plt.ylabel('Ventas')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(archivo_salida)
    plt.close()
    print(f"Gráfico guardado en '{archivo_salida}'")

def main():
    meses, ventas = generar_datos_ventas()
    crear_grafico_barras(meses, ventas)

if __name__ == '__main__':
    main()
