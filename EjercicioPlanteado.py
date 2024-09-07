import math

# Valor exacto de sin(1.5)
x = 1.5
valor_real = math.sin(x)

# Expansión de Taylor hasta el tercer orden
taylor_tercer_orden = x - (x**3) / math.factorial(3)

# Expansión de Taylor hasta el quinto orden
taylor_quinto_orden = x - (x**3) / math.factorial(3) + (x**5) / math.factorial(5)

# Cálculo de errores relativos
error_relativo_tercer_orden = abs((valor_real - taylor_tercer_orden) / valor_real) * 100
error_relativo_quinto_orden = abs((valor_real - taylor_quinto_orden) / valor_real) * 100

# Resultados
print(f"Valor exacto de sin(1.5): {valor_real:.5f}")
print(f"Aproximación con Taylor (tercer orden): {taylor_tercer_orden:.5f}")
print(f"Aproximación con Taylor (quinto orden): {taylor_quinto_orden:.5f}")
print(f"Error relativo (tercer orden): {error_relativo_tercer_orden:.2f}%")
print(f"Error relativo (quinto orden): {error_relativo_quinto_orden:.2f}%")
