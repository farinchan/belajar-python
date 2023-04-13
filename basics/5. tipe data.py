#tipe data

#tipe data dari variable pada python bersifat dynamic 

nilai_x = 15 # integer (bilangan asli)
print("nilai x = ", nilai_x, ", Beritpe : ", type(nilai_x))

nilai_y = 15.5 # float (bilangan desimal)
print("nilai y = ", nilai_y, ", Beritpe : ", type(nilai_y))

nilai_z = "15" # string (huruf)
print("nilai z = ", nilai_z, ", Beritpe : ", type(nilai_z))

boolean = True # boolean (true/false)
print("nilai boolean = ", boolean, ", Beritpe : ", type(boolean))

list = [1,2, "fajri"] # list
print("nilai list = ", list, ", Beritpe : ", type(list))

#Tipe data khusus
complex = complex(1,3) # complex
print("nilai complex = ", complex, ", Beritpe : ", type(complex))


#Konversi Tipe data / casting tipe data
# Merubah tipe data menjadi tipe data yang lain

nilai_int = 10 #integer
print("nilai = ", nilai_int, ", Beritpe : ", type(nilai_int))

nilai_float = float(nilai_int) #float - diubah dari tipe data integer
print("nilai = ", nilai_float, ", Beritpe : ", type(nilai_float))

