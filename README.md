# Lab7_PlataformasAbiertas_Opcional
## Universidad de Costa Rica
### IE 0117 - Programación Bajo Plataformas Abiertas
#### Laboratorio 7: Script y Procesos en Pyhton (segundo ciclo del 2023) (Opcional)

- Alexa López Marcos, B94353

## Código `IDprocesos.py`
Este script de Python permite obtener información detallada sobre un proceso en sistemas Linux utilizando su ID.
### Uso del código `IDprocesos.py`:
Para ejecutar este script, sigue estos pasos:
1. Ejecuta el script `informacion_proceso.py` desde la línea de comandos de la siguiente manera:
    ```bash
    sudo python3 informacion_proceso.py <ID_del_proceso>
    ```

    - `<ID_del_proceso>`: ID numérico del proceso del cual deseas obtener información.

### Detalles de Implementación del código `IDprocesos.py`:
- `obtener_informacion_proceso(pid)`: Función principal que recopila información detallada sobre el proceso identificado por su ID.
- Utiliza archivos especiales en `/proc` en sistemas Linux para extraer detalles sobre el proceso, como estado, consumo de memoria, porcentaje de uso de CPU, entre otros.
- La información recuperada incluye el nombre del proceso, ID, ID del proceso padre, usuario propietario, porcentaje de uso de CPU, consumo de memoria, estado y ruta del ejecutable.
- Se requieren permisos de administrador (`sudo`) para acceder a la información detallada del proceso.

### Ejemplo de Uso del código `IDprocesos.py`:
Supongamos que queremos obtener información sobre un proceso con ID `1234`. Podemos utilizar el script de la siguiente manera:

```bash
sudo python3 informacion_proceso.py 1234
```

## Código `Monitoreo.py`
Este script monitorea constantemente un proceso y lo reinicia si finaliza, utilizando el nombre del proceso y un comando para reiniciarlo.
### Uso del código `Monitoreo.py`:
Para utilizar este script, sigue los siguientes pasos:
1. Ejecuta el script `monitor_procesos.py` desde la línea de comandos de la siguiente manera:
    ```bash
    python monitor_procesos.py <nombre_del_proceso> <comando_para_ejecutar>
    ```
    - `<nombre_del_proceso>`: Nombre del proceso que se desea monitorear.
    - `<comando_para_ejecutar>`: Comando para iniciar el proceso en caso de que finalice.

### Detalles de Implementación del código `Monitoreo.py`:
- `monitorear_proceso(nombre_proceso, comando)`: Función principal que monitorea el proceso.
- Utiliza el módulo `subprocess` para verificar si el proceso está en ejecución mediante `pgrep`.
- Si el proceso finaliza, lo reinicia ejecutando el comando proporcionado.
- Se establece un intervalo de tiempo de 5 segundos entre verificaciones.

## Código `CPU.py`
Este script de Python monitorea el consumo de CPU y memoria de un proceso específico durante un período de tiempo y genera una gráfica con los datos obtenidos.

### Uso del código `CPU.py`

Para ejecutar este script, sigue estos pasos:

1. Ejecuta el script `monitoreo_consumo.py` desde la línea de comandos de la siguiente manera:

    ```bash
    python monitoreo_consumo.py <nombre_del_ejecutable>
    ```

    - `<nombre_del_ejecutable>`: Nombre del ejecutable del proceso que deseas monitorear.

### Detalles de Implementación del código `CPU.py`:

- `proceso_en_ejecucion(nombre_proceso)`: Función que verifica si el proceso está en ejecución.
- `monitorear_proceso(ejecutable, duracion_monitoreo, archivo_log)`: Función principal que realiza el monitoreo.
- Utiliza la biblioteca `psutil` para obtener estadísticas de CPU y memoria del proceso.
- Guarda los datos recopilados en un archivo de registro (`registro_monitoreo.log`) con el formato `Tiempo CPU Memoria`.
- Genera una gráfica mostrando el consumo de CPU y memoria en función del tiempo (`ConsumoCPU.png`).

### Ejemplo de Uso del código `CPU.py`:

Supongamos que queremos monitorear el proceso llamado `mi_proceso` durante 60 segundos. Podemos usar el script de la siguiente manera:

```bash
python monitoreo_consumo.py mi_proceso
```
# Resultados
### Código `IDprocesos.py`
Al ejecutar este código en la terminal se muestran los resultados de:
- Nombre del proceso
- ID del proceso
- Parent process ID
- Usuario propietario
- Porcentaje de uso de CPU al momento de correr el script
- Consumo de memoria
- Estado (status)
- Path del ejecutable

### Código `Monitoreo.py`
Al ejecutar este código se tiene como resultado un mensaje en la terminal sobre si el proceso a monitorear se encuentra ejecutandose o si no se esta ejecutando y el código lo vuelve a abrir.

### Código `CPU.py`
Al ejecutar este código se tiene como resultado una grafica llamada "ConsumoCPU.png" se almacena en la misma carpeta en la que se ejecuta el código.
