# realizar un programa que al recibir como datos 
# dos cadenas de caracteres forme una tercera cadena
# intercalando los caracteres de las palabras 
# de las cadenas recibidas

def intercalar(cadena1, cadena2): 
  resultado = "" 
  
  # recorrer las dos cadenas  
  for x, y in zip(cadena1, cadena2): 
    resultado += x + y  

  return resultado  
    
# driver code  
cadena1 = "holas"
cadena2 = "mundo"
print(intercalar(cadena1, cadena2))