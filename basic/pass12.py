variable = 3  # Define una variable global llamada 'variable' con el valor 3.
def funcion():
    # Dentro de la función, definimos otra variable llamada 'variable'.
    # Esta es una variable local, distinta de la variable global.
    variable = 0  # Le asignamos el valor 0 a la variable local.
    # Imprimimos el valor de la variable local dentro de la función.
    print(variable)
funcion()

# Después de llamar a la función, imprimimos el valor de la variable global.
# La variable global no fue modificada por la variable local dentro de la función.
print(variable)