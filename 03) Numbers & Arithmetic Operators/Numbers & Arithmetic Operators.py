# -----------------
# ---- Numbers ----
# -----------------

# Integer
print(type(10))
print(type(999))
print(type(0))
print(type(-10))
print(type(-999))

# Floating Point Number
print(type(10.153))
print(type(-10.52))
print(type(0.2556))
print(type(-0.659))

# Complex
print(type(3+6j)) # Contain of Real and Imaginary

myComplexNumber = 9+5j
print("Real is: {}".format(myComplexNumber.real))
print("Imaginary is: {}".format(myComplexNumber.imag))

# [1] You can convert from Int to Float or Comolex.
# [2] You can convert from Float to Int or Complex.
# [3] You can't convert from Comlex to Int or Float.

print(float(100)) 
print(complex(100))

print(int(10.25))
print(complex(10.25))

# --------------------------
# -- Arithmetic operators --
# --------------------------
# [+] Addition
# [-] Subtraction
# [*] multiplication
# [/] Division
# [%] Modulus
# [**] Exponent
# [//] Floor Division
# --------------------------

# -------------------------------------
# -- Arithmetic operators Priorities --
# -------------------------------------
# [1] Parentheses ()
# [2] Exponent
# [3] Multiplication (*), Division (/), Floor Division (//), Modulus (%)
# [4] Addition (+), Subtraction (-)
# -------------------------------------

# Addition
print(10 + 55)
print(-20 + 10)
print(1.5 + 6.2)

# Subtraction
print(40 - 10)
print(-30 - -20)
print(3.7 - 2.2)

# multiplication
print(10 * 10)
print(70 + 65 * 2)
print((70 + 65) * 2)

# Division
print(100 / 20)
print(50 + 250 / 5)
print(int(100 / 20))

# Modulus
print(8 % 2)
print(9 % 2)
print(20 % 5 - 1)

# Exponent
print(2 ** 3)
print(4 ** 4)

# Floor Division
print(20 // 6)
print(1000 // 15)
print(130 // 20)