# Realizar un algoritmo que invierta el orden de una cola.

def invert_queue(queue: list) -> list:
    inverted_queue = list()
    for x in queue:
        inverted_queue.insert(0, x)
    return inverted_queue

queue_1 = ["a", 1, "b", 2, True, 98, 99, 100]
print(f"COLA:\t\t{queue_1}")
print(f"COLA INVERTIDA: {invert_queue(queue_1)}")