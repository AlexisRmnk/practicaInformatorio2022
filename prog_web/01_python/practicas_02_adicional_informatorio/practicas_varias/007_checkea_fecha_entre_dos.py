import datetime
# checkear que una fecha (d3 a d7) este entre otras dos
#   (d1 como minimo y d2 como maximo)


d1 = datetime.date(day=1,month=1,year=2000)
d2 = datetime.date(day=10,month=1,year=2000)

d3 = datetime.date(day=5,month=1,year=2000)
d4 = datetime.date(day=1,month=2,year=2000)
d5 = datetime.date(day=1,month=5,year=1900)
d6 = datetime.date(day=7,month=1,year=2000)
d7 = datetime.datetime(day=8,month=1,year=2000,minute=10,hour=1,second=20)
ds = [d3, d4, d5, d6, d7]

print(type(d6))
print(type(d7))

for d in ds:
    print(f"d:{d} - tipo: {type(d)}")
    if isinstance(d, datetime.datetime): 
        #necesario xq python toma a datetime como date
        pass
    elif isinstance(d, datetime.date):
        print("Es DATE!")
    if isinstance(d, datetime.datetime):
        print("Es DATETIME!")
        print("CONVIRTIENDO A DATE!")
        d=d.date()
        if isinstance(d, datetime.date):
            print("Ahora es DATE!")
            print(f"AHORA: d:{d} - tipo: {type(d)}")
    
    if d2 >= d >= d1:
        print(f"{d.strftime('%d/%m/%Y')} ocurre entre "
              f"{d1.strftime('%d/%m/%Y')} y {d2.strftime('%d/%m/%Y')}" )
        print(True)
    
