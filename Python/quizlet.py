# szavak = ["alma", "autó", "szív", "só", "ananász"]


szo1 = "alma"
jelentés1 = "apple"
szo2 = "autó"
jelentés2 = "car"
szo3 = "szív"
jelentés3 = "heart"
szo4 = "só"
jelentés4 = "salt"
szo5 = "ananász"
jelentés5 = "pineapple"

szamlalo = 0
valasz = str(input("Hogy van a következő zó angolul? ", szo1, " - " ))
if valasz == jelentés1:
    print("Helyes válasz")
    szamlalo += 1
else:
    print("A válasz helytelen")

valasz2 = str(input("Hogy van a következő zó angolul? ", szo2, " - " ))
if valasz == jelentés2:
    print("Helyes válasz")
    szamlalo += 1
else:
    print("A válasz helytelen")

valasz3 = str(input("Hogy van a következő zó angolul? ", szo3, " - " ))
if valasz == jelentés3:
    print("Helyes válasz")
    szamlalo += 1
else:
    print("A válasz helytelen")

valasz4 = str(input("Hogy van a következő zó angolul? ", szo4, " - " ))
if valasz == jelentés4:
    print("Helyes válasz")
    szamlalo += 1
else:
    print("A válasz helytelen")

valasz5 = str(input("Hogy van a következő zó angolul? ", szo5, " - " ))
if valasz == jelentés5:
    print("Helyes válasz")
    szamlalo += 1
else:
    print("A válasz helytelen")



print("Eredmény: 5/", szamlalo)
print("helyes válaszok: alma - apple, autó - car, szív - heart, só - salt, ananász - pineapple")




