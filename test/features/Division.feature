Feature: Division de dos numeros
	Como usuario de la calculadora
	puedo dividir dos numeros
	y obtener el resultado.

	Scenario: Division de 2 entre 2
		Dado los numeros para la division "2" y "2"
		cuando realizo la operacion
		el resultado de la division es "1"

	Scenario: Division de 0 entre 9
		Dado los numeros para la division "0" y "9"
		cuando realizo la operacion
	    el resultado de la division es "0"

    Scenario: Division de 9 entre 3
		Dado los numeros para la division "9" y "3"
		cuando realizo la operacion
		el resultado de la division es "3"