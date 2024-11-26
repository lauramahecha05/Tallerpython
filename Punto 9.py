alto = float(input("Digite el alto del muro en metros: "))
ancho = float(input("Digite el ancho del muro en metros: "))
area_baño = alto * ancho
baldosas_necesarias = area_baño / 3.5
print(f"El área del baño es: {area_baño:.2f} metros cuadrados.")
print(f"El número de baldosas necesarias es: {baldosas_necesarias:.2f}")
