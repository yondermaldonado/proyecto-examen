import json
def menuPrincipal():
    print("---------------------------------------")
    print("SISTEMA DE FACRURACION RESTAURANTE ACME")
    print("1. Menu productos")
    print("2. Menu mesas")
    print("3. Menu clientes")
    print("4. Crear factura")
    print("5. Registro de ventas")
    print("6. Salir")
    print("---------------------------------------")
    
def menuProductos():
    print("---------------------------------------")
    print("MENU PRODUCTOS")
    print("1. registrar producto")
    print("2. ver productos")
    print("3. Salir")
    print("---------------------------------------")
    
def menuMesas():
    print("---------------------------------------")
    print("MENU MESAS")
    print("1. registrar mesas")
    print("2. ver mesas")
    print("3. Salir")
    print("---------------------------------------")
    
def menuClientes():
    print("---------------------------------------")
    print("MENU CLIENTES")
    print("1. registrar clientes")
    print("2. ver clientes")
    print("3. Salir")
    print("---------------------------------------")

def leerArchivo(ruta):
    try:
        with open(ruta,"r")as file:
            return json.load(file)
    except Exception:
        return []
    
def guardarArchivo(ruta,datos):
    with open(ruta,"w")as file:
        json.dump(datos,file,indent=4)
    

def registrarProductos(listaProductos):
    diccionarioProductos = {
        "codigo":input("digite codigo: "),
        "nombre":input("digite nombre: "),
        "precio":input("digite precio: "),
        "iva":input("digite iva: ")
    }
    listaProductos.append(diccionarioProductos)
    guardarArchivo("productos.json",listaProductos)
    return listaProductos
    
def registrarMesas(listaMesas):
    diccionarioMesas = {
        "codigo":input("digite codigo: "),
        "nombre":input("digite nombre: "),
        "puestos":input("digite puestos: "),
    }
    listaMesas.append(diccionarioMesas)
    guardarArchivo("mesas.json",listaMesas)
    return listaMesas