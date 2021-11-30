import json
import producto
import csv

class Inventario:
	def __init__(self, nombreArchivo):
		self._nombreArchivo = nombreArchivo
		self._listaProductos = []

		with open(nombreArchivo) as file:
			data = json.load(file)

		for productData in data['productos']:
			productoObj = producto.Producto(
				productData['Nombre'],
				productData['Precio'],
				productData['Cantidad'],
				productData['EsLiquido'],
				productData['Marca'],
				productData['Calificacion'],
			)
			if not self.checkDuplicate(productoObj):
				self._listaProductos.append(productoObj)

		

	def checkDuplicate(self, productoAChecar):
		for i in range(len(self._listaProductos)):
			if self._listaProductos[i]._nombre == productoAChecar._nombre and self._listaProductos[i]._marca == productoAChecar._marca:
				return True
		return False
				
	def getListaDeCategorias(self):
		Lista = []
		for i in range(len(self._listaProductos)):
			Lista.append(self._listaProductos[i]._nombre)
		return list(set(Lista))
 
	def fromCSV(self, nombreArchivoCSV):
		with open(nombreArchivoCSV, newline='') as f:
			reader = csv.reader(f)
			data = list(reader)
		for i in range(1, len(data)):
			productoObj = producto.Producto(
				data[i][0],
				float(data[i][1]),
				int(data[i][2]),
				data[i][3].lower() in ['True','true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh'],
				data[i][4],
				int(data[i][5]),
			)
			if not self.checkDuplicate(productoObj):
				self._listaProductos.append(productoObj)

	def __del__(self):
		data = {}
		data['productos'] = []
		for productoObj in self._listaProductos:
			data['productos'].append({
					'Nombre': productoObj._nombre,
					'Precio': productoObj._precio,
					'Cantidad': productoObj._cantidad, #Son gramos o mililitros
					'EsLiquido': productoObj._esLiquido,
					'Marca': productoObj._marca,
					'Calificacion': productoObj._calificacion,
			})

		with open(self._nombreArchivo , 'w') as file:
			json.dump(data, file, indent=4)

	
