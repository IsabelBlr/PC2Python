def convertir_fecha(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    partes = fecha.split()  

    if "/" in fecha:
        mes, dia, ano = map(int, partes[0].split("/"))
    else:
        mes = partes[0]
        dia = int(partes[1].strip(","))
        ano = int(partes[2])

    if isinstance(mes, str):
        mes = meses.index(mes) + 1

    return f"{ano:04d}-{mes:02d}-{dia:02d}" 



fecha_input = input("Ingrese una fecha (en formato mes/día/año o Mes día, año): ")


fecha_convertida = convertir_fecha(fecha_input)
print("Fecha convertida:", fecha_convertida)