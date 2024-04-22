if __name__ == "__main__": # Función main par indicar el inicio del código
  x = int(input("Ingrese numero a: ")) # Se inicializa la variable
  if x == 1:
    print("Valor invalido, resultado indeterminado") # Caso indeterminado
  else:
    operacion = (lambda x: x/(x**(1/3)-1))(x) # Caso convencional
    print(f"Para {x} el resultado del cálculo es: {operacion}")