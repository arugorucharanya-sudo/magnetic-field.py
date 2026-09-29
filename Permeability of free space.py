import math

 Permeability of free space
mu_0 = 4 * math.pi * 10**-7

 Input values
I = float(input("Enter current (A): "))
r = float(input("Enter distance from conductor (m): "))

 Calculate magnetic field
B = (mu_0 * I) / (2 * math.pi * r)

 Display result
print("\n--- Magnetic Field Calculation ---")
print("Current =", I, "A")
print("Distance =", r, "m")
print("Magnetic Field =", B, "T")
