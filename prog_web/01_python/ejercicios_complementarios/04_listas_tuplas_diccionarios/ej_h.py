# Construya un algoritmo que sume todos los elementos
#  en posición par de una lista.

def list_to_string_sum(list_:list) -> str:
    '''
    Makes a string from a list with the next form:
    "list[0] + list[1] + ... + list[n-1] + list[n]"
    '''
    string_ = ""
    i = 0
    for x in list_:
        if i==((len(list_))-1):
            if x >= 0:
                string_ = string_ + str(x)
            else:
                string_ = string_ + "(" + str(x) + ")"            
        else:
            if x >= 0:
                string_ = string_ + str(x) + " + "
            else:
                string_ = string_ + "(" + str(x) + ")" + " + "
        i += 1
    return string_

list_ = [1, 3, 55, 35, -1, 12, 44]
sum_ = i = 0
aux_ = list()

print("Lista: ", list_)
for x in list_:
    if i%2==0:
        aux_.append(x)
        sum_+=x
    i += 1

string_ = list_to_string_sum(aux_)
print(f"Sumatoria elementos posicion par: {string_} = {sum_}")