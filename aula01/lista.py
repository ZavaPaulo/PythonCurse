#LISTA
frutas = ["Banana", "Maçã", "Uva"]
print(frutas)

frutas[1] = "Abacaxi"
print(frutas)

frutas.insert(0, "Kiwi")
print(frutas)

frutas.remove("Abacaxi")
print(frutas)

if "Uva" in frutas:
    print("Tem uva nas frutas")
else:
    print("Não tem uva nas frutas")