def SaidaTempo(tempo):
    
    minutos = 0
    segundos = 0

    segundos = tempo%60
    minutos = tempo//60
    minutos = minutos%60

    result = {
        "minutos": minutos,
        "segundos": segundos
    }
    return result


def SaidaMetros(quantidade):
    metros = quantidade//100
    m = quantidade%100

    result={
        "metros": metros,
        "m": m
    }
    return result