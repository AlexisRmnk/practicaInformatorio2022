from class_pizzeria import *

def menu():
    p = Pizzeria()
    while(True):
        op = returns_option()
        if op == "0":
            print("Finalizando ejecucion.")
            break
        elif op == "1":
            p.generate_order()
            print("Pedido generado")
        elif op == "2":
            p.show_orders()
        elif op == "3":
            p.most_popular()
        elif op == "4": # TESTEAR
            p.income_period()
        elif op == "5":
            p.modify_orders_date()    
        
def returns_option():
    print("PIZZERIA MENU")
    while(True):
            print("INDICAR OPERACION:\n\t0) Finalizar programa\n\t"
                  "1) Añadir pedido\n\t2) Mostrar pedidos\n\t3) "
                  "Mostrar variedades y tipos mas solicitados\n\t4) "
                  "Mostrar recaudaciones y detalle de pedidos dado un "
                  "periodo de tiempo.\n\t5) Modificar fechas pedidos "
                  "para realizar pruebas")
            x = input("\t").strip()
            if x not in ("0", "1", "2", "3", "4", "5"):
                print("Error. Reintentar ingreso de operacion.")
                continue
            return x        