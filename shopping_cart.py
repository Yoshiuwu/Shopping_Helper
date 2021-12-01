class Shopping_Cart:
    def __init__(self, inventario, listaSeleccion, dinero):
        self._inventario = inventario
        self._dinero = dinero
        self._listaSeleccion = listaSeleccion

    def estaEnLaLista(self, producto):
        for p in self._listaSeleccion:
            if producto._nombre == p:
                return True
        return False

    def noASidoTomado(self, producto, listaSeleccionados):
        for p in listaSeleccionados:
            if p == producto._nombre:
                return False
        return True

    def formulaSatisfaccion(self, totalPrecio, totalCalificaciones, cantidadDeGramosPorCadaPeso, cantidadDeProductosTomados, banderaProductoNoDeseado, banderaProductoYaTomado):
        satisfaccion = (100000 * cantidadDeProductosTomados) / (len(self._listaSeleccion))#Si tomo todos los items te da 1000 puntos
        if (cantidadDeProductosTomados > 0):
            satisfaccion = satisfaccion + (((self._dinero - totalPrecio) * cantidadDeGramosPorCadaPeso) * (totalCalificaciones / cantidadDeProductosTomados)) #Entre mayor sea la diferencia entre el dinero max y el propuesto por la solucion, es mejor
        if banderaProductoYaTomado: 
            satisfaccion = satisfaccion / 2
        if totalPrecio <= 0 or banderaProductoNoDeseado:
            satisfaccion = 0
        return satisfaccion
        
    def f(self, cromosoma):
        total = 0
        totalCalificaciones = 0
        cantidadDeGramosPorCadaPeso = 0
        productoNoDeseado = False
        productoYaTomado = False
        listaSeleccionados = []
        for i in range(len(cromosoma)):
            if cromosoma[i]:
                total = total + self._inventario._listaProductos[i]._precio
                totalCalificaciones = totalCalificaciones + self._inventario._listaProductos[i]._calificacion
                cantidadDeGramosPorCadaPeso = cantidadDeGramosPorCadaPeso + ( self._inventario._listaProductos[i]._cantidad / self._inventario._listaProductos[i]._precio )
                if  total  > self._dinero:
                    break
                if self.estaEnLaLista(self._inventario._listaProductos[i]) and self.noASidoTomado(self._inventario._listaProductos[i],listaSeleccionados):
                    listaSeleccionados.append(self._inventario._listaProductos[i]._nombre)
                elif self.estaEnLaLista(self._inventario._listaProductos[i]) and not self.noASidoTomado(self._inventario._listaProductos[i],listaSeleccionados):
                    productoYaTomado = True
                else:
                    productoNoDeseado = True

        return self.formulaSatisfaccion(total, totalCalificaciones, cantidadDeGramosPorCadaPeso,len(listaSeleccionados), productoNoDeseado, productoYaTomado)

