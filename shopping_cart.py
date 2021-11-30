import sys

class Shopping_Cart:
    def __init__(self, inventario, listaSeleccion, dinero):
        self._inventario = inventario
        self._dinero = dinero
        self._listaSeleccion = listaSeleccion
        self._listaSeleccionados = []

    def estaEnLaLista(self, producto):
        for p in self._listaSeleccion:
            if producto._nombre == p:
                self._listaSeleccionados.append(p)
                self._listaSeleccion.remove(p)
                return True
        return False

    def yaFueTomado(self, producto):
        for p in self._listaSeleccionados:
            if p == producto._nombre:
                return True
        return False

    def formulaSatisfaccion(self, totalPrecio, totalCantidadFaltante, banderaProductoNoDeseado):
        satisfaccion = totalCantidadFaltante * 10
        satisfaccion = satisfaccion + (totalPrecio * 2)
        if totalPrecio <= 0:
            satisfaccion = satisfaccion ** 10

        if banderaProductoNoDeseado:
            satisfaccion = 1000 ** 10
        print(satisfaccion)
        return satisfaccion

        ## Convertir todo a maximizacion esta minificado todo

        
    def f(self, cromosoma):
        total = self._dinero
        productoNoDeseado = False
        for i in range(len(cromosoma)):
            if cromosoma[i]:
                if self.estaEnLaLista(self._inventario._listaProductos[i]):
                    total = total - self._inventario._listaProductos[i]._precio
                    if  total  <= 0:
                        break
                elif self.yaFueTomado(self._inventario._listaProductos[i]):
                    #verificar Si es mejor a la seleccion anterior
                    break
                else:
                    productoNoDeseado = True

        return self.formulaSatisfaccion(total, len(self._listaSeleccion), productoNoDeseado)

