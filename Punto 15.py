inicio_dia = int(input("Digite el número de la registradora al iniciar el día: "))
fin_dia = int(input("Digite el número de la registradora al finalizar el día: "))
valor_pasaje = float(input("Digite el valor del pasaje: "))

total_pasajeros = fin_dia - inicio_dia
total_recaudado = total_pasajeros * valor_pasaje

liquidado_conductor = total_recaudado * 0.25
liquidado_empresa = total_recaudado * 0.75

print(f"Total de pasajeros transportados: {total_pasajeros}")
print(f"Valor liquidado al conductor: {liquidado_conductor}")
print(f"Total liquidado a la empresa: {liquidado_empresa}")
