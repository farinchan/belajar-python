# Operasi Logika

# operator Logika : OR, AND, NOT, XOR

# Tabel Kebenaran AND
# --------------------
# | A     | B     | A and B |
# --------------------
# | True  | True  |  True   |
# | True  | False |  False  |
# | False | True  |  False  |
# | False | False |  False  |
# --------------------

# Tabel Kebenaran OR
# --------------------
# | A     | B     | A or B |
# --------------------
# | True  | True  |  True  |
# | True  | False |  True  |
# | False | True  |  True  |
# | False | False |  False |
# --------------------

# Tabel Kebenaran NOT
# --------------------
# | A     | not A |
# --------------------
# | True  | False |
# | False | True  |
# --------------------

A = True
B = False

# Logika OR
print("===== OR =====")
print(A, " or ", B, " = ", A or B)

# Logika AND
print("===== AND =====")
print(A, " and ", B, " = ", A and B)

# Logika XOR
print("===== XOR =====")
print(A, " xor ", B, " = ", A ^ B)

# Logika NOT
print("===== NOT =====")
print("NOT ", A, " = ", not A)
print("NOT ", B, " = ", not B)



