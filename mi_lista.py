print("Ejemplo de listas")
arcoiris=["verde", "azul", "morado"]

print(arcoiris)

longitud=len(arcoiris)
print("Elementos que contiene la lista arcoiris:",longitud)

print(f"Elementos que contiene la lista arcoiris: {longitud}")
print("Accediendo a un elemento de la lista")
print(arcoiris[2])
print(f"Elemento en la posicion 0 es: {arcoiris[0]}")
print(f"Elemento en la posicion 0 es:",arcoiris[0])


print("Agregar a un elemento de la lista")
print(arcoiris)
arcoiris.append("naranja")
print(arcoiris)

print("Listar los elementos de la lista ciclo for")

for i in arcoiris:
    print(i)

