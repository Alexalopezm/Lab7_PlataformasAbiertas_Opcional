import os
import sys
import time
import psutil
import matplotlib.pyplot as plt

def proceso_en_ejecucion(nombre_proceso):
    for proceso in psutil.process_iter(['pid', 'name']):
        if proceso.info['name'] == nombre_proceso:
            return True
    return False

def monitorear_proceso(ejecutable, duracion_monitoreo, archivo_log):
    tiempo_inicio = time.time()

    # Archivar los datos
    with open(archivo_log, 'a') as archivo:
        archivo.write("Tiempo CPU Memoria\n")

    while proceso_en_ejecucion(ejecutable):
        tiempo_actual = time.time()
        tiempo_transcurrido = tiempo_actual - tiempo_inicio
        
        # Obtener el PID del proceso y sus estadísticas de CPU y memoria
        if tiempo_transcurrido <= duracion_monitoreo:
            pid_proceso = int(os.popen(f"pgrep -o {ejecutable}").read().strip())
            proceso = psutil.Process(pid_proceso)
            uso_cpu = proceso.cpu_percent(interval=1)
            uso_memoria = proceso.memory_percent()
            
            # Guardar las estadísticas en el archivo de registro
            with open(archivo_log, 'a') as archivo:
                archivo.write(f"{tiempo_transcurrido} {uso_cpu} {uso_memoria}\n")

        else:
            break

    # Generar la gráfica
    datos = {'Tiempo': [], 'CPU': [], 'Memoria': []}
    with open(archivo_log, 'r') as archivo:
        next(archivo)  # Saltar la primera línea (encabezado)
        for linea in archivo:
            tiempo, cpu, memoria = map(float, linea.split())
            datos['Tiempo'].append(tiempo)
            datos['CPU'].append(cpu)
            datos['Memoria'].append(memoria)
    
    # Crear la gráfica de consumo de CPU y memoria
    if datos['Tiempo']:
        plt.plot(datos['Tiempo'], datos['CPU'], label='CPU')
        plt.plot(datos['Tiempo'], datos['Memoria'], label='Memoria')
        plt.title(f'Consumo de CPU y Memoria de {ejecutable}')
        plt.xlabel('Tiempo (segundos)')
        plt.ylabel('Porcentaje')
        plt.legend()
        plt.savefig('ConsumoCPU.png')
        plt.close()

        print("El monitoreo ha finalizado. Ver gráfico en 'ConsumoCPU.png'.")
    else:
        print("No se registraron datos para generar la gráfica.")

if __name__ == "__main__":
    # Comprobar que el nombre del ejecutable se proporcione como argumento
    if len(sys.argv) != 2:
        print("Uso: python script.py <nombre_del_ejecutable>")
        sys.exit(1)

    ejecutable = sys.argv[1]
    duracion_monitoreo = 60  # Duración del monitoreo
    archivo_log = "registro_monitoreo.log"

    monitorear_proceso(ejecutable, duracion_monitoreo, archivo_log)
