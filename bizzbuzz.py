szam: int= int(input("Adjon meg egy számot: "))

if szam % 3 == 0 and szam % 2 == 0:
    print("BIMBUM")
elif szam % 2 == 0:
    print("BIM")
elif szam % 3 == 0:
    print("BUM")
else:
    print(szam)
