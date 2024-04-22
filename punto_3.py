def operacion (a: float, n: float, potencia: float = 1) -> float: # Datos que ingresan y salen de la función
    n -= 1 # Se actualiza
    if n <= -1:
        return potencia # caso base para finalizar la recursión
    else:
        potencia *= a # caso opuesto en donde se actualiza la variable potencia y se da la recursión
    return operacion(a, n, potencia)