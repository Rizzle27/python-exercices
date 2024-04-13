# En una función se pueden pasar 2 vectores con su punto inicial es el orígen del sistema de representación (0, 0) y que v1 = (x1, y1) y v2 = (x2, y2). Resolver:
# Si el v2 es paralelo al v1 devolver true
# Si el v2 es opuesto al v1 devolver true
# Si el v2 no es ni opuesto ni paralelo devolver false

# En la siguiente función calculo la pendiente (inclinación) de ambos vectores y la igualo. Si la pendiente es igual u opuesta entonces devuelvo true. En caso de que no sea igual ni opuesta devuelvo false
# Para calcular la pendiente resto los puntos más alejados del orígen con los puntos del orígen (0, 0)

def collinearity(x1, y1, x2, y2):
  # Caso sin vectores. Escalares (orígen)
  if(x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0):
    return True
  # Caso un vector y un escalar (orígen)
  elif((x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0)):
    return True
  # Caso 2 vectores
  elif((x1 != 0 and x2 != 0) and (y1 != 0 and y2 != 0)):
    pendienteV1 = ((y1 - 0) / (x1 - 0))
    pendienteV2 = ((y2 - 0) / (x2 - 0))
    if(pendienteV1 == pendienteV2 or pendienteV1 == (-1/pendienteV2)):
      return True
    else:
      return False
  # Caso 2 vectores paralelos al eje Y
  elif((x1 == 0 and y1 != 0) and (x2 == 0 and y2 != 0)):
    return True
  # Caso 2 vectores paralelos al eje X
  elif((x1 != 0 and y1 == 0) and (x2 != 0 and y2 == 0)):
    return True
  else:
    return False

print(collinearity(1,0,1,0))

# Al terminar este ejercicio aprendí que los vectores colineales pueden definirse de la siguiente forma:
# |x1 * y2| = |x2 * y1|