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
    inventario_actual.fromCSV(nombreDeArchivo)
    input("Importado Satisfactoriamente.\nPresione Enter para continuar...")


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
            listaSeleccion.append(listaPosiblesProductos[int(option)-1])
            listaPosiblesProductos.remove(listaPosiblesProductos[int(option)-1])
    dinero = input("Cuanto Dinero planea gastar?")
            
    input("Seleccion elegida Satisfactoriamente.\nPresione Enter para continuar...")

    empezarBusqueda(inventario_actual, listaSeleccion, float(dinero))


def empezarBusqueda(inventario_actual, listaSeleccion, dinero):
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
            
        carrito = shopping_cart.Shopping_Cart(inventario_actual, 100)

        #prod = producto.Producto('Salchicha',5,1000,False,'Corona',5)
        #print(prod.toJSON())
        # ag = AG.AG(30, len(inventario_actual._listaProductos), 1, 1200, 0.01, mochila)
        #ag.run()



if __name__ == '__main__':
    main()
