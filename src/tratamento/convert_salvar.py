def ConverterTempo(tempo, unidade):
    if unidade == "m":
        return tempo*60
    if unidade == "s":
        return tempo

def ConverteMetros(quantidade, unidade):
    if unidade == "M":
        return quantidade*100
    if unidade == "m":
        return quantidade