def ordenar_az(texto:str, ascendente=False): #ascendente es verdadero si quiero que sea en orden alfabetico
    lista_temp = list(texto) #la convierto en lista para que analice los caracteres por elementos separados
    tam = len(texto)
    for i in range(tam - 1): #burbujero
        for j in range(i + 1, tam): #burbujero
            if ascendente and lista_temp[i] > lista_temp[j] or not ascendente and lista_temp[i] < lista_temp[j] :
                aux = lista_temp[i]
                lista_temp[i] = lista_temp[j] 
                lista_temp[j] = aux
    lista_temp = ",".join(lista_temp)
    print(lista_temp)
    return(lista_temp)
ordenar_az("hola", ascendente=True)