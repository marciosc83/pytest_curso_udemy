def classifica_idade(idade):
    if idade < 12:
        return "CRIANÇA"
    elif idade < 18:
        return "ADOLESCENTE"
    elif idade < 60:
        return "ADULTO"
    else:
        return "IDOSO"