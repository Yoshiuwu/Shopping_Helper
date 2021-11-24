import json
import producto

class Inventario:
	def __init__(self, nombreArchivo):
		self._listaProductos = []

		with open(nombreArchivo) as file:
			data = json.load(file)

		for productData in data['products']:
			productoxd = producto.Producto(
				productData['Nombre'],
				productData['Precio'],
				productData['Cantidad'],
				productData['EsLiquido'],
				productData['Marca'],
				productData['Calificacion'],
			)
			print(productoxd.toJSON())
	
