class Customer:
    def __init__(self, nama, transaksi):
        self.nama = nama
        self.transaksi = transaksi

class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, customer):
        self.queue.append(customer)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def tampilkan_transaksi_selanjutnya(self):
        if self.is_empty():
            print("Antrian kosong")
        else:
            customer = self.queue[0]
            print(f"Transaksi berikutnya: {customer.transaksi} - {customer.nama}")

    def hapus_transaksi_yang_telah_dilayani(self):
        if self.is_empty():
            print("Antrian kosong")
        else:
            customer = self.queue.pop(0)
            print(f"Transaksi selesai: {customer.transaksi} - {customer.nama}")

queue = Queue()

while True:
    print("**** Antrean Transaksi Pelanggan *****")
    print("1. Tambah Transaksi ke Antrian")
    print("2. Tampilkan Transaksi Berikutnya")
    print("3. Hapus Transaksi yang telah dilayani")
    print("4. Keluar")

    choice = input("Masukkan pilihan: ")

    if choice == "1":
        nama = input("Masukkan nama pelanggan: ")
        transaksi = input("Masukkan jenis transaksi: ")
        customer = Customer(nama, transaksi)
        queue.enqueue(customer)
        print("Transaksi berhasil ditambahkan ke antrian.")
    elif choice == "2":
        queue.tampilkan_transaksi_selanjutnya()
    elif choice == "3":
        queue.hapus_transaksi_yang_telah_dilayani()
        print("transaksi layanan terakhir telah dihapus.")
    elif choice == "4":
        print("Terima kasih! Program berakhir.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
