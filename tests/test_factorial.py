from funciones.factorial import factorial
resultado_1 = factorial(5)
if resultado_1 == 120:
    print("Test 1 exitoso: factorial de 5 es 120")
else:
    print("Test 1 fallo")

resultado_2 = factorial(0)
if resultado_2 == 1:
    print("Test 2 exitoso: factorial de 0 es 1")
else:
    print("Test 2 falló")