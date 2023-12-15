def es_bisiesto(anio):
  """
  Devuelve True si el año es bisiesto, False en caso contrario.

  Parámetros:
    anio: El año a comprobar.

  Devuelve:
    True si el año es bisiesto, False en caso contrario.
  """

  return (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0

def validar_fecha(dia, mes, anio):
  """
  Valida una fecha compuesta por el día, mes y año.

  Parámetros:
    dia: El día de la fecha.
    mes: El mes de la fecha.
    anio: El año de la fecha.

  Devuelve:
    None si la fecha es válida, un mensaje de error en caso contrario.
  """

  if dia < 1 or dia > 31:
    return "El día debe estar entre 1 y 31."

  if mes < 1 or mes > 12:
    return "El mes debe estar entre 1 y 12."

  if mes == 2:
    if es_bisiesto(anio):
      if dia > 29:
        return "El día en febrero no puede ser mayor que 29 en un año bisiesto."
    else:
      if dia > 28:
        return "El día en febrero no puede ser mayor que 28 en un año no bisiesto."

  if mes in (1, 3, 5, 7, 8, 10, 12):
    if dia > 31:
      return "El día en este mes no puede ser mayor que 31."

  if mes in (4, 6, 9, 11):
    if dia > 30:
      return "El día en este mes no puede ser mayor que 30."

  return None


if __name__ == "__main__":
  dia = int(input("Introduce el día: "))
  mes = int(input("Introduce el mes: "))
  anio = int(input("Introduce el año: "))

  mensaje_error = validar_fecha(dia, mes, anio)
  if mensaje_error is not None:
    print(mensaje_error)
  else:
    print("Fecha válida.")
