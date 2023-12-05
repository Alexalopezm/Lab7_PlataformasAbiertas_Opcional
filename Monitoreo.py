import subprocess
import sys
import time

def monitorear_proceso(nombre_proceso, comando):
    while True:
        proceso = subprocess.run(["pgrep", "-x", nombre_proceso], stdout=subprocess.DEVNULL)
        
        if proceso.returncode == 0:
            print(f"El proceso '{nombre_proceso}' está en ejecución.")
        else:
            print(f"El proceso '{nombre_proceso}' ha terminado. Reiniciando...")
            subprocess.Popen(comando, shell=True)

        time.sleep(5)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Error, ingrese el nombre del proceso y comando para ejecutar")
        print("Uso: python script.py <nombre_del_proceso> <comando_para_ejecutar>")
        sys.exit(1)
    
    nombre_proceso = sys.argv[1]
    comando_inicio = sys.argv[2]
    monitorear_proceso(nombre_proceso, comando_inicio)

