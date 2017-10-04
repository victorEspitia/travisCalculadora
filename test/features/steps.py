# -*- coding: utf-8 -*-
from lettuce import step, world
from Calculadora import Calculadora

@step(u'cuando realizo la operacion')
def cuando_realizo_la_operacion(step):
    pass

# Calcular Suma
@step(u'Dado los numeros para la suma "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.suma(int(num1), int(num2))
@step(u'el resultado de la suma es "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    obtenido = world.cal.obtener_resultado()
    assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

#Calcular Resta
@step(u'Dado los numeros para la resta "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.resta(int(num1), int(num2))
@step(u'el resultado de la resta es "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    obtenido = world.cal.obtener_resultado()
    assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

# Calcular Multiplicacion
@step(u'Dado los numeros para la multiplicacion "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.multiplicaion(int(num1), int(num2))
@step(u'el resultado de la multiplicacion es "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    obtenido = world.cal.obtener_resultado()
    assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

# Calcular Division
@step(u'Dado los numeros para la division "([^"]*)" y "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.division(int(num1), int(num2))
@step(u'el resultado de la division es "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    obtenido = world.cal.obtener_resultado()
    assert int(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

# Calcular Potencia
@step(u'Dado los numeros para la potencia "([^"]*)" a la "([^"]*)"')
def dado_que_ingreso_los_numeros_group1_y_group2(step, num1, num2):
    world.cal = Calculadora()
    world.cal.potencia(int(num1), int(num2))
@step(u'el resultado de la potencia es "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    obtenido = float(world.cal.obtener_resultado())
    assert float(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)

# Calcular Raiz
@step(u'Dado el numero para la raiz "([^"]*)"')
def dado_que_ingreso_el_numero_group1(step, num1):
    world.cal = Calculadora()
    world.cal.raiz(int(num1))
@step(u'el resultado de la raiz es "([^"]*)"')
def entonces_obtengo_el_resultado_group1(step, esperado):
    obtenido = float(world.cal.obtener_resultado())
    assert float(esperado) == obtenido,'El resultado esperado de '+esperado+" y el obtenido es "+str(obtenido)