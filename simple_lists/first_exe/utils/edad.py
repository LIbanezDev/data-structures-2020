def print_promedio_edad(base):
    iterator_age = base
    sumas_edades = {'M': [0, 0], 'F': [0, 0]}
    while iterator_age is not None:
        actual_suma = sumas_edades[iterator_age.sexo]
        sumas_edades[iterator_age.sexo] = [
            actual_suma[0] + 1, actual_suma[1] + iterator_age.edad
        ]
        iterator_age = iterator_age.next

    promedios = {
        'M': 0 if sumas_edades['M'][0] == 0 else sumas_edades['M'][1] / sumas_edades['M'][0],
        'F': 0 if sumas_edades['F'][0] == 0 else sumas_edades['F'][1] / sumas_edades['F'][0]
    }

    print("Hombres: " + str(promedios['M']) + "\nMujeres: " + str(promedios['F']))
