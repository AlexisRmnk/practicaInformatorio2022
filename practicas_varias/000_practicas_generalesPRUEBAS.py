def fun_aux(e):
    return e['a']


d1 = {"a": "a", "b": "x"}
d2 = {"a": "z", "b": "x"}
d3 = {"a": "c", "b": "x"}
d4 = {"a": "b", "b": "x"}

list_ = [d1, d2, d3, d4]


print(list_)
list_.sort(key=fun_aux)
print(list_)