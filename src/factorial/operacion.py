import math
from scipy import stats
import statistics

def multiplicar(a,b):
    resultado=a*b
    return resultado

def restar(a,b):
    resultado=a-b
    return resultado

def factorial(a):
    for i in range(a+1):
        if i==0:
            b=1
        else:
            b=b*i
    return b

def promedio(vector):
    if not isinstance(vector, list) or all(isinstance(item, (int, float)) for item in vector)==False:
        print("Debe ser una lista y debe ser numerica")
    else:
        for element in vector:
            promedio = sum(vector)/len(vector)
    return promedio

def mediana(vector):
    if not isinstance(vector, list) or all(isinstance(item, (int, float)) for item in vector)==False:
        print("Debe ser una lista")
    else:
        vector.sort()
        mitad=round(len(vector)//2)
    return vector[mitad]

def moda(vector):
    if not isinstance(vector, list) or all(isinstance(item, (int, float)) for item in vector)==False:
        print("Debe ser una lista")
    else:
        moda = statistics.mode(vector)
    return moda

def varianza(vector):
    if not isinstance(vector, list) or all(isinstance(item, (int, float)) for item in vector)==False:
        print("Debe ser una lista")
    else:
        mean = promedio(vector)
        a=0
        for element in vector:
            if a==0:
                suma = (element - mean) ** 2
            else:
                suma = ((element - mean) ** 2) + suma
            a=+1
        varianza = suma / len(vector)
    return varianza

def desviacion(vector):
    if not isinstance(vector, list) or all(isinstance(item, (int, float)) for item in vector)==False:
        print("Debe ser una lista")
    else:
        desviacion = math.sqrt(varianza(vector))
    return desviacion

def pesoposicional(vector,vector2):
    if all(isinstance(item, (int, float)) for item in vector)==False or all(isinstance(item, (int, float)) for item in vector2)==False:
        print("las listas deben ser numericas debe")
    else:
        if not isinstance(vector, list) or not isinstance(vector2, list) or len(vector) != len(vector2):
            print("Debe ser una lista ambas y deben de ser de la misma longitud")
        else:
            for i in range(len(vector)):
                if i==0:
                    suma=vector[i]*vector2[i]
                else:
                    suma=(vector[i]*vector2[i])+suma
            peso=suma/sum(vector2)
            return peso   
