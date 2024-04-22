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