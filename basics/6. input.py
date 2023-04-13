# input
# mengambil input dari user melalui terminal

data = input("masukkan data : ")
print("data = ", data, "type : ", type(data))  # type data input pasti string

# kalo mau mengubah tipe data dari data input, kita harus melakukan konversi tipe data
konversi_int = int(input("masukkan angka : "))
print("data = ", konversi_int, "type : ", type(konversi_int))
