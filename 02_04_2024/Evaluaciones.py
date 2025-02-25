def evaluar_resultado(resultado_algoritmo, resultado_conocido):
    msj_error = f'Error, resultado_algoritmo: {resultado_algoritmo} \
es diferente de resultado_conocido: {resultado_conocido}'
    assert resultado_algoritmo == resultado_conocido, msj_error
    print(f'El resultado:  {resultado_algoritmo} es correcto!')