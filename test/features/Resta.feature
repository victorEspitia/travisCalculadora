Feature: Resta de dos numeros
	Como usuario de la calculadora
	puedo restar dos numeros
	y obtener el resultado.

	Scenario: Resta de 2 menos 2
		Dado los numeros para la resta "2" y "2"
		cuando realizo la operacion
		el resultado de la resta es "0"

	Scenario: Resta de 7 menos 5
		Dado los numeros para la resta "7" y "5"
		cuando realizo la operacion
		el resultado de la resta es "2"

	Scenario: Resta de 1000 menos 100
		Dado los numeros para la resta "1000" y "100"
		cuando realizo la operacion
		el resultado de la resta es "900"