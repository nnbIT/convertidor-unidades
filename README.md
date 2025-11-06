# convertidor-unidades
Un convertidor de unidades en Python que permite cambiar dinámicamente las unidades de conversión para longitud, peso y tiempo. Desarrollado con un enfoque en logica, la validación de entradas y la interacción con el usuario mediante una interfaz de línea de comandos clara. Diseñado para destacar el pensamiento estructurado, el código limpio y la flexibilidad para futuras expansiones a nuevos sistemas de medida.

#              CONVERTIDOR DE UNIDADES - PYTHON

# 🎯 OBJETIVO PRINCIPAL
#   - Convertir entre diferentes unidades de medida.
#   - Tipos admitidos: Longitud, Peso y Tiempo.

# 🧩 OBJETIVOS SECUNDARIOS
#   - Validar la entrada del usuario y manejar datos no válidos.
#   - Permitir la modificación dinámica de unidades y tipos de conversión.
#   - Asegurar una lógica limpia y una programación estructurada.
#   - Brindar una experiencia CLI clara e interactiva.

# 🧠 DIAGRAMA LÓGICO (versión comentada del flujo)

# INICIO
#   │
#   ▼
# Mostrar la introducción del programa y las opciones de conversión
#   │
#   ▼
# Pedir al usuario el tipo de conversión:
#       1) Longitud
#       2) Peso
#       3) Tiempo
#   │
#   ▼
# Mostrar las unidades disponibles para el tipo seleccionado
#   │
#   ▼
# Pedir las unidades de origen y destino
#   │
#   ▼
# Pedir el valor numérico a convertir
#   │
#   ▼
# Realizar la conversión usando el diccionario de unidades
#   │
#   ▼
# Mostrar el resultado en un formato limpio y legible
#   │
#   ▼
# Preguntar si el usuario desea modificar algún valor (tipo, unidad o número)
#   ├──► Si sí, repetir el proceso con los datos actualizados
#   └──► Si no, mostrar mensaje de salida y finalizar el programa


# 📏 TABLAS DE UNIDADES

# 1️⃣ LONGITUD (Base: metro "m")

|  Simbolo |Descripcion   |
|:------:|:-----    |
| m | Metro         |
| km |   Kilómetro  |
| cm | Centímetro   |
| mm | Milímetro    |
| mi | Milla        |
| ft | Pie          |
| in | Pulgada      |

---

# ⚖️ PESO (Base: kilogramo "kg")

|  Simbolo |Descripcion   |
|:------:|:-----    |
| kg | Kilogramo   |
| g | Gramo    |
| mg | Miligramo        |
| lb | Libra        |
| oz | Onza      |

---

# ⏱️ TIEMPO (Base: segundo "s")

|  Simbolo |Descripcion   |
|:------:|:-----    |
| s | Segundo        |
| min | Minuto        |
| h | Hora      |



# 🛠️ DESARROLLADO CON
#   - Python 3
#   - Enfoque en programación lógica e interacción con el usuario
#   - Estructura modular para facilitar la escalabilidad

# ▶️ CÓMO EJECUTAR
#   1. Abre tu terminal.
#   2. Ejecuta el script:
#          python unit_converter.py
#   3. Sigue las instrucciones en pantalla.

# 👋 SOBRE EL PROYECTO
#   ¡Hola! Construí este Convertidor de Unidades como parte de mi proceso
#   para mejorar mi lógica de programación y el diseño enfocado en el usuario.
#   El programa combina fundamentos de Python, validación
#   e interacción mediante una interfaz CLI simple pero poderosa.
