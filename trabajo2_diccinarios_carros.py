carros = {'xtw-123': {
    'Propietario': 'Jose perales', 'Referencia': 'Mazda 3', 'Modelo': 2011, 'marca': 'Mazda', 'Valor': 14222,
    'Ventas': {
        'Fecha': '12-12-2011', 'valor': 222222, 'cliente': 'Juanito'}
},

    'mtr-981': {
        'Propietario': 'Andres Figueroa', 'Referencia': 'Ferrari', 'Modelo': 2019, 'marca': 'Ferrari x100',
        'Valor': 91812,
        'Ventas': {
            'Fecha': '12-12-2019', 'valor': 922222, 'cliente': 'Elmo'}
    },

    'rw-983': {
        'Propietario': 'Yan Mioko', 'Referencia': 'Chevrolet tucano', 'Modelo': 1993, 'marca': 'Danz', 'Valor': 102222,
        'Ventas': {
            'Fecha': '12-12-2011', 'valor': 10191910, 'cliente': 'Eltiorico'}
    },
    'tqw-103': {
        'Propietario': 'toluca nitoma', 'Referencia': 'Mazerati 12', 'Modelo': 2014, 'marca': 'Maseratti',
        'Valor': 12578,
        'Ventas': {
            'Fecha': '19-05-2016', 'valor': 112092, 'cliente': 'Alejandro'}
    }

}

def listarAutos():
    for i in carros:
        print("Auto de placa : ", i, "   ")
        print(carros[i])
        print("\n")


def añadirAuto():
    placa = input("Nombre de la placa: ")
    confir = False
    for i in carros:
        # print(i)
        if i == placa:
            confir = True

    if confir == False:
        nombre_dueño = input("Digite el nombre del dueño: ")
        Referencia = input("Digite la referencia del auto: ")
        Modelo = input("Digite el modelo del auto: ")
        marca = input("Digite la marca del auto: ")
        valor = input("Digite el valor del auto: ")

        carros[placa] = {'Propietario': nombre_dueño, 'Referencia': Referencia, 'Modelo': Modelo, 'marca': marca,
                         'valor': valor, 'Ventas': ''}

    else:

        print("Pri ya existe el auto")

def buscarAuto():
    placa_auto = input("Digite la placa del auto: ")
    confirmar = False
    info = carros.get(placa_auto)
    if info != None:
        print(info)
        return info
    else:
        print("No existe el auto con esa placa")
        return info
    print()

def añadirVenta():
    placa_auto = input("Digite la placa del auto: ")
    confir = False
    lista = []
    for i in carros:

        if i == placa_auto:
            confir = True
    if confir == True:

        ventas = carros[placa_auto]['Ventas']
        if len(ventas) > 0:
            lista.append(ventas)

        fecha = input("Digite la fecha de venta: ")
        valor = input("Digite el valor del auto: ")
        cliente = input("Digite el nuevo dueño del auto: ")
        updateVentas = {'Fecha': fecha, 'valor': valor, 'cliente': cliente}
        lista.append(updateVentas)
        carros[placa_auto]['Ventas'] = lista
    else:
        print("No existe ese carro")
        

def modificarVenta():
    placa_auto = input("Digite la placa del auto: ")
    confir = False
    lista = []
    
    for i in carros:
        if i == placa_auto:
            confir = True
            break
            
    if confir == True:

        if len(carros[placa_auto]['Ventas']) > 0:
            ## Guargar ventas en lista ya sea una venta o mas de una
            ## Si es mas de una venta, las guarda como tuplas distintas
            try:
                pos = 0
                while pos < len(carros[placa_auto]['Ventas']):
                    lista.append(carros[placa_auto]['Ventas'][pos])
                    pos += 1
            except:
                lista.append(carros[placa_auto]['Ventas'])

            ## Imprimo las ventas con placas suministrada

            opc = 0
            while True:
                cont = 0
                for j in lista:
                    print (cont+1, j)
                    print ('\n')
                    cont += 1
                opc = input("Digite una opcion de la venta a modificar: ")
                if opc.isdigit() == True:
                    if int(opc) > 0 and int(opc) <= len(lista):
                        break

            print('\n')
            valor = input("Digite el nuevo valor de la venta: ")
            ##Creacion directorio con nueva venta
            
            venta = lista[int(opc)-1]
            ventaActualizada = {'valor':valor}
            venta.update(ventaActualizada)
            lista[int(opc)-1] = venta

            ##se sobreescribe ventas
            carros[placa_auto]['Ventas'] = lista

        else:
            print("Ese carro no tiene ventas disponibles")

    else:
        print("No existe ese carro")


def eliminarVenta():
    placa_auto = input("Digite la placa del auto: ")
    confir = False
    lista = []
    
    for i in carros:
        if i == placa_auto:
            confir = True
            break
            
    if confir == True:

        if len(carros[placa_auto]['Ventas']) > 0:
            ## Guargar ventas en lista ya sea una venta o mas de una
            ## Si es mas de una venta, las guarda como tuplas distintas
            try:
                pos = 0
                while pos < len(carros[placa_auto]['Ventas']):
                    lista.append(carros[placa_auto]['Ventas'][pos])
                    pos += 1
            except:
                lista.append(carros[placa_auto]['Ventas'])

            ## Imprimo las ventas con placas suministrada

            opc = 0
            while True:
                cont = 0
                for j in lista:
                    print (cont+1, j)
                    print ('\n')
                    cont += 1
                opc = input("Digite una opcion de la venta que desea eliminar: ")
                if opc.isdigit() == True:
                    if int(opc) > 0 and int(opc) <= len(lista):
                        break
                    
            ##Se borra de la lista de ventas, la seleccionada por
            ##el usuario

            lista.pop(int(opc)-1)

            ##se sobreescribe ventas
            carros[placa_auto]['Ventas'] = lista

        else:
            print("Ese carro no tiene ventas disponibles")

    else:
        print("No existe ese carro")
        

def eliminarAuto():
    placa_auto = input("Digite la placa del auto: ")
    confir = False
    for i in carros:
        if i == placa_auto:
            confir = True
    if confir == True:
        elim = carros.pop(placa_auto)
    else:
        print("No existe esa placa")


opc = 0
while opc != 10:
    if opc == 1:  ## añadir auto
        print()
        añadirAuto()
        
    if opc == 2:  ## buscar auto
        print()
        buscarAuto()

    if opc == 3:  ## modificar auto
        print()
        pass

    if opc == 4:  ## eliminar auto
        print()
        eliminarAuto()

    if opc == 5:  ## añadir venta
        print()
        añadirVenta()

    if opc == 6:  ## modificar venta
        print()
        modificarVenta()

    if opc == 7:  ## eliminar venta
        print()
        eliminarVenta()

    if opc == 8:  ## mostrar ventas
        print()
        pass

    if opc == 9:  # mostrar autos
        listarAutos()
        
    print("-------------------------------------------------------------")
    print("1. Añadir auto")
    print("2. buscar auto")
    print("3. modificar auto")
    print("4. eliminar auto")
    print("5. Añadir venta")
    print("6. Modificar venta")
    print("7. Eliminar venta")
    print("8. Listar ventas")
    print("9. Listar todo los autos")
    print("10. Salir")
    print("-------------------------------------------------------------")

    opc = input("Digite una opcion: ")
    if opc.isdigit() == True:
        opc = int(opc)

"""
4..poder listar la ventas que ha tenido un vehiculo especifico
5..poder modificar los datos del vehiculo
"""
