# operasi komparasi

# hasil dari operasi komparasi adalah boolean(true/false)
# operator koparasi : >, <, <=, >=, ==, !=, is, is not,

a = 3
b = 2

# lebih besar dari ( > )
print("===== Lebih Besar dari ( > ) =====")
hasil = a > 2
print(a, " > ", 2, " = ", hasil)
hasil = b > 2
print(b, " > ", 2, " = ", hasil)
hasil = a > 4
print(a, " > ", 4, " = ", hasil)

# lebih kecil dari ( < )
print("===== Lebih kecil dari ( < ) =====")
hasil = a < 2
print(a, " < ", 2, " = ", hasil)
hasil = b < 2
print(b, " < ", 2, " = ", hasil)
hasil = a < 4
print(a, " < ", 4, " = ", hasil)

# lebih besar sama dengan ( >= )
print("===== lebih besar sama dengan ( >= ) =====")
hasil = a >= 2
print(a, " >= ", 2, " = ", hasil)
hasil = b >= 2
print(b, " >= ", 2, " = ", hasil)
hasil = a >= 4
print(a, " >= ", 4, " = ", hasil)

# lebih Kecil sama dengan ( <= )
print("===== lebih Kecil sama dengan ( <= ) =====")
hasil = a <= 2
print(a, " <= ", 2, " = ", hasil)
hasil = b <= 2
print(b, " <= ", 2, " = ", hasil)
hasil = a <= 4
print(a, " <= ", 4, " = ", hasil)

# sama dengan sama dengan ( <= )
print("===== sama dengan sama dengan ( == ) =====")
hasil = a == 2
print(a, " == ", 2, " = ", hasil)
hasil = b == 2
print(b, " == ", 2, " = ", hasil)
hasil = a == 4
print(a, " == ", 4, " = ", hasil)

# tidak sama dengan ( <= )
print("===== tidak sama dengan ( != ) =====")
hasil = a != 2
print(a, " != ", 2, " = ", hasil)
hasil = b != 2
print(b, " != ", 2, " = ", hasil)
hasil = a != 4
print(a, " != ", 4, " = ", hasil)

# is -> membandingkan objek/memory
print("===== is =====")
hasil = a is b
print(a, " is ", b, " = ", hasil)
