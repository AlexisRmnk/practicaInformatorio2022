def relacion(a:tuple, b:tuple) -> tuple:
    name = 0
    amount = 1
    if a[amount] > b[amount]:
        return (a[name], False)
    elif a[amount] < b[amount]:
        return (b[name], False)
    else:
        return (f"{a[name]} y {b[name]}", True)

    
