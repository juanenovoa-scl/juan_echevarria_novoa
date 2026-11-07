# Juan Echevarria
# Tarea semana 3 - Renombrar archivos LOG
# Script para renombrar archivos LOG en una carpeta específica

import os
import re

# Solicitar los datos para formar el nuevo nombre
nombre = input("Ingrese el nombre: ").strip().replace(" ", "_")
apellido = input("Ingrese el apellido: ").strip().replace(" ", "_")
prefijo = f"{nombre}_{apellido}"

# Solicitar la carpeta que contiene los archivos LOG
carpeta = input("Ingrese la ruta de la carpeta con los archivos LOG: ").strip().strip('"')

if not nombre or not apellido:
    print("Error: debe ingresar nombre y apellido.")

elif not os.path.isdir(carpeta):
    print("Error: la carpeta indicada no existe.")

else:
    # Identificar los archivos que ya tienen el formato generado
    patron_generado = re.compile(
        rf"^{re.escape(prefijo)}_\d+\.log$",
        re.IGNORECASE
    )

    archivos_log = []

    # Buscar solamente archivos con extensión .log
    for archivo in os.listdir(carpeta):
        ruta_origen = os.path.join(carpeta, archivo)

        if (
            os.path.isfile(ruta_origen)
            and os.path.splitext(archivo)[1].lower() == ".log"
            and not patron_generado.fullmatch(archivo)
        ):
            archivos_log.append(archivo)

    # Ordenar los archivos antes de renombrarlos
    archivos_log.sort()

    if not archivos_log:
        print("No se encontraron archivos LOG para renombrar.")

    else:
        numero = 1

        for archivo in archivos_log:
            ruta_origen = os.path.join(carpeta, archivo)

            # Evitar sobrescribir archivos existentes
            while True:
                nuevo_nombre = f"{prefijo}_{numero:02d}.log"
                ruta_destino = os.path.join(carpeta, nuevo_nombre)

                if not os.path.exists(ruta_destino):
                    break

                numero += 1

            # Cambiar el nombre del archivo
            os.rename(ruta_origen, ruta_destino)

            print(f"{archivo} -> {nuevo_nombre}")
            numero += 1

        print(
            f"\nProceso terminado. "
            f"Archivos renombrados: {len(archivos_log)}"
        )
