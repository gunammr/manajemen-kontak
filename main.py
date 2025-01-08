"Program Manajemen Kontak"

import kontak

def main():
    kontak_keluarga = kontak.Kontak()
    kontak_sekolah = kontak.Kontak()

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

if __name__ == "__main__":
    main()