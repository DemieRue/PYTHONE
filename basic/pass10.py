# Define una función llamada 'resta' que toma dos argumentos opcionales, 'num_1' y 'num_2', con valores por defecto de 3 y 2 respectivamente.
def resta(num_1=3,num_2=2):
    # Retorna la diferencia entre 'num_1' y 'num_2'.
    return num_1-num_2
# Llama a la función 'resta' sin argumentos, usando los valores por defecto, e imprime el resultado junto con una cadena descriptiva.
print("con valores por defecto:",resta())
# Llama a la función 'resta' con un argumento posicional (10), que anulará el valor por defecto de 'num_1', e imprime el resultado.
print("usando el orden con solo 1 valor:",resta(10))
# Llama a la función 'resta' con dos argumentos posicionales (10 y 3), que anularán ambos valores por defecto, e imprime el resultado.
print("usando el orden con todos los valores:",resta(10,3))
# Llama a la función 'resta' usando argumentos de palabra clave para establecer explícitamente 'num_1' en 15 y 'num_2' en 3, e imprime el resultado.
print("con keyword arguments:",resta(num_1=15,num_2=3))
# Llama a la función 'resta' con solo un argumento de palabra clave para establecer 'num_2' en 3, usando el valor por defecto para 'num_1', e imprime el resultado.
print("con solo un keyword argument:",resta(num_2=3))