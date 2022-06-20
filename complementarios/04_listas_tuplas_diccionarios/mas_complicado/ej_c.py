# Simular la operación de colas de un Rapipago, que funciona con dos
#  colas diferentes. El usuario llega y se ubica en la cola de menor
#  cantidad de personas. Al finalizar el proceso indique cuántos
#  elementos tiene cada cola.

def simulate_queue(people:int, queue1: list, queue2: list, 
                    exit_rate_per_queue: int, daily_counter:int) -> tuple:
    '''
    simultates 2 queues.
    'exit_rate_per_queue' means how many people exits a queue in an hour
    '''

    num_pers = ""
    for i in range(people):
        daily_counter += 1
        if len(queue1) <= len(queue2):
            num_pers = "P-" + str(daily_counter)
            queue1.append(num_pers)
        else:
            num_pers = "P-" + str(daily_counter)
            queue2.append(num_pers)
    for i in range(exit_rate_per_queue * 2):
        if i%2 == 0: # in 1 hour 'exit_rate_per_queue' people exit each queue
            if len(queue1) > 0:
                queue1.pop(0)
        else:
            if len(queue2) > 0:
                queue2.pop(0)
    return queue1, queue2, daily_counter

queue_1 = list()
queue_2 = list()
exit_rate_per_queue_ = 6
daily_counter_ = 0

print("Entrada: indicar n° de personas que llegaron en un lapso de tiempo "
        "dado - En teoria, cada 10 mins se atendera dos personas (6 personas"
        " / hora en cada cola o 12 personas / hora en total)\n")

t = 8 # inicio 08 HS - Fin obligatorio a las 24 HS
while(True):
    print(f"Indicar cantidad personas que llegaron entre las {t} hs y las"
            f" {t+1} hs (-1 para finalizar simulacion)")
    people_ = int(input("\t"))
    if people_ == -1:
        break
    
    queue_1, queue_2, daily_counter_ = simulate_queue(people_, queue_1,  
                        queue_2, exit_rate_per_queue_, daily_counter_)
    print(f"ESTADO A LAS {t+1} HS")
    print(f"Cola 1: ({len(queue_1)} personas) {queue_1}")
    print(f"Cola 2: ({len(queue_2)} personas) {queue_2}")
    t += 1
    if t == 24:
        break

print(f"\n\nESTADO FINAL COLAS: (a las {t} hs)")
print(f"Cola 1: ({len(queue_1)} personas) {queue_1}")
print(f"Cola 2: ({len(queue_2)} personas) {queue_2}")