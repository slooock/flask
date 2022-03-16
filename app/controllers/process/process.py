import numpy as np

def processPost(facts = [
        ('gabriel', 'endereço', 'av rio branco, 109', True),
        ('joão', 'endereço', 'rua alice, 10', True),
        ('joão', 'endereço', 'rua bob, 88', True),
        ('joão', 'telefone', '234-5678', True),
        ('joão', 'telefone', '91234-5555', True),
        ('joão', 'telefone', '234-5678', False),
        ('gabriel', 'telefone', '98888-1111', True),
        ('gabriel', 'telefone', '56789-1010', True),
    ]):
    # resultado = np.array([])

    resultado = [[None,None,None,None]]

    schema = np.array([
        ('endereço', 'cardinality', 'one'),
        ('telefone', 'cardinality', 'many')
    ])

    arr = np.array(facts)

    test = arr[:,[3]].tolist()
    test = np.reshape(test, (1,len(test)))
    test = test == 'False'
    test = test.tolist()[0]
    listFalse = arr[test]

    if len(listFalse) != 0:
    #Retirando itens false
        arrTemp = arr
        for lf in listFalse:
            listBoolTemp = arrTemp == lf
            arrAux = np.array([], dtype=bool);
            for item in listBoolTemp:
                if  False in item[0:3]:
                    arrAux = np.append(arrAux, True)
                else:
                    arrAux = np.append(arrAux, False)

            arrTemp = arrTemp[arrAux]
        arrSemFalse = arrTemp
    else:
        arrSemFalse = arr

    #Definindo atributos e usuários unicos
    atributos = np.unique(arr[:,[1]])
    usuarios = np.unique(arr[:,[0]])

    reshapedBoolean = np.reshape(arr[:,[3]], (1,len(arr)))[0].tolist()
    listFalse = arr[list(map(lambda ele: ele == "False", reshapedBoolean))]

    for atributo in atributos:
        #Filtrando por atributo
        itemAtributo = arrSemFalse[:,[1]] == atributo
        itemAtributoFiltrado = np.reshape(itemAtributo, (1,len(arrSemFalse)))[0].tolist()
        itemAtributoFiltrado = arrSemFalse[itemAtributoFiltrado]

        for usuario in usuarios:

            #Filtrando por usuario
            itemNome = itemAtributoFiltrado[:,[0]] == usuario
            itemNomeFiltrado = np.reshape(itemNome, (1,len(itemNome)))[0].tolist()
            itemNomeFiltrado = itemAtributoFiltrado[itemNomeFiltrado]

            #Verificando cardinalidade se for cardinalidade onediciona o ultimo se for many adiciona todos
            itemSchema = schema[:,[0]] == atributo
            itemSchemaFiltrado = np.reshape(itemSchema, (1,len(schema)))[0].tolist()
            itemSchemaFiltrado = schema[itemSchemaFiltrado][0]
            cardinality = itemSchemaFiltrado[2]
            if cardinality == 'one':
                if len(itemNomeFiltrado) != 0:
                    resultado = np.concatenate((resultado, [itemNomeFiltrado[-1]]), axis = 0)
            elif cardinality == 'many':
                if len(itemNomeFiltrado) != 0:
                    resultado = np.concatenate((resultado, itemNomeFiltrado), axis=0)

    resultado = resultado[1:len(resultado)]

    resultadoTuple = []
    for item in resultado:
    #     resultadoTuple = resultadoTuple.append(tuple(item))
        resultadoTuple.append(tuple(item))

    return resultadoTuple