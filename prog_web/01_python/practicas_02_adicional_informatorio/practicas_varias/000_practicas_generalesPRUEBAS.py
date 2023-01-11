import datetime
# checkear que una fecha (d3 a d7 y d_1 a d_4) este entre otras dos
#   (d1 como minimo y d2 como maximo)

d1 = datetime.date(day=2,month=1,year=2000)
d2 = datetime.date(day=10,month=1,year=2000)

d3 = datetime.date(day=5,month=1,year=2000)
d4 = datetime.date(day=1,month=2,year=2000)
d5 = datetime.date(day=1,month=5,year=1900)
d6 = datetime.date(day=7,month=1,year=2000)
d7 = datetime.datetime(day=8,month=1,year=2000,minute=10,hour=1,second=20)
d_1 = datetime.datetime(day=2,month=1,year=2000,minute=10,hour=1,second=20)
d_2 = datetime.datetime(day=10,month=1,year=2000,minute=10,hour=1,second=20)
d_3 = datetime.datetime(day=11,month=1,year=2000,minute=10,hour=1,second=20)
d_4 = datetime.datetime(day=1,month=1,year=2000,minute=10,hour=1,second=20)
ds = [d3, d4, d5, d6, d7, d_1, d_2, d_3, d_4]
# caso 1   2   3  4    5    6   7    8    9

# print(type(d6))
# print(type(d7))
i=0
for d in ds:
    i+=1
    print("#"*50 + f"\ncaso {i}:")
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
    
    if d2 >= d >= d1: # esta comparacion INCLUYE EXTREMOS
        print(f"{d.strftime('%d/%m/%Y')} ocurre entre "
              f"{d1.strftime('%d/%m/%Y')} y {d2.strftime('%d/%m/%Y')}" )
        print(True)
    
