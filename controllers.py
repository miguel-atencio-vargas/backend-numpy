from flask_restful import Resource
from flask import request, jsonify
from numpy import *
import pandas as pd
global message


def clean(a):
    aux=[]
    for i in range(len(a)):
        if len(a[i])!=0:
            for j in range(len(a[i])):
                aux.append(a[i][j])
    a_cols = len(a[0])
    a_rows = (len(aux)//a_cols)
    m = [[0]*a_cols for i in range(a_rows)];c=0
    for i in range(a_rows):
        for j in range(a_cols) :
            m[i][j]=aux[c]
            if c+1 < len(aux):c+=1
    return m
def suma(a,b):
    try:
        global message
        message = 'La suma se realizo correctamente:'
        return a+b
    except:
        message = '(Error) Las dimensiones de sus matrices no son iguales shape(a)={} shape(b)={} '.format(shape(a), shape(b))
def resta(a,b):
    try:
        global message
        message = 'La resta se realizo correctamente:'
        return a-b
    except:
        message = '(Error) Las dimensiones de sus matrices no son iguales shape(a)={} shape(b)={} '.format(shape(a), shape(b))
def multiplicacion(a,b):
    try:
        global message 
        message = 'Se realizo la multiplicacion correctamente'
        return a*b
    except:
        message = '(Error) No se cumple la condicion de que las columnas de la matriz A sea igual a las filas de la matriz B. shape(a)={} shape(b)={}'.format(shape(a), shape(b))

def transpuesta(a):
    try:
        global message
        message = 'La transpuesta se resolvio correctamente'
        return a.transpose()
    except: 
        message = '(Error) Ocurrio un error al tratar de encontrar la transpuesta de su matriz'

def diagonall(a):
    try:
        global message
        message = 'La diagonal se resolvio correctamente'
        return diagonal(a)
    except: 
        message = '(Error) Ocurrio un error al tratar de encontrar la diagonal de su matriz'
def inversa(a):
    try:
        global message
        message = 'La inversa se resolvio correctamente'
        return linalg.inv(a)
    except: 
        message = '(Error) Ocurrio un error al tratar de encontrar la inversa de su matriz. Verifique que la matriz sea cuadrada'
def triangular(a, c):
    try:
        global message
        message = 'La triangular se resolvio correctamente'
        if c == 'i': return tril(a)
        else: return triu(a)
    except: 
        message = '(Error) Ocurrio un error al tratar de encontrar la triangular de su matriz. Verifique que la matriz sea cuadrada'
#-------------escalar------------
def determinante(a):
    try:
        global message
        message = 'El determinante se resolvio correctamente'
        return [[linalg.det(a)]]
    except:
        message = '(Error) Ocurrio un error al calcular el determinante. Verifique su matriz enviada' 

def rango(a):
    try:
        global message
        message = 'El rango se resolvio correctamente'
        return [[linalg.matrix_rank(a)]]
    except:
        message = '(Error) Ocurrio un error al calcular el rango. Verifique su matriz enviada' 
def norma(a):
    try:
        global message
        message = 'La norma se resolvio correctamente'
        return [[linalg.norm(a)]]
    except:
        message = '(Error) Ocurrio un error al calcular norma. Verifique su matriz enviada' 
#----------Sistemas Lineales-----------
def lineal(a,b):
    try:
        global message
        message = 'El sistema de ecuaciones se resolvio correctamente'
        
        return linalg.inv(a).dot(b)
    except :
        message = '(Error) Ocurrio un error al resolver el sistema. shape(A)={} shape(B)={} '.format(shape(a), shape(b))

class Employees(Resource):
    def get(self):
        return 'Servicio funcionando :D'

class Operacion(Resource):
    def post(self):
        global message
        if request.method == "POST":
            resp = request.get_json()
            a = matrix(clean(resp['matrix'][0]))
            b = matrix(clean(resp['matrix'][1]))
            op = resp['operacion']
            if op == '+': res = suma(a,b)
            if op == '-': res = resta(a,b)
            if op == '*': res = multiplicacion(a,b)
            if op =='lineal': res = lineal(a,b)
            res = pd.DataFrame(res).to_json( orient='split')
            return {'resultado': res, 'mensaje': message}


class Unimatriz(Resource):
    def post(self):
        global message
        if request.method == "POST":
            resp = request.get_json()
            a = matrix(clean(resp['matrix'][0]))
            op = resp['operacion']
            if op == 'transpuesta': res = transpuesta(a)
            if op == 'diagonal': res = diagonall(a)
            if op == 'inversa': res = inversa(a)
            if op == 'triangularI': res = triangular(a, 'i')
            if op == 'triangularS': res = triangular(a, 's')
            if op =='determinante': res = determinante(a)
            if op =='rango': res = rango(a)
            if op =='norma': res = norma(a)

            res = pd.DataFrame(res).to_json( orient='split')
            
            return {'resultado': res, 'mensaje': message}

