def classificar_regras(temperatura, umidade):
    if temperatura < 21:
        return "Frio"
    elif temperatura <= 28:
        return "Confortavel"
    else:
        return "Quente"
