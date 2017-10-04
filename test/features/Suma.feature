Feature: Suma de dos numeros
	Como usuario de la calculadora
	puedo sumar dos numeros
	y obtener el resultado.

	Scenario: Suma de 3 mas 2
		Dado los numeros para la suma "3" y "2"
		cuando realizo la operacion
		el resultado de la suma es "5"

	Scenario: Suma de 3300 mas 200
		Dado los numeros para la suma "3300" y "200"
		cuando realizo la operacion
		el resultado de la suma es "3500"

	Scenario: Suma de 8 mas 25
		Dado los numeros para la suma "8" y "25"
		cuando realizo la operacion
		el resultado de la suma es "33"