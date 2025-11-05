# convertidor-unidades
Un convertidor de unidades en Python que permite cambiar dinámicamente las unidades de conversión para longitud, peso y tiempo. Desarrollado con un enfoque en logica, la validación de entradas y la interacción con el usuario mediante una interfaz de línea de comandos clara. Diseñado para destacar el pensamiento estructurado, el código limpio y la flexibilidad para futuras expansiones a nuevos sistemas de medida.


# ╔══════════════════════════════════════════════════╗
# ║              UNIT CONVERTER - PYTHON             ║
# ╚══════════════════════════════════════════════════╝

# 🎯 MAIN OBJECTIVE
#   - Convert between different units of measurement.
#   - Supported types: Length, Weight, and Time.

# 🧩 SECONDARY OBJECTIVES
#   - Validate user input and handle invalid data.
#   - Allow dynamic modification of units and conversion types.
#   - Ensure clean logic and structured programming.
#   - Provide a clear, interactive CLI experience.

# 🧠 LOGIC DIAGRAM (commented version of the flow)

# START
#   │
#   ▼
# Display program introduction and conversion options
#   │
#   ▼
# Ask the user for the conversion type:
#       1) Length
#       2) Weight
#       3) Time
#   │
#   ▼
# Show available units for the selected type
#   │
#   ▼
# Ask for the origin and destination units
#   │
#   ▼
# Ask for the numeric value to convert
#   │
#   ▼
# Perform the conversion using the dictionary of units
#   │
#   ▼
# Display the result in a clean, readable format
#   │
#   ▼
# Ask if the user wants to modify any value (type, unit, or number)
#   ├──► If yes, repeat the process with updated data
#   └──► If no, display exit message and finish the program


# 📏 UNIT TABLES

# 1️⃣ LENGTH (Base: meter "m")
# ┌─────────┬──────────────┐
# │ Symbol  │ Description  │
# ├─────────┼──────────────┤
# │ m       │ Meter        │
# │ km      │ Kilometer    │
# │ cm      │ Centimeter   │
# │ mm      │ Millimeter   │
# │ mi      │ Mile         │
# │ ft      │ Foot         │
# │ in      │ Inch         │
# └─────────┴──────────────┘

# ⚖️ WEIGHT (Base: kilogram "kg")
# ┌─────────┬──────────────┐
# │ Symbol  │ Description  │
# ├─────────┼──────────────┤
# │ kg      │ Kilogram     │
# │ g       │ Gram         │
# │ mg      │ Milligram    │
# │ lb      │ Pound        │
# │ oz      │ Ounce        │
# └─────────┴──────────────┘

# ⏱️ TIME (Base: second "s")
# ┌─────────┬──────────────┐
# │ Symbol  │ Description  │
# ├─────────┼──────────────┤
# │ s       │ Second       │
# │ min     │ Minute       │
# │ h       │ Hour         │
# └─────────┴──────────────┘


# 🛠️ BUILT WITH
#   - Python 3
#   - Focus on logical programming and user interaction
#   - Modular structure for easy scalability

# ▶️ HOW TO RUN
#   1. Open your terminal.
#   2. Run the script:
#          python unit_converter.py
#   3. Follow the on-screen instructions.

# 👋 ABOUT THE PROJECT
#   Hi! I built this Unit Converter as part of my journey
#   to improve my programming logic and user-focused design.
#   The program combines Python fundamentals, validation,
#   and interaction through a simple but powerful CLI.
