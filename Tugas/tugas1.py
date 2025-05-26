# jumlah baris piramida
n = 3
i = 0

while i < n :
    spasi = " " * (n - i - 1) # menambahkan spasi di kiri
    bintang = "*" * (2 * i + 1) # Menambahkan jumlah bintang sesuai baris
    print(spasi + bintang)  # Gabungkan spasi dan bintang lalu cetak
    i += 1

