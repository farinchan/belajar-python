# String Manipulation

# 1. Concatenate
nama_depan = "Fajri"
nama_tengah = "Rinaldi"
nama_belakang = "Chan"

nama_lengkap = nama_depan + " " + nama_tengah + " " + nama_belakang
print(nama_lengkap)

# 2. hitung panjang string
nama = "Fajri Rinaldi Chan"
panjang = len(nama)
print(panjang)

# 3. Cek karakter dalam string
i = "i"
status = i in nama
print(status)

# 4. Mengulang string
print("wk"*10)

# 5 . indexing
print(nama[0])
print(nama[1])
print(nama[2:5])

# 6. cek item paling kecil dan besat
print(min(nama))
print(max(nama))
# maksudnya disini min/max dari ascii code
ascii_code = ord(" ")
print("ascii ocde dari char ini adalah" + str(ascii_code))

# 7. Operator dalam bentuk method
data = "halo nama saya fajri rinaldi chan"
jumlah = data.count("a")
print("jumlah 'a' dalam data = ", str(jumlah))
