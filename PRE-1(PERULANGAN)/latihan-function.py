def sapa():
    print("halo selamat datang")

# memanggil function
sapa()
sapa()
sapa()

# function dengan satu parameter
def sapa_nama(nama) :
    print(f"halo , {nama}")

# memanggil function
sapa_nama("adam")

# function dengan lebih dari 1 parameter
def luas_segitiga(alas, tinggi) :
    luas= (alas * tinggi) / 2
    print("luas segitiga : %f" % luas)

# pemanggilan function 
luas_segitiga(3, 4)

def tambah(a, b):
    return a + b

# pemanggilan fungsi
hasil = tambah(3, 5)
print("Hasil:", hasil)

def luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# pemanggilan fungsi
print(f"Luas Persegi : {luas_persegi(6)}")

# rumus sisi x sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas


# rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    return volume

# pemanggilan fungsi
vol_persegi = volume_persegi(6)
print(f"Volume_Persegi = {vol_persegi}")

# pemanggilan function, dengan 1 argumen
student("Wallberg")

# pemanggilan function, dengan 3 argumen
student('John', 'Gates', 'Seventh')  

# pemanggilan function dengan 2 argumen
student('John', 'Gates')               
student('John', 'Seventh')

def kali(a: int, b: int) -> int:
    return a * b

# Pemanggilan function
print("Hasil = " ,kali(3, 4))
print("Tipe Data : ", type(kali(3,4)))

# *args untuk argumen bervariasi
def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Selamat Datang', 'Di', 'PTI UNDIKMA')

def jumlahkan(*angka):
    total = sum(angka)
    print("Total:", total)

jumlahkan(1, 2, 3)
jumlahkan(5, 10, 15, 20)

# *args dengan ekstra argumen
def fun(arg1, *argv):
    print("First argument :", arg1)
    for arg in argv:
        print("Argument *argv :", arg)

# pemanggilan fungsi
fun('Hello', 'Selamat Datang', 'di', 'PTI UNDIKMA')

def info_mahasiswa(**data):
    for key, value in data.items():
        print(f"{key}: {value}")

# Pemanggilan function
info_mahasiswa(nama="Rina", jurusan="TI", angkatan=2022)

# kombinasi syntax *args dan **kwargs dalam satu function
def fun(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Pemanggilan function
fun(1, 2, 3, a=4, b=5)

nama = "Budi"  # variabel global

def sapa():
    print("Halo,", nama)

# memanggil function
sapa()

def halo():
    pesan = "Halo dari dalam fungsi!"  # variabel lokal
    print(pesan)

# memanggil function
halo()
print(pesan)  # ❌ Error! variabel 'pesan' tidak dikenali di luar fungsi


# membuat variabel global
nama = "UNDIKMA"
versi = "1.0.0"

def help():
    # ini variabel lokal
    nama = "Programku"
    versi = "1.0.2"
    # mengakses variabel lokal
    print "Nama: %s" % nama
    print "Versi: %s" % versi


# mengakses variabel global
print "Nama: %s" % nama
print "Versi: %s" % versi

# memanggil fungsi help()
help()


# Fungsi untuk menampilkan semua data buku
def show_data():
    if len(buku) <=0 :
        print("DATA BUKU BELUM ADA")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))

def insert_data():
    buku_baru = input("Judul Buku : ")
    buku.append(buku_baru)

def edit_data():
    show_data()
    indeks = int(input("Inputkan ID Buku : "))
    if(indeks > len(buku)):
        print("ID Buku Tidak Ditemukan")
    else:
        judul_baru = input("Judul Baru : ")
        buku[indeks] = judul_baru
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID Buku : "))
    if(indeks > len(buku)):
        print("ID Buku Tidak Ditemukan")
    else:
        buku.remove(buku[indeks])
        print(f"Buku dengan ID {indeks} Terhapus")

def show_menu():
    print("\n")
    print(5*"-","MENU", 5*"-")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    
    menu = int(input("PILIH MENU : "))
    print("\n")
    if menu == 1:
        show_data()
    elif menu == 2:
        insert_data()
    elif menu == 3:
        edit_data()
    elif menu == 4:
        delete_data()
    elif menu == 5:
        exit()
    else:
        print("Pilihan Anda Salah!")