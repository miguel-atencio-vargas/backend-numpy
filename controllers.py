from flask_restful import Resource
from flask import request, jsonify
from numpy import *
import pandas as pd

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



class Employees(Resource):
    def get(self):
        print('hola')
        return {'employees': [{'id':1, 'name':'Balram'},{'id':2, 'name':'Tom'}]}

class Suma(Resource):

    def post(self):
        if request.method == "POST":
            try:
                resp = request.get_json()
                a = array(clean(resp[0]))
                b = array(clean(resp[1]))
                res = a+b
                res = pd.DataFrame(res).to_json( orient='split')
                print(res)
                return {'resultado': res}
            except ValueError:
                print(ValueError)
                return {'error': 'Se ha producido un error en el servicio. Se recomienda revisar las dimensiones de las matrices'}
