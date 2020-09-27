# funciones complejos
## autor sebastian porras
import math
def suma(complejo1, complejo2):
    complejo1 = list(complejo1)
    real1, imag1 = complejo1[0], complejo1[1]
    complejo2 = list(complejo2)
    real2, imag2 = complejo2[0], complejo2[1]
    suma1 =  real1 + real2
    suma2 = imag1 + imag2
    return complex(round(suma1,2), round(suma2,2))
def producto(a, b):
    complejo1 = list(a)
    real1, imag1 = complejo1[0], complejo1[1]
    complejo2 = list(b)
    real2, imag2 = complejo2[0], complejo2[1]
    producto1 = real2*real1 - imag1*imag2
    producto2 = imag1*real2 + real1*imag2
    return complex(round(producto1,2), round(producto2,2))
def resta(complejo1, complejo2):
    complejo1 = list(complejo1)
    real1, imag1 = complejo1[0], complejo1[1]
    complejo2 = list(complejo2)
    real2, imag2 = complejo2[0], complejo2[1]
    resta1 =  real1 - real2
    resta2 = imag1 - imag2
    return complex(round(resta1,2), round(resta2,2))
def division(a, b):
    a = list(a)
    a1, b1 = a[0], a[1]
    b = list(b)
    a2, b2 = b[0], b[1]
    division1 = round((a2*a1 + b1*b2) / (a2**2 + b2**2),2)
    division2 = round((b1*a2 - a1*b2) / (a2**2 + b2**2), 2)
    return complex(round(division1,2), round(division2,2))
def modulo(complejo):
    complejo = list(complejo)
    real, imaginario = complejo[0], complejo[1]
    modulo = (real**2 + imaginario**2)**0.5
    return round(modulo, 2)
def conjugado(complejo):
    complejo = list(complejo)
    real, imaginario = complejo[0], complejo[1]
    imaginario = -imaginario
    return complex(real, imaginario)
def conversioncap(a):
    complejo = list(a)
    real1, imag1 = complejo[0], complejo[1]
    r = (real1**2 + imag1**2)**0.5
    angulo = math.atan2(imag1, real1)
    return (round(r,2), round(angulo,2))
def conversionpac(complejo):
    complejo = list(complejo)
    r, angulo = complejo[0], complejo[1]
    real = round(r* math.cos(angulo),2)
    imag = round(r* math.sin(angulo),2)
    return(real, imag)
def fase(complejo):
    complejo = list(complejo)
    real, imag = complejo[0], complejo[1]
    fase = math.degrees(math.atan2(imag,real))
    return round(fase, 2)
