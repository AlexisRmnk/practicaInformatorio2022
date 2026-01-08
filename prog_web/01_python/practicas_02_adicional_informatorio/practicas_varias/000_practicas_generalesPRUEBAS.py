from functools import reduce
depositos = [20, 50, 10]

# Sin initializer empieza en 20 + 50...
# Con initializer (100), empieza calculando 100 + 20...
total = reduce(lambda saldo, ingreso: saldo + ingreso, depositos, 100)

print(total) # 180 (100 inicial + 20 + 50 + 10)
