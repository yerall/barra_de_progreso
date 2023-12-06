#! /usr/bin/python3

import time

def barra_de_progreso(total, longitud=40):
    try:
        for i in range(total + 1):
            time.sleep(0.05)
            porcentaje = i / total
            completado = int(porcentaje * longitud)
            restante = longitud - completado
            barra = "[{}{}] - {:.2%} completado - Tiempo restante: {}s".format('=' * completado, ' ' * restante, porcentaje, int((total - i) * 0.05))
            print(barra, end='\r', flush=True)
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario.")
