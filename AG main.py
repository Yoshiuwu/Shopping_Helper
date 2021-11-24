import shopping_cart
import AG
import json
import inventario

def main():
    inventario_actual = inventario.Inventario('data.json')

    mochila = shopping_cart.Shopping_Cart(inventario_actual, 100)
    #prod = producto.Producto('Salchicha',5,1000,False,'Corona',5)
    #print(prod.toJSON())

    # ag = AG.AG(30, len(inventario_actual._listaProductos), 1, 1200, 0.01, mochila)
    #ag.run()
    print("Hola")

if __name__ == '__main__':
    main()
'''
    data = {}
    data['clients'] = []
    data['clients'].append({
        'Nombre': 'Salchica',
        'Precio': 40,
        'Cantidad': 1000, #Son gramos o mililitros
        'esLiquido': False,
        'Marca': 'Corona',
        'calificacion': 1,
        
    })

    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
'''
