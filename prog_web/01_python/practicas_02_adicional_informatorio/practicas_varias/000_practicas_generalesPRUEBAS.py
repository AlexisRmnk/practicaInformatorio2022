
# copiar un diccionario de forma correcta
dict1 = {0: "0", 1:"1", 2:"2"}
dict1_copy = dict1.copy()

print(f"dict1: {dict1} - dict1_copy: {dict1_copy}")
dict1[1] = "otra cosa"
print(f"dict1: {dict1} - dict1_copy: {dict1_copy}")