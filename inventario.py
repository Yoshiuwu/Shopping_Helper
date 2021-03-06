import json
import producto
import csv
import copy
import sys

class Inventario:
	def __init__(self, nombreArchivo):
		self._nombreArchivo = nombreArchivo
		self._listaProductos = []

		try:
			file = open(nombreArchivo, 'r')
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
		except FileNotFoundError:
			jsonArray = ({'productos':[]}) 
			jsonString = json.dumps(jsonArray, indent=4)
			jsonFile = open(nombreArchivo, "w")
			jsonFile.write(jsonString)
			jsonFile.close()

	def getInventarioRecortado(self, listaSeleccion):
		lista = copy.deepcopy(self._listaProductos)
		indicesARemover=[]

		for i in range(len(lista)):
			siEsta = False
			for pNombre in listaSeleccion:
				if pNombre == lista[i]._nombre:
					siEsta = True
			if not siEsta:
				indicesARemover.append(i)
		k=0
		for i in indicesARemover:
			del lista[i-k]
			k = k+1
		return lista


	def appendProducto(self, nombre, precio, cantidad, esLiquido, marca, calificacion):
		productoObj = producto.Producto(nombre, precio, cantidad, esLiquido, marca, calificacion)
		if not self.checkDuplicate(productoObj):
			self._listaProductos.append(productoObj)
			return True
		return False

	def getPrecioMinimoDeUnaSeleccion(self, listaSeleccion):
		minimo = sys.float_info.max
		for p in self._listaProductos:
			for nombreProductoListaSeleccion in listaSeleccion:
				if p._nombre == nombreProductoListaSeleccion and p._precio < minimo:
					minimo = p._precio
		return minimo

	def checkDuplicate(self, productoAChecar):
		for i in range(len(self._listaProductos)):
			if self._listaProductos[i]._nombre.lower() == productoAChecar._nombre.lower() and self._listaProductos[i]._marca.lower() == productoAChecar._marca.lower() and self._listaProductos[i]._cantidad == productoAChecar._cantidad:
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
		contadorDeElementosErroneos = 0
		for i in range(1, len(data)):
			try:
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
			except ValueError:
				contadorDeElementosErroneos = contadorDeElementosErroneos + 1
		if contadorDeElementosErroneos:
			print("Hay "+ str(contadorDeElementosErroneos) +" Elementos con campos errones.\n")
		

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
			json.dump(data, file, indent = 4)

	
