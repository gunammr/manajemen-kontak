#Program Manajemen Kontak

def membuka_kontak(path = 'kontak.txt'):
    with open(path, mode='r') as file:
        kontak = file.readlines()
    return kontak

def menyimpan_kontak(path = 'kontak.txt', isi=[]):
    with open(path, mode='w') as file:
        file.writelines(isi)

class Kontak:
    def __init__(self):
        self.kontak = membuka_kontak()

    def melihat_kontak(self):
        if self.kontak:
            print("\nKontak Anda : ")
            print("--------------")
            for i, item in enumerate(self.kontak, start=1):
                print(f'{i}. ' + item )
        else:
            print("Maaf, Kontak Anda Kosong")
            return 1
    def menambahkan_kontak(self):
        nama = input("Masukkan nama kontak yang baru : ")
        HP = input("Masukkan nomor HP kontak yang baru : ")
        email = input("Masukkan email kontak yang baru : ")
        kontak_baru = f"{nama}, ({HP}, {email})" + "\n"
        self.kontak.append(kontak_baru)
        print("\nKontak Baru Berhasil Ditambahkan")
    def menghapus_kontak(self):
        if self.melihat_kontak()==1:
            return
        else :
            try :
                i_hapus = int(input("Masukkan nomor kontak yang akan dihapus : "))
                del self.kontak[i_hapus - 1]
                print("\nKontak Berhasil Dihapus")
            except :
                print("Input yang anda masukkan salah!")
    def keluar_kontak(self):
        menyimpan_kontak(isi = self.kontak)

kontak_keluarga = Kontak()
kontak_sekolah = Kontak()

while True:
    print("------------------------")
    print("Program Manajemen Kontak")
    print("------------------------")
    print("1. Melihat semua kontak ")
    print("2. Menambahkan kontak ")
    print("3. Menghapus kontak ")
    print("4. Keluar Program ")

    pilihan = input("Masukkan pilihan anda ( 1 - 4 ) : ")

    if pilihan == '1' : #melihat semua kontak
        kontak_sekolah.melihat_kontak()
    elif pilihan == '2' : #menambahkan kontak
        kontak_sekolah.menambahkan_kontak()
    elif pilihan == '3' : #menghapus kontak
        kontak_sekolah.menghapus_kontak()
    elif pilihan == '4' : #keluar program
        kontak_sekolah.keluar_kontak()
        print("Terima Kasih Telah Menggunakan Program Ini ")
    else :
        print("Pilihan Anda Salah! Masukkan ulang mulai dari 1 - 4")
