# Existen 4 tipos de cursos: a) rápido, b) mínimo, c) promedio y d) máximo. Calcular:
# 1) Qué tan rapido es el "curso rápido" en comparación de los demás cursos
# 2) Cuantas horas de contenido inservible se ahorraron viendo el "curso rápido"
# 3) Si el "curso rápido" durara 10 horas, cuantas porcentaje de los otros cursos deberiamos ver para aprender el mismo contenido

curso_rapido = 1.5

otros_cursos = {
  "minimo": 2.5,
  "promedio": 4,
  "maximo": 7
}

def porcentaje(curso_rapido, mas_largo):
  return ((mas_largo - curso_rapido) / curso_rapido) * 100

def equivalencia(curso_rapido, mas_largo):
  curso_rapido_extendido = 10
  porcentaje_curso_rapido_extendido = (curso_rapido_extendido / curso_rapido) * 100
  return (mas_largo * (porcentaje_curso_rapido_extendido / 100))

for curso, duracion in otros_cursos.items():
  porcentaje_curso = porcentaje(curso_rapido, duracion)
  contenido_inservible = duracion - curso_rapido
  equivalencia_horas = equivalencia(curso_rapido, duracion)
  print(f'El curso rápido ({curso_rapido}) es un {round(abs(porcentaje_curso))}% más rápido que el curso {curso} ({duracion}). Se ahorraron {contenido_inservible} horas en contenido inservible. Tendrías que ver {round(equivalencia_horas)} horas del curso {curso} para hacer 10 horas del curso rápido ({curso_rapido})')