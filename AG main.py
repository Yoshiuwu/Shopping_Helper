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
        print("0 - Salir")
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
            float(dinero)
            if float(dinero) >= 50: #Buscar el precio minimo de un producto y agregar el agregar un producto por consola
                break
            else:
                print("Minimo ponle 50 enfermo.")
        except ValueError:
                print("Entrada Invalida")
            
    input("Seleccion elegida Satisfactoriamente.\nPresione Enter para continuar...")

    empezarBusqueda(inventario_actual, listaSeleccion, float(dinero))


def empezarBusqueda(inventario_actual, listaSeleccion, dinero):
    carrito = shopping_cart.Shopping_Cart(inventario_actual, listaSeleccion, dinero)
    indiceActivos = 0

    ag = AG.AG(50, len(inventario_actual._listaProductos), 1, 1000, 0.01, carrito)
    mejorSolucion = ag.run()

    print("Objetos seleccionados:")
    with open('lista.txt', 'w') as f:
        for i in range(len(mejorSolucion)):
            if mejorSolucion[i]:
                productoActual = inventario_actual._listaProductos[i]
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
        elif option == "0":
            return 0

if __name__ == '__main__':
    main()
