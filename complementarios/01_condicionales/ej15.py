# Un obrero necesita calcular su salario semanal, el cual se obtiene de
# la siguiente manera:
#       i.  Si trabaja 40 horas o menos se le paga $16 por hora
#       ii. Si trabaja más de 40 horas se le paga $16 por cada una de
#           las primeras 40 horas y $20 por cada hora extra.

hs = float(input("Ingrese cant de hs semanales trabajadas:\n"))

if hs <= 40:
    paga = hs * 16
else:
    paga = 40 * 16 + (hs-40) * 20

print(f"Por las {hs} hs semanales trabajadas se pagaran ${paga}")
