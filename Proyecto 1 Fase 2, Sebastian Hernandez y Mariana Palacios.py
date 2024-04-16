#Proyecto No. 1 Fase 2
# Mariana Palacios Castillo 1127124
#Sebastian Hernandez Grijalva 1321724

nombre = input("Ingrese su nombre: ")
NIT = input("Ingrese su numero de NIT (en dado caso no desee ingrese CF): ")

costo = 20.00
costoazucar = 0
costosinleche = -2.00
costolechedeslactosada = 0.00
costolecheentera = 0.00
costolechesoya = 3.00
costoagrandado = 0.05
total1 = 0
total2 = 0
total3 = 0
total4 = 0

cuchazucar = 0
tipoleche = "Leche Deslactosada"
tamaño = "normal"
agrandado = False

total = 0





while True:
    print ("Menu ")
    print ("Opc.1 Ver informacion del pedido")
    print ("Opc.2 Agregar azucar")
    print ("Opc.3 Modificar la leche")
    print ("Opc.4 Agrandar el licuado")
    print ("Opc.5 Confirmar pedido ")
    opc = input("Ingrese el numero de la opcion que desee: ")

    if opc == "1":
        print("Informacion del Pedido")
        print("Cliente:", nombre)
        print("NIT:", NIT)
        print("Licuado de Fresa con",tipoleche,"con",cuchazucar,"cucharadas de azucar de tamaño",tamaño,".")
        total = costo + total1 + total2 + total3
        if agrandado:
            total = total * 1.05
        else:
            total = total
        print("Su precio es de Q.", total)

    elif opc == "2":
        azuc = input("¿Desea agregar azucar? (Si o No): ")
        if azuc == "Si":
            cuchazucar = int(input("Ingrese la cantidad de cucharadas de azucar que desee agregar: "))
            if cuchazucar <= 2:
                total2 = cuchazucar * 0.50
            else:
                print ("No se puede agregar mas de dos cucharadas de azucar")
                cuchazucar = 0
                
        else:
            total2 = costoazucar


    elif opc == "3":
        print("Opciones de leche en el licuado")
        print("1. Sin Leche")
        print("2. Leche Deslactosada")
        print("3. Leche Entera")
        print("4. Leche de Soya")

        tipo = input("Ingrese el numero de opcion de leche que desee: ")

        if tipo == "1":
            tipoleche = "Agua"
            total3 = costosinleche
        
        elif tipo == "2":
            tipoleche = "Leche Deslactosada"
            total3 = costolechedeslactosada
        
        elif tipo == "3":
            tipoleche = "Leche Entera"
            total3 = costolecheentera

        elif tipo == "4":
            tipoleche = "Leche de soya"
            total3 = costolechesoya 
        else:
            print("Opcion invalida")

    elif opc == "4":
        agrandado = input("Desea agrandar su pedido (Si o No): ")
        if agrandado == "Si":
            tamaño = "grande"
            agrandado = True
        else:
            tamaño = "nomal"
            agrandado = False

    elif opc == "5":
        total = costo + total1 + total2 + total3
        if agrandado:
            total = total * 1.05
        else:
            total = total
        print("Detalles del pedido")
        print("Nombre: ", nombre)
        print("NIT: ", NIT)
        print("Licuado de Fresa con",tipoleche,"con",cuchazucar,"cucharadas de azucar de tamaño",tamaño,".") 
        print("Su total a pagar es Q.", total)
        break
    else:
        print("Escoger opcion valida")