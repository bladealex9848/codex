#!/usr/bin/env python3
"""
Script para generar un gráfico de líneas con datos aleatorios de temperatura diaria durante un mes
y guardarlo como 'temperatura.png'.
"""
import random
import matplotlib.pyplot as plt

def generar_temperaturas(num_dias=30, min_temp=15.0, max_temp=30.0):
    """Genera una lista de temperaturas aleatorias entre min_temp y max_temp."""
    return [random.uniform(min_temp, max_temp) for _ in range(num_dias)]

def main():
    dias = list(range(1, 31))
    temperaturas = generar_temperaturas(len(dias))

    plt.figure(figsize=(10, 5))
    plt.plot(dias, temperaturas, marker='o', linestyle='-')
    plt.title('Temperaturas diarias durante un mes')
    plt.xlabel('Día')
    plt.ylabel('Temperatura (°C)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('temperatura.png')
    plt.close()
    print("Gráfico guardado como 'temperatura.png'.")

if __name__ == '__main__':
    main()
