# Lab7_PlataformasAbiertas_Opcional
## Universidad de Costa Rica
### IE 0117 - Programación Bajo Plataformas Abiertas
#### Laboratorio 7: Script y Procesos en Pyhton (segundo ciclo del 2023)

- Alexa López Marcos, B94353

# Código `IDprocesos.py`


# Código `Monitoreo.py`
Este script monitorea constantemente un proceso y lo reinicia si finaliza, utilizando el nombre del proceso y un comando para reiniciarlo.
## Uso
Para utilizar este script, sigue los siguientes pasos:
1. Ejecuta el script `monitor_procesos.py` desde la línea de comandos de la siguiente manera:
    ```bash
    python monitor_procesos.py <nombre_del_proceso> <comando_para_ejecutar>
    ```
    - `<nombre_del_proceso>`: Nombre del proceso que se desea monitorear.
    - `<comando_para_ejecutar>`: Comando para iniciar el proceso en caso de que finalice.

## Detalles de Implementación:
- `monitorear_proceso(nombre_proceso, comando)`: Función principal que monitorea el proceso.
- Utiliza el módulo `subprocess` para verificar si el proceso está en ejecución mediante `pgrep`.
- Si el proceso finaliza, lo reinicia ejecutando el comando proporcionado.
- Se establece un intervalo de tiempo de 5 segundos entre verificaciones.

# Código `CPU.py`


