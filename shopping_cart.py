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

    def formulaSatisfaccion(self, totalPrecio, totalCalificaciones, cantidadDeGramosPorCadaPeso, cantidadDeProductosTomados, banderaProductoNoDeseado, productosYaTomados):
        satisfaccion = (10000 * cantidadDeProductosTomados) / (len(self._listaSeleccion))#Si tomo todos los items te da 10000 puntos
        if (cantidadDeProductosTomados > 0):
            satisfaccion = satisfaccion + (((self._dinero - totalPrecio) * cantidadDeGramosPorCadaPeso) * (totalCalificaciones / cantidadDeProductosTomados))*.01 #Entre mayor sea la diferencia entre el dinero max y el propuesto por la solucion, es mejor
        if productosYaTomados: 
            satisfaccion = satisfaccion / (5*(productosYaTomados))
        if totalPrecio <= 0 or banderaProductoNoDeseado:
            satisfaccion = 0
        return satisfaccion
        
    def f(self, cromosoma):
        total = 0
        totalCalificaciones = 0
        cantidadDeGramosPorCadaPeso = 0
        productoNoDeseado = False
        productosYaTomados = 0
        listaSeleccionados = []
        for i in range(len(cromosoma)):
            if cromosoma[i]:
                total = total + self._inventario[i]._precio
                totalCalificaciones = totalCalificaciones + self._inventario[i]._calificacion
                cantidadDeGramosPorCadaPeso = cantidadDeGramosPorCadaPeso + ( self._inventario[i]._cantidad / self._inventario[i]._precio )
                if  total  > self._dinero:
                    break
                if self.estaEnLaLista(self._inventario[i]) and self.noASidoTomado(self._inventario[i],listaSeleccionados):
                    listaSeleccionados.append(self._inventario[i]._nombre)
                elif self.estaEnLaLista(self._inventario[i]) and not self.noASidoTomado(self._inventario[i],listaSeleccionados):
                    productosYaTomados = productosYaTomados + 1
                else:
                    productoNoDeseado = True

        return self.formulaSatisfaccion(total, totalCalificaciones, cantidadDeGramosPorCadaPeso,len(listaSeleccionados), productoNoDeseado, productosYaTomados)

