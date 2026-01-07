
# ejemplo de practica mio
def su_suma_es_par(numero1,numero2):
    if ( (numero1+numero2) % 2 == 1):
        return False
    else:
        return True

print('(2 + 1) es par?', su_suma_es_par(2,1))
print('(3 + 3) es par?', su_suma_es_par(3,3))
print('(4 + 3) es par?', su_suma_es_par(4,3))
print('(5 + 1) es par?', su_suma_es_par(5,1))

# ejemplo lambda
lmbd_suma_par = lambda n1,n2: (n1+n2) % 2 == 1
print('lmbd (2 + 1) es par?', lmbd_suma_par(2,1))
print('lmbd (3 + 3) es par?', lmbd_suma_par(3,3))
print('lmbd (4 + 3) es par?', lmbd_suma_par(4,3))
print('lmbd (5 + 1) es par?', lmbd_suma_par(5,1))
