#Program Manajemen Kontak

def melihat_kontak():
    if kontak:
        print("\nKontak Anda : ")
        print("--------------")
        for i, item in enumerate(kontak, start=1):
            print(f'{i}. {item["nama"]} ({item["HP"]}, {item["email"]})')
    else:
        print("Maaf, Kontak Anda Kosong")
        return 1
def menambahkan_kontak():
    nama = input("Masukkan nama kontak yang baru : ")
    HP = input("Masukkan nomor HP kontak yang baru : ")
    email = input("Masukkan email kontak yang baru : ")
    kontak_baru = {'nama': nama, 'HP': HP, 'email': email}
    kontak.append(kontak_baru)
    print("\nKontak Baru Berhasil Ditambahkan")
def menghapus_kontak():
    if melihat_kontak()==1:
        return
    else :
        i_hapus = int(input("Masukkan nomor kontak yang akan dihapus : "))
        del kontak[i_hapus - 1]
        print("\nKontak Berhasil Dihapus")

kontak1 = {'nama':"Bunga", 'HP':"08156742", 'email':"bunga@python.com"}
kontak2 = {'nama':"Jasmine", 'HP':"08512345", 'email':"jasmine@python.com"}
kontak = [kontak1, kontak2]

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
        melihat_kontak()
    elif pilihan == '2' : #menambahkan kontak
        menambahkan_kontak()
    elif pilihan == '3' : #menghapus kontak
        menghapus_kontak()
    elif pilihan == '4' : #keluar program
        print("Terima Kasih Telah Menggunakan Program Ini ")
        break
    else :
        print("Pilihan Anda Salah! Masukkan ulang mulai dari 1 - 4")
