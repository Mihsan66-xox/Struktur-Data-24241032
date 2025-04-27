# Variabel global untuk menyimpan data mahasiswa
mahasiswa_list = []

def create():
    """Menambahkan nama mahasiswa ke dalam list."""
    nama = input("Masukkan nama mahasiswa: ")
    mahasiswa_list.append(nama)
    print(f"Nama '{nama}' berhasil ditambahkan.")

def read():
    """Menampilkan semua data mahasiswa."""
    if not mahasiswa_list:
        print("Tidak ada data mahasiswa.")
    else:
        print("Daftar Mahasiswa:")
        for index, nama in enumerate(mahasiswa_list):
            print(f"{index + 1}. {nama}")

def update():
    """Mengubah nama mahasiswa berdasarkan indeks."""
    read()  # Tampilkan daftar mahasiswa
    try:
        indeks = int(input("Masukkan nomor mahasiswa yang ingin diubah: ")) - 1
        if 0 <= indeks < len(mahasiswa_list):
            nama_baru = input("Masukkan nama baru: ")
            mahasiswa_list[indeks] = nama_baru
            print("Nama mahasiswa berhasil diubah.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def delete():
    """Menghapus nama mahasiswa berdasarkan indeks."""
    read()  # Tampilkan daftar mahasiswa
    try:
        indeks = int(input("Masukkan nomor mahasiswa yang ingin dihapus: ")) - 1
        if 0 <= indeks < len(mahasiswa_list):
            nama_dihapus = mahasiswa_list.pop(indeks)
            print(f"Nama '{nama_dihapus}' berhasil dihapus.")
        else:
            print("Indeks tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

def main():
    """Fungsi utama untuk menjalankan program."""
    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Mahasiswa")
        print("3. Ubah Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih aksi (1-5): ")
        
        if pilihan == '1':
            create()
        elif pilihan == '2':
            read()
        elif pilihan == '3':
            update()
        elif pilihan == '4':
            delete()
        elif pilihan == '5':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()