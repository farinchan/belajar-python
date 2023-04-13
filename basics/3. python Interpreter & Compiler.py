# Python Interpreter
"""
    dimana python yang menggunakan interpreter akan menjalankan
    code baris ber baris
    caranya:
    - buka terminal lalu tulis
        python [nama_file]
"""

#python Compiler
"""
    dimana source code python dijalankan dengan mengubah source code
    menjadi bytcode terlebih dahulu
    caranya:
    -buka terminal lalu tulis
        python -m py_compile [nama_file]
    -lalu jalankan execute file
        python __pycache__/[nama_file]
"""

#jalankan

import time
start_time = time.time()

print("Hello World")
print("Nama Saya Fajri Rinaldi Chan")
a=10
print(a)

#kode dibawah untuk membandingkan Kecepatan compiler dengan interpreter
print("Kecepatan", time.time() - start_time, "Detik")