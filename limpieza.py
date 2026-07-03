import os
import shutil

# Obtener rutas temporales
temp_usuario = os.environ.get("TEMP")

# Ruta temporal del sistema
temp_sistema = os.path.join(os.environ.get("SystemRoot", "C:\\Windows"), "Temp")

print(f"Ruta temporal de usuario localizada: {temp_usuario}")
print(f"Ruta temporal del sistema localizada: {temp_sistema}")

# Lista de rutas a procesar
RUTAS_TEMP = [temp_usuario, temp_sistema]


def escanear_carpetas(lista_rutas):
    """Muestra el contenido de las carpetas temporales."""

    for ruta in lista_rutas:
        if not ruta:
            continue

        if os.path.exists(ruta):
            print(f"\n=== Analizando el contenido de: {ruta} ===")

            try:
                elementos = os.listdir(ruta)

                if not elementos:
                    print("Carpeta vacía.")
                    continue

                for elemento in elementos:
                    ruta_completa = os.path.join(ruta, elemento)
                    print(f"Elemento detectado listo para procesar: {ruta_completa}")

            except Exception as e:
                print(f"Error al analizar {ruta}: {e}")


def limpiar_temporales(lista_rutas):
    """Elimina archivos y carpetas temporales."""

    for ruta in lista_rutas:
        if not ruta or not os.path.exists(ruta):
            continue

        print(f"\n[!] Iniciando purga en: {ruta}")

        try:
            elementos = os.listdir(ruta)

            for elemento in elementos:
                ruta_completa = os.path.join(ruta, elemento)

                try:
                    if os.path.isfile(ruta_completa) or os.path.islink(ruta_completa):
                        os.unlink(ruta_completa)
                        print(f"Borrado: {elemento}")

                    elif os.path.isdir(ruta_completa):
                        shutil.rmtree(ruta_completa)
                        print(f"Directorio purgado: {elemento}")

                except PermissionError:
                    print(f"Recurso en uso exclusivo: {elemento} (Omitido)")

                except Exception as e:
                    print(f"Error crítico inesperado en {elemento}: {e}")

        except Exception as e:
            print(f"No se pudo acceder a {ruta}: {e}")


# ==========================
# EJECUCIÓN DEL PROGRAMA
# ==========================

print("\nEscaneando carpetas temporales...")
escanear_carpetas(RUTAS_TEMP)

respuesta = input("\n¿Deseas limpiar los archivos temporales? (s/n): ").lower()

if respuesta == "s":
    print("\nIniciando limpieza...")
    limpiar_temporales(RUTAS_TEMP)
    print("\n✅ Proceso finalizado.")
else:
    print("\n❌ Limpieza cancelada.")

_ = input("\nPulsa ENTER para salir...")
