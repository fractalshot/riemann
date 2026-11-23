# Genereert de eerste 100 niet-triviale nullen van de Riemann zeta-functie (imaginair deel) met mpmath.
import mpmath as m
m.mp.dps = 20
z = [round(float(m.zetazero(n).imag), 9) for n in range(1, 101)]
print(",".join(map(str, z)))
