taller1 = float(input("Digite la primera nota del taller: "))
taller2 = float(input("Digite la segunda nota del taller: "))
prom_taller = (taller1 + taller2) / 2

evaluacion1 = float(input("Digite la primera evaluación: "))
evaluacion2 = float(input("Digite la segunda evaluación: "))
evaluacion3 = float(input("Digite la tercera evaluación: "))
prom_evaluaciones = (evaluacion1 + evaluacion2 + evaluacion3) / 3

trabajo_final = float(input("Digite la nota del trabajo final: "))

quiz1 = float(input("Digite la primera nota del quiz: "))
quiz2 = float(input("Digite la segunda nota del quiz: "))
quiz3 = float(input("Digite la tercera nota del quiz: "))
quiz4 = float(input("Digite la cuarta nota del quiz: "))
prom_quizzes = (quiz1 + quiz2 + quiz3 + quiz4) / 4

nota_definitiva = (prom_taller * 0.15) + (prom_evaluaciones * 0.30) + (trabajo_final * 0.30) + (prom_quizzes * 0.25)

print(f"La nota definitiva del estudiante es: {nota_definitiva}")
