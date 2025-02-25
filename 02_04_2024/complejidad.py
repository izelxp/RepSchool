
import time
import tracemalloc

def medir_tiempo(funcion, argumentos):
    # Pregunta la hora
   ## t_inicial = time.time()##UTC (relog)
    t_inicial=time.perf_counter()
    #Algoritmo que se va a medir
    funcion(argumentos)
    #Pregunta la hora
    ##t_final =time.time()##UTC(relog)
    t_final=time.perf_counter()
    #Imprime tiempo transcurido
    print(f'Tiempo:{t_final-t_inicial:.10f} (segundos)')

def medir_memoria(funcion, argumentos):
    #Iniciar el seguimienti de memoria
    tracemalloc.start()
    #Algoritmo que se va a medir
    funcion(argumentos)
    #Captura del seguimiento de memoria
    current, peak = tracemalloc.get_traced_memory()
    #Terminar el seguimiento de memoria
    tracemalloc.stop()
    #Imprime los resultados del seguimiento
    print(f'Memoria actual : {current/1024:.2} KB, Memoria pico: {peak/1024:.2} KB')

    #*********************
    #multiples argumentos
def medir_memoria_1(funcion, *argumentos):
    #Iniciar el seguimienti de memoria
    tracemalloc.start()
    #Algoritmo que se va a medir
    funcion(*argumentos)
    #Captura del seguimiento de memoria
    current, peak = tracemalloc.get_traced_memory()
    #Terminar el seguimiento de memoria
    tracemalloc.stop()
    #Imprime los resultados del seguimiento
    print(f'Memoria actual : {current/1024:.2} KB, Memoria pico: {peak/1024:.2} KB')
