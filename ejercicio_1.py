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