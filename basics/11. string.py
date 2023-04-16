# string

string = "ini adalah string"  # Variabel dengan tipe data string
print(string)
print(type(string))


# membuat string
"""
    1. dengan menggunakan single quote ( '' )
"""
string = 'ini adalah string'
print(string)

'''
    2. Menggunakan Double quote ( "" )
'''
string = "ini adalah string"
print(string)

# bisa juga digabungkan- dengan beberapa penggunaan
print('saya : "Apakah Kamu Sehat?"')
print("ini adalah hari jum'at")

# dapat juga mengguinakan tanda backslash ( \ )
print('ini adalah hari jum\'at')

"""
    \n	    Baris baru / newline	"Halo\nDunia"
    \t	    Tab	"Nama:\tJohn"	    Nama: John
    \\	    Karakter backslash	    "C:\\Program Files"
    \'	    Tanda petik tunggal	    "It's a dog"
    \"	    Tanda petik ganda	    "She said, \"Hi!\""	
    \b	    Backspace	            "Halo\bDunia"
    \r	    Carriage return	        "Halo\rDunia"
    \0	    Karakter null	        "Halo\0Dunia
"""

# String Literal / RAW String
print(r'C:/new Folder')

# multiline String
print("""
    Nama : inan
    Kelas : 12
""")

# Multiline String $ RAW
print(r"""
    coba \n gg
""")
