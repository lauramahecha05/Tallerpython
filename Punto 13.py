terreno_total = float(input("Digite el área total del terreno en metros cuadrados: "))
area_cultivos = terreno_total * 0.40
area_vivienda = terreno_total * 0.25
area_zonas_verdes = terreno_total * 0.15
area_disponible = terreno_total - (area_cultivos + area_vivienda + area_zonas_verdes)

print(f"Área para cultivos: {area_cultivos} metros cuadrados.")
print(f"Área para vivienda: {area_vivienda} metros cuadrados.")
print(f"Área para zonas verdes: {area_zonas_verdes} metros cuadrados.")
print(f"Área disponible para otros proyectos: {area_disponible} metros cuadrados.")
