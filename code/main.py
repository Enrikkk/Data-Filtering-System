import math
import sys
import re


# FECHAS
def bisiesto(anio):
    return int(anio) % 4 == 0 and (int(anio) % 400 == 0 or not int(anio) % 100 == 0)


def fechaCorrecta(anio, mes, dia):
    if (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia <= 30:
        return True
    elif ((mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10
           or mes == 12) and dia <= 31):
        return True
    elif mes == 2:
        if bisiesto(anio) and 29 >= dia >= 1:
            return True
        if not (bisiesto(anio)) and 28 >= dia >= 1:
            return True
    return False


def horaCorrecta(hora, minuto, segundo):
    if int(hora) < 0 or int(hora) > 23 or int(minuto) < 0 or int(minuto) > 59 or int(segundo) < 0 or int(segundo) > 59:
        return False
    else:
        return True


def comprueba_fecha(dia, mes, anio):
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and (1 <= dia <= 31):
        return True
    if bisiesto(anio) and mes == 2 and (1 <= dia <= 29):
        return True
    if mes == 2 and (dia < 1 or dia > 28):
        return False
    if dia < 1 or dia > 30:
        return False
    return True


# NIF
def letra_dni(numero):
    solucion = numero % 23
    lista = "TRWAGMYFPDXBNJZSQVHLCKE"
    return lista[solucion]


def letra_dni_extranjero(cadena):
    if cadena[0] == "X":
        cadena = "0" + cadena[1:8]
    elif cadena[0] == "Y":
        cadena = "1" + cadena[1:8]
    elif cadena[0] == "Z":
        cadena = "2" + cadena[1:8]
    return letra_dni(int(cadena))


def is_DNI_extranjero(cadena):
    if cadena[0] == "X" or cadena[0] == "Y" or cadena[0] == "Z":
        return True
    return False


def dni_valido(cadena):
    # "121345678Z"
    if is_DNI_extranjero(cadena):
        return True
    numero = int(cadena[0:8])
    if letra_dni(numero) == cadena[8]:
        return True
    else:
        return False


# EXPRESIONES REGULARES
telf = re.compile(r"^\d{9}$|^(\d{3} ?\d{3} ?\d{3})$")
telf2 = re.compile(r"^\+(?:\d ?){10,15}$")
nif = re.compile(r"(\d{8}[-A-HJ-NP-TV-Z])|([X-Z]\d{7}[-A-HJ-NP-TV-Z])")
temp = re.compile(
    r"(?P<formato1>(?P<ano1>\d{4})-(?P<mes1>0[1-9]|1[0-2])-(?P<dia1>0[1-9]|[12][0-9]|3[01])\s+(?P<hora1>[01][0-9]|2[0-3]):(?P<min1>[0-5][0-9]))"
    r"|(?P<formato2>(?P<mes2>January|February|March|April|May|June|July|August|September|October|November|December)\s+(?P<dia2>[1-9]|[12][0-9]|3[01]),\s+(?P<ano2>\d{4})\s+(?P<hora2>0?[1-9]|1[0-2]):(?P<min2>[0-5][0-9])\s+(?P<AM_PM>AM|PM|am|pm))"
    r"|(?P<formato3>(?P<hora3>[01][0-9]|2[0-3]):(?P<min3>[0-5][0-9]):(?P<seg3>[0-5][0-9])\s+(?P<dia3>0[1-9]|[12][0-9]|3[01])/(?P<mes3>0[1-9]|1[0-2])/(?P<ano3>\d{4}))",
    re.IGNORECASE
)


import re

coord = re.compile(
    # ---------- DECIMAL ----------
    r"(?P<formato1>"
        r"(?P<decimal>"
            r"(?P<latitudDecimal>[+-]?(?:\d|[1-8]\d|90)\.\d+)\s*,\s*"
            r"(?P<longitudDecimal>[+-]?(?:\d|[1-9]\d|1[0-7]\d|180)\.\d+)"
        r")"
    r")"
    r"|"
    # ---------- SEXAGESIMAL ----------
    r"(?P<formato2>"
        r"(?P<sexagesimal>"
            r"(?P<latitudSexagesimal>"
                r"(?P<gradosLatitudSexagesimal>(?:\d|[1-8]\d|90))[º°]\s*"
                r"(?P<minutosLatitudSexagesimal>\d|[1-5]\d)'\s*"
                r"(?P<segundosLatitudSexagesimal>(?:\d|[1-5]\d|60)\.\d{4})\"\s*"
                r"(?P<orientacionLatitudSexagesimal>[NS])"
            r")\s*,\s*"
            r"(?P<longitudSexagesimal>"
                r"(?P<gradosLongitudSexagesimal>(?:\d|[1-9]\d|1[0-7]\d|180))[º°]\s*"
                r"(?P<minutosLongitudSexagesimal>\d|[1-5]\d)'\s*"
                r"(?P<segundosLongitudSexagesimal>(?:\d|[1-5]\d|60)\.\d{4})\"\s*"
                r"(?P<orientacionLongitudSexagesimal>[EW])"
            r")"
        r")"
    r")"
    r"|"
    # ---------- GPS (fixed, same group names) ----------
    r"(?P<formato3>"
        r"(?P<GPS>"
            r"(?P<gradosLatitudGPS>\d{2,3})"
            r"(?P<minutosLatitudGPS>[0-5]\d)"
            r"(?P<segundosLatitudGPS>\d{2}\.\d{4})"
            r"(?P<orientacionLatitudGPS>[NS])"
            r"(?P<gradosLongitudGPS>\d{3})"
            r"(?P<minutosLongitudGPS>[0-5]\d)"
            r"(?P<segundosLongitudGPS>\d{2}\.\d{4})"
            r"(?P<orientacionLongitudGPS>[EW])"
        r")"
    r")"
)



din = re.compile(r"((?P<euros>\d*)(?P<centimos>(\.\d*))?€)")


# ----------CONVERSORES DE TIEMPOS----------
# --------------------------------------------------
# MESES A MESES NUMERICOS
# --------------------------------------------------
def mesNumerico(tiempo):
    resultado = temp.fullmatch(tiempo.strip(" "))
    meses = re.compile(
        r"(?i)(?P<enero>January)|(?P<febrero>February)|(?P<marzo>March)|(?P<abril>April)|(?P<mayo>May)|("
        r"?P<junio>June)|(?P<julio>July)|(?P<agosto>August)|(?P<septiembre>September)|(?P<octubre>October)|("
        r"?P<noviembre>November)|(?P<diciembre>December)")
    Mes = meses.fullmatch(resultado.group("mes2").strip(" "))

    MES = 0

    if Mes.group("enero") is not None:
        MES = 1
    elif Mes.group("febrero") is not None:
        MES = 2
    elif Mes.group("marzo") is not None:
        MES = 3
    elif Mes.group("abril") is not None:
        MES = 4
    elif Mes.group("mayo") is not None:
        MES = 5
    elif Mes.group("junio") is not None:
        MES = 6
    elif Mes.group("julio") is not None:
        MES = 7
    elif Mes.group("agosto") is not None:
        MES = 8
    elif Mes.group("septiembre") is not None:
        MES = 9
    elif Mes.group("octubre") is not None:
        MES = 10
    elif Mes.group("noviembre") is not None:
        MES = 11
    elif Mes.group("diciembre") is not None:
        MES = 12
    return MES


# --------------------------------------------------
# FORMATO 2 A FORMATO 1
# --------------------------------------------------
def convertirFormato2Formato1(tiempo):
    resultado = temp.fullmatch(tiempo.strip(" "))
    anio = int(resultado.group("ano2"))
    mes = mesNumerico(tiempo)
    dia = int(resultado.group("dia2"))
    minutos = int(resultado.group("min2"))
    if resultado.group("AM_PM") == "PM":
        hora = int(resultado.group("hora2")) + 12
    else:
        hora = int(resultado.group("hora2"))
    return f"{anio:04d}-{mes:02d}-{dia:02d} {hora:02d}:{minutos:02d}"


# --------------------------------------------------
# FORMATO 3 A FORMATO 1
# --------------------------------------------------
def convertirFormato3Formato1(tiempo):
    resultado = temp.fullmatch(tiempo.strip(" "))
    anio = int(resultado.group("ano3"))
    mes = int(resultado.group("mes3"))
    dia = int(resultado.group("dia3"))
    hora = int(resultado.group("hora3"))
    minutos = int(resultado.group("min3"))
    return f"{anio:04d}-{mes:02d}-{dia:02d} {hora:02d}:{minutos:02d}"


# ----------CONVERSORES DE COORDENADAS----------
# --------------------------------------------------
# DECIMAL A GPS
# --------------------------------------------------
def convertidorLatitudDecimalGPS(coordenada):
    resultado = coord.fullmatch(coordenada.strip(" "))
    latitudDecimal = abs(float(resultado.group("latitudDecimal")))
    gradosDecimales = int(latitudDecimal)
    minutosDecimales = int((latitudDecimal - gradosDecimales) * 60)
    segundos = ((latitudDecimal - gradosDecimales) * 60 - minutosDecimales) * 60
    decimalesSegundos = "{:.4f}".format(segundos)
    if float(resultado.group("latitudDecimal")) >= 0:
        orientacionDecimal = "N"
    else:
        orientacionDecimal = "S"
    return f"{gradosDecimales:03d}{minutosDecimales:02d}{decimalesSegundos}{orientacionDecimal}"


def convertidorLongitudDecimalGPS(coordenada):
    resultado = coord.fullmatch(coordenada.strip(" "))
    longitudDecimal = abs(float(resultado.group("longitudDecimal")))
    gradosDecimales = int(longitudDecimal)
    minutosDecimales = int((longitudDecimal - gradosDecimales) * 60)
    segundos = ((longitudDecimal - gradosDecimales) * 60 - minutosDecimales) * 60
    decimalesSegundos = "{:.4f}".format(segundos)
    if float(resultado.group("longitudDecimal")) >= 0:
        orientacionDecimal = "E"
    else:
        orientacionDecimal = "W"

    return f"{gradosDecimales:03d}{minutosDecimales:02d}{decimalesSegundos}{orientacionDecimal}"


def convertidorDecimalGPS(coordenadas):
    return convertidorLatitudDecimalGPS(coordenadas) + convertidorLongitudDecimalGPS(coordenadas)


# --------------------------------------------------
# SEXAGESIMAL A GPS
# --------------------------------------------------
def convertidorLatitudSexagesimalGPS(coordenada):
    resultado = coord.fullmatch(coordenada.strip(" "))
    gradosSexagesimal = int(resultado.group("gradosLatitudSexagesimal"))
    minutosSexagesimal = int(resultado.group("minutosLatitudSexagesimal"))
    segundosSexagesimal = resultado.group("segundosLatitudSexagesimal")
    orientacionSexagesimal = resultado.group("orientacionLatitudSexagesimal")
    return f"{gradosSexagesimal:03d}{minutosSexagesimal:02d}{segundosSexagesimal}{orientacionSexagesimal}"


def convertidorLongitudSexagesimalGPS(coordenada):
    resultado = coord.fullmatch(coordenada.strip(" "))
    gradosSexagesimal = int(resultado.group("gradosLongitudSexagesimal"))
    minutosSexagesimal = int(resultado.group("minutosLongitudSexagesimal"))
    segundosSexagesimal = resultado.group("segundosLongitudSexagesimal")
    orientacionSexagesimal = resultado.group("orientacionLongitudSexagesimal")
    return f"{gradosSexagesimal:03d}{minutosSexagesimal:02d}{segundosSexagesimal}{orientacionSexagesimal}"


def convertidorSexagesimalGPS(coordenadas):
    return convertidorLatitudSexagesimalGPS(coordenadas) + convertidorLongitudSexagesimalGPS(coordenadas)


# ----------FORMATOS----------
# --------------------------------------------------
# FORMATOS DE TIEMPO
# --------------------------------------------------

def tiempoFormato1(tiempo):
    resultado = temp.fullmatch(tiempo.strip(" "))
    if resultado:
        if (comprueba_fecha(int((resultado.group("dia1"))), int((resultado.group("mes1"))),
                            int((resultado.group("ano1"))))
                and horaCorrecta(int(resultado.group("hora1")), int(resultado.group("min1")), 0)):
            return True
        else:
            # Se cumple el fullmatch pero el instante temporal no es correcto.
            print("\nFormato correcto pero instante temporal incorrecto.")
            return False
    else:
        print("\nInstante temporal incorrecto")  # No se cumple el fullmatch.
        return None


def tiempoFormato2(tiempo):
    resultado = temp.fullmatch(tiempo.strip(" "))
    if resultado:
        meses = re.compile(
            r"(?i)(?P<enero>January)|(?P<febrero>February)|(?P<marzo>March)|(?P<abril>April)|(?P<mayo>May)|("
            r"?P<junio>June)|(?P<julio>July)|(?P<agosto>August)|(?P<septiembre>September)|(?P<octubre>October)|("
            r"?P<noviembre>November)|(?P<diciembre>December)")
        Mes = meses.fullmatch(resultado.group("mes2").strip(" "))

        MES = 0

        if Mes.group("enero") is not None:
            MES = 1
        elif Mes.group("febrero") is not None:
            MES = 2
        elif Mes.group("marzo") is not None:
            MES = 3
        elif Mes.group("abril") is not None:
            MES = 4
        elif Mes.group("mayo") is not None:
            MES = 5
        elif Mes.group("junio") is not None:
            MES = 6
        elif Mes.group("julio") is not None:
            MES = 7
        elif Mes.group("agosto") is not None:
            MES = 8
        elif Mes.group("septiembre") is not None:
            MES = 9
        elif Mes.group("octubre") is not None:
            MES = 10
        elif Mes.group("noviembre") is not None:
            MES = 11
        elif Mes.group("diciembre") is not None:
            MES = 12

        if resultado.group("AM_PM") == "AM":
            HORA = resultado.group("hora2")
        else:
            HORA = int(resultado.group("hora2")) + 12

        if (comprueba_fecha(int((resultado.group("dia2"))), MES, int((resultado.group("ano2"))))
                and horaCorrecta(HORA, int(resultado.group("min2")), 0)):
            # Ponemos el campo de segundos a 0 para que se valide siempre ese campo, puesto que este formato no
            # incluye segundos.
            return True
        else:
            print(
                "\nFormato correcto pero instante temporal incorrecto.")  # Se cumple el fullmatch pero el instante
            # temporal no es correcto.
            return False
    else:
        print("\nInstante temporal incorrecto")  # No se cumple el fullmatch.
        return None


def tiempoFormato3(tiempo):
    resultado = temp.fullmatch(tiempo.strip(" "))
    if resultado:
        if (comprueba_fecha(int((resultado.group("dia3"))), int((resultado.group("mes3"))),
                            int((resultado.group("ano3"))))
                and horaCorrecta(int(resultado.group("hora3")), int(resultado.group("min3")),
                                 int(resultado.group("seg3")))):
            return True
        else:
            print(
                "\nFormato correcto pero instante temporal incorrecto.")  # Se cumple el fullmatch pero el instante
            # temporal no es correcto.
            return False
    else:
        print("\nInstante temporal incorrecto")  # No se cumple el fullmatch.
        return None


def comprobarFormato1(tiempo):
    resultado = temp.fullmatch(tiempo.strip(" "))
    if resultado:
        if resultado.group("formato1") is not None:
            return True
        else:
            return None
    else:
        print("Formato de tiempo incorrecto.")
        return False


def comprobarFormato2(tiempo):
    resultado = temp.fullmatch(tiempo.strip(" "))
    if resultado:
        if resultado.group("formato2") is not None:
            return True
        else:
            return None
    else:
        print("Formato de tiempo incorrecto.")
        return False


def comprobarFormato3(tiempo):
    resultado = temp.fullmatch(tiempo.strip(" "))
    if resultado:
        if resultado.group("formato3") is not None:
            return True
        else:
            return None
    else:
        print("Formato de tiempo incorrecto.")
        return False


# --------------------------------------------------
# FORMATO COORDENADAS
# --------------------------------------------------
def coordenadasFormato1(coordenada):
    resultado = coord.fullmatch(coordenada.strip(" "))
    if resultado:
        if resultado.group("formato1") is not None:
            return True
        else:
            return None
    else:
        print("Formato de coordenadas incorrecto.")
        return False


def coordenadasFormato2(coordenada):
    resultado = coord.fullmatch(coordenada.strip(" "))
    if resultado:
        if resultado.group("formato2") is not None:
            return True
        else:
            return None
    else:
        print("Formato de coordenadas incorrecto.")
        return False


def coordenadasFormato3(coordenada):
    resultado = coord.fullmatch(coordenada.strip(" "))
    if resultado:
        if resultado.group("formato3") is not None:
            return True
        else:
            return None
    else:
        print("Formato de coordenadas incorrecto.")
        return False


# ----------VALIDACIONES----------
# --------------------------------------------------
# NUMERO TELEFONO
# --------------------------------------------------
def validaNum(numero):
    if numero.strip(" ")[0] != '+':
        resultado = telf.fullmatch(numero.replace(" ", ""))
        if resultado:
            return dict([('telefono', numero.replace(" ", ""))])
        else:
            return None
    else:
        resultado = telf2.fullmatch(numero.replace(" ", ""))
        if resultado:
            return dict([('telefono', numero.replace(" ", ""))])
        else:
            return None


# --------------------------------------------------
# NIF
# --------------------------------------------------
def validaNIF(NIF):
    resultado = nif.fullmatch(NIF.strip(" "))
    if resultado:
        if dni_valido(NIF):
            return dict([('nif', NIF)])
        else:
            return None
    else:
        return None


# --------------------------------------------------
# TIEMPO
# --------------------------------------------------
def validaTiempo(tiempo):
    resultado = temp.fullmatch(tiempo.rstrip())
    if resultado:

        if resultado.group("formato2") is not None:  # Formato 2 detectado.

            # Formato 2 -> August 6, 1945 8:15 AM
            meses = re.compile(
                r"(?i)(?P<enero>January)|(?P<febrero>February)|(?P<marzo>March)|(?P<abril>April)|(?P<mayo>May)|(?P<junio>June)|(?P<julio>July)|(?P<agosto>August)|(?P<septiembre>September)|(?P<octubre>October)|(?P<noviembre>November)|(?P<diciembre>December)")
            Mes = meses.fullmatch(resultado.group("mes2").rstrip())

            MES = 0

            if Mes.group("enero") is not None:
                MES = 1
            elif Mes.group("febrero") is not None:
                MES = 2
            elif Mes.group("marzo") is not None:
                MES = 3
            elif Mes.group("abril") is not None:
                MES = 4
            elif Mes.group("mayo") is not None:
                MES = 5
            elif Mes.group("junio") is not None:
                MES = 6
            elif Mes.group("julio") is not None:
                MES = 7
            elif Mes.group("agosto") is not None:
                MES = 8
            elif Mes.group("septiembre") is not None:
                MES = 9
            elif Mes.group("octubre") is not None:
                MES = 10
            elif Mes.group("noviembre") is not None:
                MES = 11
            elif Mes.group("diciembre") is not None:
                MES = 12

            if resultado.group("AM_PM") == "AM":
                HORA = resultado.group("hora2")
            else:
                HORA = int(resultado.group("hora2")) + 12

            if (fechaCorrecta(int((resultado.group("ano2"))), MES, int((resultado.group("dia2"))))
                    and horaCorrecta(HORA, int(resultado.group("min2")), 0)):
                D = dict(fecha=tiempo, año=resultado.group("ano2"), mes=MES,
                         dia=resultado.group("dia2"), hora=HORA, minutos=resultado.group("min2"), segundos=0)
                # Ponemos el campo de segundos a 0 para que se valide siempre ese campo, puesto que este formato no
                # incluye segundos.
                return D
            else:
                return None

        if resultado.group("formato1") is not None:  # Formato 1 detectado.

            # Formato 1 -> 1945-08-06 08:15

            if (fechaCorrecta(int((resultado.group("ano1"))), int((resultado.group("mes1"))),
                              int((resultado.group("dia1"))))
                    and horaCorrecta(int(resultado.group("hora1")), int(resultado.group("min1")), 0)):
                D = dict(fecha=tiempo, año=resultado.group("ano1"), mes=resultado.group("mes1"),
                         dia=resultado.group("dia1"),
                         hora=resultado.group("hora1"), minutos=resultado.group("min1"), segundos=0)
                # Segundos a 0 para que los valide siempre, ya que el formato no incluye segundos.
                return D
            else:
                return None

        if resultado.group("formato3") is not None:  # Formato 3 detectado.

            # Formato 3 -> 08:15:00 06/08/1945

            if (fechaCorrecta(int((resultado.group("ano3"))), int((resultado.group("mes3"))),
                              int((resultado.group("dia3"))))
                    and horaCorrecta(int(resultado.group("hora3")), int(resultado.group("min3")),
                                     int(resultado.group("seg3")))):
                D = dict(fecha=tiempo, año=resultado.group("ano3"), mes=resultado.group("mes3"),
                         dia=resultado.group("dia3"),
                         hora=resultado.group("hora3"), minutos=resultado.group("min3"),
                         segundos=resultado.group("seg3"))

                return D
            else:
                return None

    else:
        # print("Instante temporal incorrecto") # No se cumple el fullmatch.
        return None


# --------------------------------------------------
# COORDENADAS
# --------------------------------------------------
def validaCoord(coordenada):
    resultado = coord.fullmatch(coordenada.rstrip())
    if resultado:
        # print("Formato correcto y coordenada correcta.")
        if resultado.group("decimal") is not None:
            D = dict(latitud=float(resultado.group("latitudDecimal")),
                     longitud=float(resultado.group("longitudDecimal")))
            return D

        elif resultado.group("sexagesimal") is not None:
            latitud = resultado.group("gradosLatitudSexagesimal")
            latitud = float(latitud)
            minl = resultado.group("minutosLatitudSexagesimal")
            minl = float(minl)
            segl = resultado.group("segundosLatitudSexagesimal")
            segl = float(segl)
            Latitud = convertir_a_grados(latitud, minl, segl)
            if (resultado.group("orientacionLatitudSexagesimal") == "S" or resultado.group(
                    "orientacionLatitudSexagesimal") == "s"):
                Latitud = Latitud * (-1)

            longitud = resultado.group("gradosLongitudSexagesimal")
            longitud = float(longitud)
            minlo = resultado.group("minutosLongitudSexagesimal")
            minlo = float(minlo)
            seglo = resultado.group("segundosLongitudSexagesimal")
            seglo = float(seglo)
            Longitud = convertir_a_grados(longitud, minlo, seglo)
            if resultado.group("orientacionLongitudSexagesimal") == "W" or \
                    resultado.group("orientacionLongitudSexagesimal") == "w":
                Longitud = Longitud * (-1)
            D = dict(latitud=Latitud, longitud=Longitud)
            return D
        elif resultado.group("GPS") is not None:

            latitud = resultado.group("gradosLatitudGPS")
            latitud = float(latitud)
            minl = resultado.group("minutosLatitudGPS")
            minl = float(minl)
            segl = resultado.group("segundosLatitudGPS")
            segl = float(segl)
            Latitud = convertir_a_grados(latitud, minl, segl)
            if resultado.group("orientacionLatitudGPS") == "S" or resultado.group("orientacionLatitudGPS") == "s":
                Latitud = Latitud * (-1)

            longitud = resultado.group("gradosLongitudGPS")
            longitud = float(longitud)
            minlo = resultado.group("minutosLongitudGPS")
            minlo = float(minlo)
            seglo = resultado.group("minutosLongitudGPS")
            seglo = float(seglo)
            Longitud = convertir_a_grados(longitud, minlo, seglo)
            if resultado.group("orientacionLongitudGPS") == "W" or resultado.group("orientacionLongitudGPS") == "w":
                Longitud = Longitud * (-1)
            D = dict(latitud=Latitud, longitud=Longitud)
            return D
    else:
        # print("Formato de coordenadas incorrecto.")
        return None


# --------------------------------------------------
# DINERO
# --------------------------------------------------
def validaDinero(dinero):
    resultado = din.fullmatch(dinero.rstrip())
    if resultado:
        return True
    else:
        return False


# ----------PROGRAMA PRINCIPAL----------
# --------------------------------------------------
# -N
# --------------------------------------------------
def parsear_n(fichero):
    try:
        archivo = open(fichero, encoding='utf8')
    except FileNotFoundError:
        print("El fichero pasado como parametro es incorrecto", file=sys.stderr)
        return
    except Exception as error:
        print("Problema analizando el fichero:", error, file=sys.stderr)
        return
    try:
        for linea in archivo:
            campos = linea.split(";")

            if validaNum(campos[0].strip(" ")) and validaNIF(campos[1].strip(" ")) and validaTiempo(
                    campos[2].strip(" ")) and validaCoord(campos[3].strip(" ")) and validaDinero(
                    campos[5].strip(" ")):
                if comprobarFormato2(campos[2].strip(" ")):
                    tiempoFormato1N = convertirFormato2Formato1(campos[2].strip(" "))
                elif comprobarFormato3(campos[2].strip(" ")):
                    tiempoFormato1N = convertirFormato3Formato1(campos[2].strip(" "))
                else:
                    tiempoFormato1N = campos[2].strip(" ")
                if coordenadasFormato1(campos[3].strip(" ")):
                    coordenadasGPS = convertidorDecimalGPS(campos[3].strip(" "))
                elif coordenadasFormato2(campos[3].strip(" ")):
                    coordenadasGPS = convertidorSexagesimalGPS(campos[3].strip(" "))
                else:
                    coordenadasGPS = campos[3].strip(" ")
                print(
                    f"{campos[0].rstrip()};{campos[1].rstrip()};{tiempoFormato1N};{coordenadasGPS};"
                    f"{campos[4].rstrip()};{campos[5].rstrip()}")
    finally:
        archivo.close()


# --------------------------------------------------
# -SPHONE
# --------------------------------------------------
def parsear_sphone(telefono, fichero):
    
    if validaNum(telefono):
        try:
            archivo = open(fichero, encoding='utf8')
        except FileNotFoundError:
            print("El fichero pasado como parametro es incorrecto", file=sys.stderr)
            return
        except Exception as error:
            print("Problema analizando el fichero:", error, file=sys.stderr)
            return

        try:
            for linea in archivo:
                campos = linea.split(";")

                #if(campos[1].strip() == "94524959L") and (campos[5].strip() == "2312.5€"):
                #    print(validaNum(campos[0].strip(" ")))
                #    print(validaNIF(campos[1].strip(" ")))
                #    print(validaTiempo(campos[2].strip(" ")))
                #    print(validaCoord(campos[3].strip()))
                #    print(validaDinero(campos[5].strip(" ")))

                if validaNum(campos[0].strip(" ")) and validaNIF(campos[1].strip(" ")) and validaTiempo(
                        campos[2].strip(" ")) and validaCoord(campos[3].strip()) and validaDinero(
                        campos[5].strip(" ")):
                    
                    if(telf.fullmatch(campos[0].replace(" ", ""))):
                        resultado = telf.fullmatch(campos[0].replace(" ", ""))
                            

                        if resultado is not None:
                            num = campos[0].replace(" ", "")

                            if(telefono.replace(" ", ""))[0:3] == "+34":
                                num = "+34" + num

                            if(telefono.replace(" ", "") == num):  
                                print(linea, end='')

                    elif(telf2.fullmatch(campos[0].replace(" ", ""))):
                        resultado = telf2.fullmatch(campos[0].replace(" ", ""))

                        if resultado is not None:

                            num = campos[0].replace(" ", "")

                            if(telefono.replace(" ", ""))[0] != "+" and num[0:3] == "+34":
                                num = num[3:]

                            if(telefono.replace(" ", "") == num):    
                                print(linea, end='')

        finally:
            archivo.close()
    else:
        exit(1)


# --------------------------------------------------
# -SNIF
# --------------------------------------------------
def parsear_snif(NIF, fichero):
    if validaNIF(NIF):
        try:
            archivo = open(fichero, encoding='utf8')
        except FileNotFoundError:
            print("El fichero pasado como parametro es incorrecto", file=sys.stderr)
            return
        except Exception as error:
            print("Problema analizando el fichero:", error, file=sys.stderr)
            return

        try:
            for linea in archivo:
                campos = linea.split(";")
                if validaNum(campos[0].strip(" ")) and validaNIF(campos[1].strip(" ")) and validaTiempo(
                        campos[2].strip(" ")) and validaCoord(campos[3].strip(" ")) and validaDinero(
                        campos[5].strip(" ")):
                    if NIF == campos[1].strip(" "):
                        print(linea, end='')
        finally:
            archivo.close()
    else:
        print("Número de DNI inválido")
        exit(1)


# --------------------------------------------------
# -STIME
# --------------------------------------------------
def isContenido(tiempo, D1, D2):
    # Tenemos que verficiar si tiempo está dentro de D1 y D2, ambos inclusive.
    if D1.get("año") <= tiempo.get("año") <= D2.get("año"):
        # Si el año coincide, tenemos que ir comparando en los niveles inferiores temporales uno a uno.
        if D1.get("año") == tiempo.get("año"):
            # Meses...
            if int(D1.get("mes")) <= int(tiempo.get("mes")):
                if int(D1.get("mes")) == int(tiempo.get("mes")):
                    # Días...
                    if int(D1.get("dia")) <= tiempo.get("dia"):
                        if D1.get("dia") == tiempo.get("dia"):
                            if D1.get("hora") <= tiempo.get("hora"):
                                if D1.get("hora") == tiempo.get("hora"):
                                    if D1.get("minutos") <= tiempo.get("minutos"):
                                        if D1.get("minutos") == tiempo.get("minutos"):
                                            if D1.get("segundos") <= tiempo.get("segundos"):
                                                return True
                                            else:
                                                return False
                                        return True
                                    return False
                                return True
                            return False
                        return True
                    return False
                return True
            return False
        elif D2.get("año") == tiempo.get("año"):
            if int(tiempo.get("mes")) <= int(D2.get("mes")):
                if int(tiempo.get("mes")) == int(D2.get("mes")):
                    if int(tiempo.get("dia")) <= D2.get("dia"):
                        if tiempo.get("dia") == D2.get("dia"):
                            if tiempo.get("hora") <= D2.get("hora"):
                                if tiempo.get("hora") == D2.get("hora"):
                                    if tiempo.get("minutos") <= D2.get("minutos"):
                                        if tiempo.get("minutos") == D2.get("minutos"):
                                            if tiempo.get("segundos") <= D2.get("segundos"):
                                                return True
                                            else:
                                                return False
                                        return True
                                    return False
                                return True
                            return False
                        return True
                    return False
                return True
            return False
        else:
            # Tras tratar los casos que incluyen ser iguales que D1 o D2, tratamos el caso de estar estrictamente
            # entre estos. Básicamente, devolvemos True.
            return True
    return False


def parsear_stime(desde, hasta, fichero):
    D1 = validaTiempo(desde)
    D2 = validaTiempo(hasta)

    if D1 is not None and D2 is not None:
        try:
            archivo = open(fichero, encoding='utf8')
        except FileNotFoundError:
            print("El fichero pasado como parametro es incorrecto", file=sys.stderr)
            return
        except Exception as error:
            print("Problema analizando el fichero:", error, file=sys.stderr)
            return

        try:
            for linea in archivo:
                campos = linea.split(";")
                if validaNum(campos[0].strip(" ")) and validaNIF(campos[1].strip(" ")) and validaTiempo(
                        campos[2].strip(" ")) and validaCoord(campos[3].strip(" ")) and validaDinero(
                        campos[5].strip(" ")):
                    tiempo = validaTiempo(campos[2].strip(" "))  # Lo convertimos a diccionario
                    if isContenido(tiempo, D1, D2):
                        print(linea, end='')
        finally:
            archivo.close()
    else:
        print("Instante temporal incorrecto inválido")
        exit(1)


# --------------------------------------------------
# -SLOCATION
# --------------------------------------------------
def distanciaKilometros(latitud1, longitud1, latitud2, longitud2):
    radioTierra = 6371.0

    # De grados a radianes
    lat1 = math.radians(latitud1)
    lon1 = math.radians(longitud1)
    lat2 = math.radians(latitud2)
    lon2 = math.radians(longitud2)

    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1

    # Utilizamos la fórmula de Haversine
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = radioTierra * c

    return float(distancia)


def convertir_a_grados(grados, minutos, segundos):
    # Convertimos minutos y segundos a su valor en grados
    minutos_a_grados = minutos / 60
    segundos_a_grados = segundos / 3600
    resultado = grados + minutos_a_grados + segundos_a_grados

    return resultado


def parsear_slocation(desde, hasta, fichero):
    if int(hasta) >= 0 and validaCoord(desde):
        try:
            archivo = open(fichero, encoding='utf8')
        except FileNotFoundError:
            print("El fichero pasado como parametro es incorrecto", file=sys.stderr)
            return
        except Exception as error:
            print("Problema analizando el fichero:", error, file=sys.stderr)
            return
        try:
            for linea in archivo:
                campos = linea.split(";")
                if validaNum(campos[0].strip(" ")) and validaNIF(campos[1].strip(" ")) and validaTiempo(
                        campos[2].strip(" ")) and validaCoord(campos[3].strip(" ")) and validaDinero(
                        campos[5].strip(" ")):
                    origen = validaCoord(desde)
                    coordenada = validaCoord(campos[3].strip(" "))
                    if distanciaKilometros(origen["latitud"], origen["longitud"], coordenada["latitud"],
                                           coordenada["longitud"]) < float(hasta):
                        print(linea, end='')
        finally:
            archivo.close()
    else:
        print("Coordenada Inválida")
        exit(1)


def main():
    lista_argumentos = sys.argv
    if lista_argumentos[1] == "-n":
        parsear_n(lista_argumentos[2])
    elif lista_argumentos[1] == "-sphone":
        parsear_sphone(lista_argumentos[2], lista_argumentos[3])
    elif lista_argumentos[1] == "-snif":
        parsear_snif(lista_argumentos[2], lista_argumentos[3])
    elif lista_argumentos[1] == "-stime":
        parsear_stime(lista_argumentos[2], lista_argumentos[3], lista_argumentos[4])
    elif lista_argumentos[1] == "-slocation":
        parsear_slocation(lista_argumentos[2], lista_argumentos[3], lista_argumentos[4])
    else: 
        exit(2) # Introduced wrong parameters


main()
