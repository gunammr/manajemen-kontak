'Ini adalah module yang berisi class untuk menjalankan program'

import dokumen

class Kontak:
    def __init__(self):
        self.kontak = dokumen.membuka_kontak()

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
        dokumen.menyimpan_kontak(isi = self.kontak)