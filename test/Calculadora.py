import math
class Calculadora(object):
	def __init__(self):
		self.resultado = 0

	def suma(self, num1, num2):
		self.resultado = (num1 + num2)

	def resta(self, num1, num2):
		self.resultado = (num1 - num2)

	def multiplicaion(self, num1, num2):
		self.resultado = (num1 * num2)

	def division(self, num1, num2):
		self.resultado = (num1 / num2)

	def potencia(self, num1, num2):
		self.resultado = (num1 ** num2)

	def raiz(self, num1):
		self.resultado = math.sqrt(num1)

	def obtener_resultado(self):
		return self.resultado