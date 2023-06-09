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

# 8. Mengganti string menjadi UpperCase
halo = "Halo Dek"
print("String Normal = ", halo)
halo = halo.upper()
print("String UpperCase = ", halo)

# 8. Mengganti String Menjadi LowerCase
halo = "Halo DekkZ, Mau SAma OMMZZ Gak?"
print("String Normal = ", halo)
halo = halo.lower()
print("String UpperCase = ", halo)

# 9 . Pengecekan lower/upper dll, x.method dalam string
halo = "halo"
halo_apakah_lower = halo.islower()  # hasilnya Boolean
print("halo = " + str(halo_apakah_lower))
halo_apakah_upper = halo.isupper()  # hasilnya Boolean
print("halo = " + str(halo_apakah_upper))
"""
    isalpha() -> untuk ngecek semua huruf
    isnum() -> pengecekan huruf dan angka
    isdecimal() -> pengecekan angka saja
    isspace() -> penegcekan spasi, tab, newline \n
    istitle() -> pengecekan apakah semu kata dimulai dari huruf besar
"""
# 10. ngecek komponen startswith() dan endswith()
halo = "halo dek".startswith("halo")
print(halo)
halo = "halo dek".endswith("halo")
print(halo)

# 11. penggabungan Component join() dan memisahkan komponen split()
pisah = ["aku", "sayang", "kamu"]
print(pisah)
gabung = " ".join(pisah)
print(gabung)
print(gabung.split(" "))

# 12. alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10)
print("'" + kanan + "'")

kiri = "kiri".ljust(10)
print("'" + kiri + "'")

tengah = "tengah".center(10)
print("'" + tengah + "'")

