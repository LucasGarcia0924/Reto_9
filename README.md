# Reto_9
***
Evidencia de la solución de las actividades propuestas en el reto #9
## Ejercicios de la clase
  ### N°1
  Cree una función que permita calcular el Máximo Comun Divisor de dos números dados (a y b).
```
def max_com_divi_recursivo(a : int ,b : int, n : int = 2)-> int: # Se especifican los datos que entran y salen
  divisor: int = 1 # Se declara e inicializa la variable
  # condicion
  if  n > a or n > b:
    return 1 # caso base
  elif a%n == 0 and b%n == 0:
    divisor = n
    return divisor*max_com_divi_recursivo(a/n,b/n,n) # caso donde si es divisor
  else:
    divisor = 1
    return divisor*max_com_divi_recursivo(a,b,n+1) # caso donde no es divisor
  
if __name__ == "__main__": # Función main par indicar el inicio del código
  # Se declaran e inicializan las variables
  a = int(input("Ingrese un numero: "))
  b = int(input("Ingrese otro numero: "))
  if a in [0,1] or b in [0,1]:
    # caso base donde a o b (o ambos), son iguales a 0 o a 1
    mcd = 1
    print(f"Su máximo común divisor es {mcd}")
  else: # Caso para cualquier otro número
    mcd = max_com_divi_recursivo(a,b)
    print(f"El máximo común divisor de {a} y {b} es {mcd}")
```
  ### N°2
  Cree una función anónima que calcule: $$f(x) = \frac{x}{x^{1/3}-1}$$
```
if __name__ == "__main__": # Función main par indicar el inicio del código
  x = int(input("Ingrese numero a: ")) # Se inicializa la variable
  if x == 1:
    print("Valor invalido, resultado indeterminado") # Caso indeterminado
  else:
    operacion = (lambda x: x/(x**(1/3)-1))(x) # Caso convencional
    print(f"Para {x} el resultado del cálculo es: {operacion}")
```
  ### N°3
  Cree una función que reciba dos números y un parametro con el cual se decida si regresa el mayor o el menor, por defecto debe regresar el mayor.
```
# Se especifican los datos que entran y salen, y se especifica el valor por defecto de la preferencia
def Comparacion(a : int, b : int, preferencia : str = "mayor", c : int = 0)-> int: 
  if b > a: # condición para reorganizar los datos
    c: int = b
    b = a
    a = c
  if preferencia == "mayor": # Caso convencional o por defecto
    return a
  else:
    return b # Caso contrario si así se desea
valor: int = 0
if __name__ == "__main__": # Función main par indicar el inicio del código
  # Se declaran e inicializan las variables
  a = int(input("Ingrese numero a: "))
  b = int(input("Ingrese numero b: "))
  preferencia = str(input("Deseas ver cuál es (mayor) o (menor)?"))

  if a == b: # condición de igualdad
    print("Ambos son el mismo valor, por ende son iguales")
  else: # caso contrario, donde se llama a la función con todos los valores y con uno por defecto
    valor = Comparacion(a, b)
    print(f"Entre {a} y {b}, {valor} es mayor")
    valor = Comparacion(a, b, preferencia)
    print(f"{valor} es el {preferencia}")
```
## Funciones del reto
  ### Funciones en forma de lambdas
  #### N# 1 Calcular el modulo de 2 valores:
  [![Lambda1.png](https://i.postimg.cc/sDLsQtcy/Lambda1.png)](https://postimg.cc/TpnZBNFH)
  
  #### N# 2 Calcular el cambio recibido al comprar ciertos artículos en una tienda:
  [![Lambda2.png](https://i.postimg.cc/65rFwgmY/Lambda2.png)](https://postimg.cc/Lnsx3CR1)
  
  #### N# 3 Calcular la cantidad de contagiados de un virus luego de D dias y partiendo de una cantidad base C:
  [![Lambda3.png](https://i.postimg.cc/90t155Q9/Lambda3.png)](https://postimg.cc/5Qy8Lrv9)
  
  ### Funciones con argumentos no definidos (*args)
  #### N# 1 Calcular el promedio de 5 valores:
  [![args1.png](https://i.postimg.cc/BnsbnWQ6/args1.png)](https://postimg.cc/zVt8xchZ) 
  
  ##### N# 2 Calcular el promedio multiplicativo de 5 valores:
  [![args2.png](https://i.postimg.cc/4NXRKXtr/args2.png)](https://postimg.cc/K4pHwS0N)
  
  #### N# 3 Ordenar los datos de menor a mayor:
  [![args3-1.png](https://i.postimg.cc/YS6xmBQs/args3-1.png)](https://postimg.cc/4K3crML6)
  [![args3-2.png](https://i.postimg.cc/dDc1Cp25/args3-2.png)](https://postimg.cc/4Hwsk8Fc)
  
  ### Punto #3
Escriba una función recursiva para calcular la operación de la potencia.
***
[![punto3.png](https://i.postimg.cc/bJYBR9H8/punto3.png)](https://postimg.cc/NyVDsTzP)

  ### Punto #4
Realice pruebas para calcular fibonacci con iteración o con recursión. Determine desde que número de la serie la diferencia de tiempo se vuelve significativa.
```
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
```
## Perfiles solicitados:
***
  ### Stackoverflow:
[![stackoverflow.png](https://i.postimg.cc/T3dskBSW/stackoverflow.png)](https://postimg.cc/MvLtH3zW)

  ### Linkedln:
www.linkedin.com/in/lucas-garcía-álvarez-050268305
