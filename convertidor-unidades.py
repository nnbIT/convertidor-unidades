# Convertidor de Unidades
# Tipos: Longitud, Peso y Tiempo
# Unidades base:
# Longitud → metro (m)
# Peso → kilogramo (kg)
# Tiempo → segundo (s)

unidades = {
    1: {  # Longitud
        "m": 1,
        "km": 1000,
        "cm": 0.01,
        "mm": 0.001,
        "mi": 1609.34,
        "ft": 0.3048,
        "in": 0.0254
    },
    2: {  # Peso
        "kg": 1,
        "g": 0.001,
        "mg": 0.000001,
        "lb": 0.453592,
        "oz": 0.0283495
    },
    3: {  # Tiempo
        "s": 1,
        "min": 60,
        "h": 3600
    }
}

# Funciones

def conversion_unidades(tipo, valor, origen, destino):
    base = valor * unidades[tipo][origen]   # Convertir a la unidad base
    resultado = base / unidades[tipo][destino]  # Convertir a la unidad destino
    return resultado


def verificar_numero(valor):
    try:
        if "." in str(valor):
            float(valor)
        else:
            int(valor)
        return True
    except ValueError:
        return False


def verificacion_manual(tipo, origen, destino, valor):
    while True:
        verificar = input("\n¿Desea modificar algún dato? (s/n): ").lower()
        if verificar == "n":
            break
        elif verificar == "s":
            opcion = input("¿Qué desea modificar? (tipo/origen/destino/valor): ").lower()

            if opcion == "tipo":
                while True:
                    try:
                        nuevo_tipo = int(input("Ingrese el nuevo tipo (1: Longitud, 2: Peso, 3: Tiempo): "))
                        if nuevo_tipo in unidades:
                            tipo = nuevo_tipo
                            print("Unidades disponibles:", ", ".join(unidades[tipo].keys()))
                            break
                        else:
                            print("Por favor, elija una opción entre 1 y 3.")
                    except ValueError:
                        print("Debe ingresar un número válido (1, 2 o 3).")

            elif opcion == "origen":
                while True:
                    origen = input("Ingrese la nueva unidad de origen: ").lower()
                    if origen in unidades[tipo]:
                        break
                    else:
                        print("Unidad no válida. Elija entre:", ", ".join(unidades[tipo].keys()))

            elif opcion == "destino":
                while True:
                    destino = input("Ingrese la nueva unidad de destino: ").lower()
                    if destino in unidades[tipo]:
                        break
                    else:
                        print("Unidad no válida. Elija entre:", ", ".join(unidades[tipo].keys()))

            elif opcion == "valor":
                while True:
                    valor_input = input("Ingrese el nuevo valor: ")
                    if verificar_numero(valor_input):
                        valor = float(valor_input)
                        break
                    else:
                        print("Por favor, ingrese un número válido.")
            else:
                print("Opción no válida.")
        else:
            print("Por favor, responda 's' o 'n'.")
    return tipo, origen, destino, valor


## Inicio del Programa#
print("Bienvenido al convertidor de unidades de: Longitud, Peso y Tiempo" \
      "\nA continuación, seleccione el tipo de conversión deseada." \
      "\nDespués de escribir cada opción, presione ENTER para continuar.")

##Tipo de conversion
while True:
    try:
        tipo = int(input("\nSeleccione el tipo de conversión:\n1) Longitud\n2) Peso\n3) Tiempo\n→ "))
        if tipo in unidades:
            break
        else:
            print("Por favor, elija una opción entre 1 y 3.")
    except ValueError:
        print("Debe ingresar un número válido (1, 2 o 3).")
print("\nUnidades disponibles:")
for key in unidades[tipo]:
    print(f" - {key}")

##Unidad de origen
while True:
    origen = input("\nIngrese la unidad de origen: ").lower()
    if origen in unidades[tipo]:
        break
    else:
        print("Unidad no válida. Elija entre:", ", ".join(unidades[tipo].keys()))
##Unidad destino
while True:
    destino = input("Ingrese la unidad de destino: ").lower()
    if destino in unidades[tipo]:
        break
    else:
        print("Unidad no válida. Elija entre:", ", ".join(unidades[tipo].keys()))

##Valor
while True:
    valor = input(f"\nIngrese el valor en {origen}: ")
    if verificar_numero(valor):
        valor = float(valor)
        break
    else:
        print("Por favor, ingrese un número válido.")


tipo, origen, destino, valor = verificacion_manual(tipo, origen, destino, valor)


resultado = conversion_unidades(tipo, valor, origen, destino)
print(f"\n✅ {valor} {origen} equivalen a {resultado:.4f} {destino}")
