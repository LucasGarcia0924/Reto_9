import time # se importa el módulo time
# Se definen las funciones
def fibo(n : int )-> int: 
  i : int = 1
  # caso base
  n1 : int = 0
  n2 : int = 1
  while(i <= n):
    # Condicion
    sumFibo = n1 + n2
    # Actualizacion
    n1 = n2
    n2 = sumFibo
    i += 1
  return sumFibo
def fiboRecursivo(n : int )-> int:
  if n <=1:
    # caso base
    return 1
  else:
    # condicion
    return fiboRecursivo(n-1)+fiboRecursivo(n-2)  

# Se declaran e inicializan las variables
num: int = 1
diferencia_tiempos: float
serieFibo: int 
tiempo_iteracion: float
tiempo_recursion: float
diferencia_tiempos: float
start_time: float
end_time: float

if __name__ == "__main__": # Función main par indicar el inicio del código

  # Inicio del ciclo con la bandera num, y debe terminar al obtener un valor diferente a 0 en la diferencia
  while num == 1 or diferencia_tiempos == 0:
    # medicion del tiempo de ejecución de la serie de fibonacci por iteración
    start_time = time.time()
    serieFibo = fibo(num)
    end_time = time.time()
    tiempo_iteracion = end_time - start_time
      
    # medicion del tiempo de ejecución de la serie de fibonacci por recursión
    start_time = time.time()
    serieFibo = fiboRecursivo(num)
    end_time = time.time()
    tiempo_recursion = end_time - start_time
        
    diferencia_tiempos = tiempo_iteracion - tiempo_recursion # Se obtiene su diferencia
    num += 1 # Se actualiza la variable
    
  # Presentación de los resultados
  print("Para hallar una diferencia significativa en sus tiempos, la serie necesitó llegar a", str(num))
  print("El tiempo por iteración fue de", str(tiempo_iteracion), "segundos")
  print("El tiempo por recursión fue de", str(tiempo_recursion), "segundos")
  print("Y su diferencia fue de", str(diferencia_tiempos))