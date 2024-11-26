herencia_total = float(input("Digite el monto total de la herencia: "))
esposa = herencia_total * 0.40
restante=herencia_total-esposa
hijo1 = restante * 0.30
hijo2 = restante * 0.20
hijo3 = restante * 0.40
hijo4 = restante * 0.10
print(f"A la esposa le corresponde: {esposa}")
print(f"Al hijo 1 le corresponde: {hijo1}")
print(f"Al hijo 2 le corresponde: {hijo2}")
print(f"Al hijo 3 le corresponde: {hijo3}")
print(f"Al hijo 4 le corresponde: {hijo4}")
