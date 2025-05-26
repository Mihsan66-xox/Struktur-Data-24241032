# Input jumlah deret
n = 5

# Inisialisasi dua angka pertama
a = 1
b = 1
# Inisialisasi list untuk menyimpan deret
Deret = [a, b]

print(a, end=' , ')  # Cetak angka pertama
print(b, end=' , ')  # Cetak angka kedua

# Proses fibonacci
for i in range(2, n):  # range(2,10) karena 2 angka sudah dicetak
    c = a + b  # angka selanjutnya adalah penjumlahan 2 angka sebelumnya
    print(c, end=' , ')
    # Update nilai untuk iterasi selanjutnya
    a = b
    b = c
print("Deret Fibonacci:", ', '.join(map(str, Deret)))