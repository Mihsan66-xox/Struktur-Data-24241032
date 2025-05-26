# Meminta Input dari pengguna untuk jumlah deret
jumlah_deret = int(input('masukan jumlahderet bilangan:'))

# inisialisasi variabel untuk mrnyimpan bilangan genap
bilangan_genap = []

# perulangan untuk menghasilkan bilangan genap
for i in range(1, jumlah_deret + 1):
    bilangan_genap.append(i * 2)
# menghitung bilangan genap
a, b = 1, 1

# menampilkan deret bilangan genap
print("Deret bilangan genap:",bilangan_genap)