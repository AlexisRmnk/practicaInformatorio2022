from class_tenis import *
    
def returns_option():
    print("MATCH MENU")
    while(True):
            print("INDICAR OPERACION:\n0) Suspender partido\n"
                  "1) Anotar punto\n2) Mostrar estado")
            x = input("\t").strip()
            if x not in ("0", "1", "2"):
                print("Error. Reintentar ingreso de operacion.")
                continue
            return x
       
def start_match():
    m = Match()
    m.show_status()
    
    while(True):
        op = returns_option()
        if op == "0":
            print("Se suspende el partido.")
            print("Estado previo: ")
            m.show_status()
            break
        elif op == "1":
            m.good_ball()
        else: # op == "2":
            m.show_status()
        if m.getStatus() == m.getStatus_final_value():
            print("Partido finalizado.")
            break
        
def simulate_match():
    ''' function made for testing purposes '''
    m2 = Match()
    turn = 0
    while(m2.getStatus()!=m2.getStatus_final_value()):
        turn+=1
        print(f"Turno: {turn}")
        m2.test_good_ball()
        m2.show_status()
    
def simulate_match2():
    ''' function made for testing purposes '''
    m3 = Match()
    m3.show_status()
    
    m3.status = m3.status_tuple[0]
    m3.players[1].setScore(40)
    m3.players[1].setGames(5)
    m3.players[1].setSets(2)
    m3.players[2].setScore(30)
    m3.players[2].setGames(3)
    m3.players[2].setSets(2)
    print("TEST")
    m3.show_status()
    
    while(True):
        op = returns_option()
        if op == "0":
            print("Se suspende el partido.")
            print("Estado previo: ")
            m3.show_status()
            break
        elif op == "1":
            m3.good_ball()
        else: # op == "2":
            m3.show_status()
        if m3.getStatus() == m3.getStatus_final_value():
            print("Partido finalizado.")
            break