import shopping_cart
import AG
import inventario
import os
import platform

def clear_console(): 
    if platform.system() == 'Windows':
        return os.system('cls')
    else: 
        return os.system('clear') 

def printMainMenu():
    print("1-Importar desde Excel")
    print("2-Empezar Selección")
    print("3-Agregar Un Producto Manual")
    print("0-Salir")

def option1(inventario_actual):
    nombreDeArchivo = input("Nombre del archivo: ")
    try:
        inventario_actual.fromCSV(nombreDeArchivo)
        input("Importado Satisfactoriamente.\nPresione Enter para continuar...")
    except FileNotFoundError:
        input("No existe un archivo con ese nombre.\nPresione Enter para continuar...")
        


def option2(inventario_actual):
    listaPosiblesProductos = inventario_actual.getListaDeCategorias()
    listaSeleccion = []
    while True:
        for i in range(len(listaPosiblesProductos)):
            print(str(i + 1) + " - " + listaPosiblesProductos[i])
        print("0 - Continuar")
        option = input("Seleccion un producto: ")
        if option == "0":
            break
        else:
            try:
                if int(option) - 1 <= len(listaPosiblesProductos):
                    listaSeleccion.append(listaPosiblesProductos[int(option)-1])
                    listaPosiblesProductos.remove(listaPosiblesProductos[int(option)-1])
                else:
                    print("Opcion No existente")
            except ValueError:
                print("Entrada Invalida")
    while True:
        try:
            dinero = input("Cuanto Dinero planea gastar?: ")
            dineroMinimo = inventario_actual.getPrecioMinimoDeUnaSeleccion(listaSeleccion)
            if float(dinero) >= dineroMinimo:
                break
            else:
                print("Minimo ponle "+ str(dineroMinimo) +".")
        except ValueError:
                print("Entrada Invalida")
            
    input("Seleccion elegida Satisfactoriamente.\nPresione Enter para continuar...")

    empezarBusqueda(inventario_actual, listaSeleccion, float(dinero))

def option3(inventario_actual):
    marca = ""
    nombre = ""
    precio = 0.0
    esLiquido = False
    cantidad = 0
    calificacion = 0
    mensaje = ""
    while True:
        clear_console()
        try:
            marca = input("Marca?")
            nombre = input("Nombre?")
            precio = float(input("Precio?"))
            respuesta = input("Es Liquido o Solido? [1]Liquido [0]Solido: ")
            esLiquido = respuesta.lower() in ['1']
            esSolido = respuesta.lower() in ['0']
            stringSi = ""
            if not esLiquido and not esSolido:
                continue
            if esLiquido:
                stringSi = "mililitros"
            else:
                stringSi = "gramos"
            cantidad = int(input("Cantidad (en "+ stringSi+")? "))
            calificacion = int(input("Calificacion(0-5)? "))
            if calificacion > 5 or calificacion < 0:
                continue
            break
        except ValueError:
            continue
    if inventario_actual.appendProducto(nombre, precio, cantidad, esLiquido, marca, calificacion):
        mensaje = "Producto creado con exito."
    else:
        mensaje = "Producto Repetido."
    input(mensaje + "\nPresione Enter para continuar...")


    

def empezarBusqueda(inventario_actual, listaSeleccion, dinero):
    inventarioRecortado = inventario_actual.getInventarioRecortado(listaSeleccion)

    carrito = shopping_cart.Shopping_Cart(inventarioRecortado, listaSeleccion, dinero)
    indiceActivos = 0

    ag = AG.AG(60, len(inventarioRecortado), 1, 100*(len(inventarioRecortado)), 0.01, carrito)
    mejorSolucion = ag.run()

    print("Objetos seleccionados:")
    with open('lista.txt', 'w') as f:
        for i in range(len(mejorSolucion)):
            if mejorSolucion[i]:
                productoActual = inventarioRecortado[i]
                cantidad = ""
                if productoActual._cantidad >= 1000:
                    cantidad = cantidad + str(productoActual._cantidad / 1000)
                    if productoActual._esLiquido:
                        cantidad = cantidad + " L"
                    else:
                        cantidad = cantidad + " Kg"
                else:
                    cantidad = cantidad + str(productoActual._cantidad)
                    if productoActual._esLiquido:
                        cantidad = cantidad + " ml"
                    else:
                        cantidad = cantidad + " gr"
                precio = str(productoActual._precio)
                indiceActivos = indiceActivos + 1
                indiceString = str(indiceActivos)
                string = indiceString + " - " + productoActual._nombre + " " + productoActual._marca + " " + cantidad + " $" + precio
                print(string)
                f.write( string+ "\n" )

    input("Encontrado.\nPresione Enter para continuar...")

    return 0

def main():
    inventario_actual = inventario.Inventario('data.json')
    
    while True:
        clear_console()
        printMainMenu()
        option = input("Selecciona una opción: ")

        if option == "1":
            option1(inventario_actual)
        elif option == "2":
            option2(inventario_actual)
        elif option == "3":
            option3(inventario_actual)
        elif option == "0":
            return 0

if __name__ == '__main__':
    main()
