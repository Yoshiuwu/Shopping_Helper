class Shopping_Cart:
    def __init__(self, inventario, dinero):
        self._inventario = inventario
        self._dinero = dinero

    def f(self, cromosoma):
        total = 0
        for i in range(len(cromosoma)):
            if cromosoma[i]:
                total = total + self._inventario[i]
                if  total > self._dinero:
                    total = total - (self._inventario[i])*2
                    break
        if total < 0:
            total = 0
        return total
