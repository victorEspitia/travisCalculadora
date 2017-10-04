Feature: Potencia de dos numeros
	Como usuario de la calculadora
	puedo elevar un numero a cierta potencia
	y obtener el resultado.

	Scenario: Potencia de 3 a la 3
		Dado los numeros para la potencia "3" a la "3"
		cuando realizo la operacion
		el resultado de la potencia es "27"

    Scenario: Potencia de 10 a la 3
		Dado los numeros para la potencia "10" a la "3"
		cuando realizo la operacion
		el resultado de la potencia es "1000"

    Scenario: Potencia de 65 a la 3
		Dado los numeros para la potencia "65" a la "3"
		cuando realizo la operacion
		el resultado de la potencia es "274625"