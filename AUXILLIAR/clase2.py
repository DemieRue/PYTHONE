def edad_actual(an):
    ea=2023-an
    t=ea+4
    return ea,t
a=int(input("año"))
aux=edad_actual(a)
print("su",aux)