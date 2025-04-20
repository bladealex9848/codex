#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Este script muestra la fecha y hora actual, además de un saludo personalizado para Alexander.
"""
import datetime

def main():
    ahora = datetime.datetime.now()
    fecha = ahora.strftime("%d/%m/%Y")
    hora = ahora.strftime("%H:%M:%S")
    print(f"Fecha actual: {fecha}")
    print(f"Hora actual: {hora}")
    print("¡Hola Alexander!")

if __name__ == "__main__":
    main()