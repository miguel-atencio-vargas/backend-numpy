from flask_restful import Resource
from flask import request, jsonify
from numpy import *
import numpy as np
import pandas as pd

from scipy import stats
global message
global name

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
        message = 'Se realizo el producto vectorial correctamente'
        return a*b
    except:
        message = '(Error) No se cumple la condicion de que las columnas de la matriz A sea igual a las filas de la matriz B. shape(a)={} shape(b)={}'.format(shape(a), shape(b))
def producto_escalar(a,b):
    try:
        global message 
        message = 'Se realizo el producto escalar correctamente'
        res=0;a=array(a);b=array(b)
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                res+= a[i][j]*b[i][j]
        return [res]
    except:
        message = '(Error) Las dimensiones de sus matrices no son iguales shape(a)={} shape(b)={} '.format(shape(a), shape(b))


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

def arrayNormal(m,n):
    global message, name
    message =  'Se creo el archivo correctamente'
    name = 'Distribucion Normal Scipy'
    f = stats.norm.pdf
    v_bound = np.sqrt(f(np.sqrt(2))) * np.sqrt(2)
    umax, vmin, vmax = np.sqrt(f(0)), -v_bound, v_bound
    rvs = []
    for i in range(m):
        print(n)
        rvs.append(stats.rvs_ratio_uniforms(f, umax, vmin, vmax, size=n))
    return rvs
def arrayMulti(m,n):
    global message, name
    message =  'Se creo el archivo correctamente'
    name = 'Multivariate_normal Scipy'
    f = stats.multivariate_normal.pdf
    v_bound = np.sqrt(f(np.sqrt(2))) * np.sqrt(2)
    umax, vmin, vmax = np.sqrt(f(0)), -v_bound, v_bound
    rvs = []
    for i in range(m):
        print(n)
        rvs.append(stats.rvs_ratio_uniforms(f, umax, vmin, vmax, size=n))
    return rvs
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
            if op == 'escalar': res = producto_escalar(a,b)
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
 
class Random(Resource):
    def post(self):
        global message, name
        if request.method == 'POST':
            resp = request.get_json()
            m = int(resp['m']); n = int(resp['n'])
            a = int(resp['a']); b = int(resp['b']); tipo = resp['type']; 
            if tipo == 'float':
                message='Se creo la tabla de excel de valores de tipo float con los siguientes valores: filas:{}, columnas:{}, rango: ({}, {}) '.format(m,n,a,b)
                name='Float({}, {})'.format(n,m)
                res = (1+b-a) * np.random.random_sample((m, n)) + a
            if tipo == 'normal':
                name='Normal({}, {})'.format(n,m)
                mu = resp['mu']; sigma = resp['sigma']
                message='Se creo la tabla de excel de distribucion normal con los siguientes valores: filas:{}, columnas:{}, mu:{}, sigma:{} '.format(m,n,mu,sigma)
                res=[]
                for i in range(m): 
                    res.append(np.random.normal(mu, sigma, n))
            if tipo=='normal_Scipy': res = arrayNormal(m,n)
            if tipo=='Multivariate_normal': res = arrayMulti(m,n)
            if tipo =='Integer':
                name='Integers({}, {})'.format(n,m)
                res = np.random.randint(a,b+1, size=(m, n))
                message='Se creo la tabla de excel de valores de tipo int con los siguientes valores: filas:{}, columnas:{}, rango: ({}, {}) '.format(m,n,a,b)
            res = pd.DataFrame(res).to_json( orient='split')
            return {'data': res, 'message': message, 'name': name}



