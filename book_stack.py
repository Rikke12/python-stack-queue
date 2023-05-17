class BookStack:
    def __init__(self):
        self.stack = []

    def tambah_buku(self, nama_buku, pengarang):
        self.stack.append((nama_buku, pengarang))

    def hapus_buku_terakhir(self):
        if not self.is_empty():
            self.stack.pop()

    def buku_teratas(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


# Membuat objek tumpukan buku
stack = BookStack()

while True:
    print("\nMenu:")
    print("1. Tambah Buku")
    print("2. Hapus Buku Terakhir")
    print("3. Tampilkan Buku Teratas")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == '1':
        nama_buku = input("Masukkan nama buku: ")
        pengarang = input("Masukkan nama pengarang: ")
        stack.tambah_buku(nama_buku, pengarang)
        print("Buku berhasil ditambahkan.")
    elif pilihan == '2':
        if stack.is_empty():
            print("Tumpukan buku kosong.")
        else:
            stack.hapus_buku_terakhir()
            print("Buku terakhir dihapus.")
    elif pilihan == '3':
        buku_teratas = stack.buku_teratas()
        if buku_teratas is None:
            print("Tumpukan buku kosong.")
        else:
            nama_buku, pengarang = buku_teratas
            print("Buku teratas:")
            print("Nama buku:", nama_buku)
            print("Pengarang:", pengarang)
    elif pilihan == '4':
        print("Program telah selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")
