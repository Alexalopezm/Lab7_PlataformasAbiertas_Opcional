import os
import sys

def obtener_informacion_proceso(pid):
    try:
        # Obtener información del proceso
        stat = {}
        with open(f"/proc/{pid}/status", 'r') as file:
            for line in file:
                if ':' in line:
                    key, value = line.split(':', 1)
                    stat[key.strip()] = value.strip()

        # Obtener información adicional
        with open(f"/proc/{pid}/stat", 'r') as file:
            stat_info = file.read().split()
            stat['Estado'] = stat_info[2]
            stat['Usuario propietario'] = stat_info[0]
            stat['Consumo de memoria'] = int(stat_info[23]) * os.sysconf(os.sysconf_names['SC_PAGE_SIZE'])

        # Nombre del proceso y path del ejecutable
        stat['Nombre del proceso'] = stat['Name']
        stat['Path del ejecutable'] = os.readlink(f"/proc/{pid}/exe")

        # Obtener porcentaje de uso de CPU
        with open(f"/proc/{pid}/stat", 'r') as file:
            for line in file:
                fields = line.split()
                total_time = float(fields[13]) + float(fields[14]) + float(fields[15]) + float(fields[16])
                seconds = os.sysconf(os.sysconf_names['SC_CLK_TCK'])
                cpu_usage = ((total_time / seconds) / os.cpu_count())
                stat['Porcentaje de uso de CPU'] = round(cpu_usage, 2)

        print("Información del proceso:")
        print(f"Nombre del proceso: {stat['Nombre del proceso']}")
        print(f"ID del proceso: {pid}")
        print(f"Parent process ID: {stat['PPid']}")
        print(f"Usuario propietario: {stat['Usuario propietario']}")
        print(f"Porcentaje de uso de CPU: {stat['Porcentaje de uso de CPU']}%")
        print(f"Consumo de memoria: {stat['Consumo de memoria']} bytes")
        print(f"Estado: {stat['Estado']}")
        print(f"Path del ejecutable: {stat['Path del ejecutable']}")

    except FileNotFoundError:
        print(f"No se encontró un proceso con el ID {pid}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: sudo python3 IDprocesos.py <ID_del_proceso>")
    else:
        proceso_id = int(sys.argv[1])
        obtener_informacion_proceso(proceso_id)
