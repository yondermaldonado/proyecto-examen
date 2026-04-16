import funciones
import datetime

listaProductos=funciones.leerArchivo("productos.json")
listaMesas=funciones.leerArchivo("mesas.json")
listaClientes=funciones.leerArchivo("clientes.json")

while True:
    funciones.menuPrincipal()
    opcionPrincipal = input("Digite la opcion: ")
    print("---------------------------------------")

    if opcionPrincipal == "1":
        while True:
            funciones.menuProductos()
            opcionProductos = int(input("Digite la opcion: "))
            print("---------------------------------------")
            if(opcionProductos==1):
                listaProductos = funciones.registrarProductos(listaProductos)
                    
            elif(opcionProductos==2):
                for producto in listaProductos:
                    print(producto)
            elif(opcionProductos==3):
                "saliendo...."
                break

    elif opcionPrincipal == "2":
         while True:
            funciones.menuMesas()
            opcionMesas = int(input("Digite la opcion: "))
            print("---------------------------------------")
            if(opcionMesas==1):
                funciones.registrarMesas(listaMesas)
                    
            elif(opcionMesas==2):
                for mesas in listaMesas:
                    print(mesas)
            elif(opcionMesas==3):
                "saliendo...."
                break
    
    elif opcionPrincipal == "3":
        while True:
            funciones.menuClientes()
            opcionClientes = int(input("Digite la opcion: "))
            print("---------------------------------------")
            if(opcionClientes==1):
                diccionarioClientes= {
                    "identificacion":input("digite identificacion: "),
                    "nombre":input("digite nombre: "),
                    "telefono":input("digite telefono: ")
                }
                listaClientes.append(diccionarioClientes)
                funciones.guardarArchivo("clientes.json",listaClientes)
                    
            elif(opcionClientes==2):
                for clientes in listaClientes:
                    print(clientes)
            elif(opcionClientes==3):
                "saliendo...."
                break
    elif opcionPrincipal == "4":
        listaFactura=[]
        listaProductosFactura = []
        print("facturacion")
        codigoMesa= input("digite codigo de la mesa: ")
        cliente= input("digite identificacion del cliente: ")
        
        while True:
            codigoProducto= input("digite codigo del producto: ")
            for producto in listaProductos:
                if(producto["codigo"]==codigoProducto):
                    cantidad= input("digite cantidad")
                    productoFactura= {
                        "codigo": codigoProducto,
                        "cantidad": cantidad
                    }
                    listaProductosFactura.append(productoFactura)
            opcionFactura= input("quieres agregar mas productos s/n: ")
            if(opcionFactura=="n"):
                break
        
        diccionarioFactura={
            "fecha": datetime.datetime.now().strftime("%Y-%m-%d"),
            "cliente": cliente,
            "codigoMesa": codigoMesa,
            "productos": listaProductosFactura
        }
        listaFactura.append(diccionarioFactura)
        funciones.guardarArchivo("factura.json",listaFactura)
    elif opcionPrincipal == "6":
        print("Saliendo del sistema...")
        break
    else:
        print("Opcion no valida")
