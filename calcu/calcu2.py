# Define una función para la calculadora
def calcular_resistencia(codigo):
    # Crea un diccionario que asocia cada color con su valor numérico
    colores = {
        "negro": 0,
        "marrón": 1,
        "rojo": 2,
        "naranja": 3,
        "amarillo": 4,
        "verde": 5,
        "azul": 6,
        "violeta": 7,
        "gris": 8,
        "blanco": 9
    }
    
    # Extrae los valores numéricos de los colores y los convierte en una cadena de texto
    valor = str(colores[codigo[0]]) + str(colores[codigo[1]])
    multiplicador = colores[codigo[2]]
    
    # Calcula la resistencia en ohms y la convierte en una cadena de texto con la notación adecuada
    resistencia = int(valor) * 10**multiplicador
    if resistencia >= 1e6:
        resistencia_texto = str(resistencia/1e6) + "MΩ"
    elif resistencia >= 1e3:
        resistencia_texto = str(resistencia/1e3) + "kΩ"
    else:
        resistencia_texto = str(resistencia) + "Ω"
        
    # Retorna la resistencia calculada como una cadena de texto
    return resistencia_texto

# Ejecuta la función con un ejemplo de código de colores
codigo = ["marrón", "negro", "rojo", "oro"]
resistencia = calcular_resistencia(codigo)
print("La resistencia es", resistencia)
