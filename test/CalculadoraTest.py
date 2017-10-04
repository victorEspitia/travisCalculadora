##
import unittest
from Calculadora import Calculadora
class CalculadoraTest(unittest.TestCase):

	def setUp(self):
		self.cal = Calculadora()

	def test_suma_prueba1(self):
		self.cal.suma(3,4)
		self.assertEquals(self.cal.obtener_resultado(), 7)

	def test_suma_prueba2(self):
		self.cal.suma(100,20)
		self.assertEquals(self.cal.obtener_resultado(), 120)

	def test_suma_prueba3(self):
		self.cal.suma(1000,1000)
		self.assertEquals(self.cal.obtener_resultado(), 2000)

	def test_resta_prueba1(self):
		self.cal.resta(1000,400)
		self.assertEquals(self.cal.obtener_resultado(), 600)

	def test_resta_prueba2(self):
		self.cal.resta(87,3)
		self.assertEquals(self.cal.obtener_resultado(), 84)

	def test_resta_prueba3(self):
		self.cal.resta(10,7)
		self.assertEquals(self.cal.obtener_resultado(), 3)

	def test_multiplicacion_prueba1(self):
		self.cal.multiplicaion(10,7)
		self.assertEquals(self.cal.obtener_resultado(), 70)

	def test_multiplicacion_prueba2(self):
		self.cal.multiplicaion(4,4)
		self.assertEquals(self.cal.obtener_resultado(), 16)

	def test_multiplicacion_prueba3(self):
		self.cal.multiplicaion(90,100)
		self.assertEquals(self.cal.obtener_resultado(), 9000)

	def test_division_prueba1(self):
		self.cal.division(95,5)
		self.assertEquals(self.cal.obtener_resultado(), 19)

	def test_division_prueba2(self):
		self.cal.division(1312,4)
		self.assertEquals(self.cal.obtener_resultado(), 328)

	def test_division_prueba3(self):
		self.cal.division(801,28)
		self.assertEquals(self.cal.obtener_resultado(), 28)

	def test_potencia_prueba1(self):
		self.cal.potencia(4, 2)
		self.assertEquals(self.cal.obtener_resultado(), 16)

	def test_potencia_prueba2(self):
		self.cal.potencia(4, 4)
		self.assertEquals(self.cal.obtener_resultado(), 256)

	def test_potencia_prueba3(self):
		self.cal.potencia(25, 5)
		self.assertEquals(self.cal.obtener_resultado(), 9765625)

	def test_raiz_prueba1(self):
		self.cal.raiz(16)
		self.assertEquals(self.cal.obtener_resultado(), 4)

	def test_raiz_prueba2(self):
		self.cal.raiz(81)
		self.assertEquals(self.cal.obtener_resultado(), 9)

	def test_raiz_prueba3(self):
		self.cal.raiz(9)
		self.assertEquals(self.cal.obtener_resultado(), 3)

if __name__ == '__main__': # pragma: no cover
	unittest.main()
