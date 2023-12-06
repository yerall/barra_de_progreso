# Barra de carga simple para la mejora de espacios entre procesos

Este script de Python proporciona una función simple para visualizar una barra de progreso en la línea de comandos. La barra de progreso se actualiza en tiempo real para representar el progreso de una tarea específica.

### Uso
1. Asegúrate de tener Python 3 instalado.
2. Puedes incorporar la función `barra_de_progreso` en tu propio código de preferencia en otro archivo de tu programa principal o ejecutar el script directamente para ver un ejemplo.

```python
# Ejemplo de uso
from barra_de_progreso import barra_de_progreso

# Especifica el total de la tarea
total_tarea = 100

# Llama a la función de la barra de progreso
barra_de_progreso(total_tarea)
```

### Características

- **Personalización**: Puedes ajustar la longitud de la barra y la velocidad de actualización.
- **Información adicional**: La barra de progreso incluye el porcentaje completado y el tiempo estimado restante.
- **Interrupción grácil**: Puedes interrumpir el proceso de manera grácil usando `Ctrl+C`.

### Parámetros de la Función

- `total`: La cantidad total de unidades que representan el progreso completo.

- `longitud` (opcional): La longitud total de la barra de progreso (por defecto es 40).

### Ejemplo de Salida

```python
[=======            ] - 50.00% completado - Tiempo restante: 2s
```
