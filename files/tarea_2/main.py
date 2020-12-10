from datetime import date


def verificar_fecha(fecha: str) -> [bool, str or None]:
    try:
        day, month, year = fecha.strip().split('/')
        date(int(year), int(month), int(day))
        if int(year) < 2010 or int(year) > 2020:
            raise Exception('Anio debe estar entre 2010 y 2020')
        return [True, None]
    except ValueError and Exception as error:
        return [False, error]


def obtener_ultimo_codigo_enc_vta() -> int:
    names_file = open('db/ENC_VTA.dat', 'r')
    last = ""
    for line in names_file:
        last = line
    names_file.close()
    if last == "":
        return 0
    return int(last.split(";")[0])


def verificar_vendedor(codigo: int) -> bool:
    return True


def agregar_encabezado(fecha: str, cod_vendedor: int, estado: str) -> bool:
    encab_file = open('db/ENC_VTA.dat', 'a')
    existe_vendedor = verificar_vendedor(cod_vendedor)
    if not existe_vendedor:
        print("No existe vendedor con el codigo " + str(cod_vendedor))
        return False
    [fecha_valida, error] = verificar_fecha(fecha)
    if not fecha_valida:
        print("Fecha no es valida. Error: ", error)
    ultimo_codigo = obtener_ultimo_codigo_enc_vta()
    encab_file.write(str(ultimo_codigo + 1) + ';' + fecha + ';' + str(cod_vendedor) + ';' + estado + '\n')
    encab_file.close()


agregar_encabezado("28/02/2012", 23233, "V")
