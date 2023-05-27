# Rango de precios para la línea de cartuchos compatibles

def mr_toncomp(costo):

    rangos_margenes = [
        (0, 50, 70), (50, 100, 68.66), (100, 150, 64.06),
        (150, 200, 56.66), (200, 250, 46.90), (250, 300, 41.06),
        (300, 350, 39.04), (350, 400, 37.81), (400, 450, 37.02),
        (450, 500, 36.91), (500, 550, 36.13), (550, 600, 35.79),
        (600, 650, 35.57), (650, 700, 35.34), (700, 750, 35.23)
    ]

    for rango in rangos_margenes:
        if rango[0] < costo <= rango[1]:
            return rango[2]

    return 35

# if __name__ == "__main__":

#     while True:
#         costo = int(input("Costo: "))

#     # calcular_margen_rango(costo)
#         print(mr_toncomp(costo))

