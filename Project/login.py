#create login dan register yang data nya akan disimpan di csv da untuk login data di ambil dari csv dengan role admin dan user yang memiliki hak akses yang berbeda

import csv
import os



def login():
    os.system('cls')
    print("Login")
    print("=====")
    username = input("Username: ")
    password = input("Password: ")
    found = False
    with open('user.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == username and row[1] == password and row[2] == "admin":
                print("Berhasil login")
                menu_admin()
                found = True
                
            else:
                print("Gagal login")
                print("Username atau password salah")
                print("Silahkan coba lagi")

                pilihan = input("Kembali ke menu login? (y/n) ")
                if pilihan == "y":
                    login()
                else:
                    exit()
            

            

    
def cek_plat():
    os.system('cls')
    print("Cek Plat")
    print("========")
    nim = input("NIM: ")
    no_plat = "P"+ nim[8:12]+ "IF"
    print("No Plat: " + no_plat)
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[3] == no_plat:
                print("Plat ditemukan")
                return True
            else:
                print("Plat tidak ditemukan")
                return False



def create():
    os.system('cls')
    print("Create")
    print("======")
    no= input("No: ")
    nama = input("Nama: ")
    nim = input("NIM: ")
    no_plat = "P"+" "+nim[7:12] +" "+ "IF"
    nama = input("Nama: ")
    jenis_ken = input("Jenis Kendaraan: ")

    
    with open('data.csv', mode='a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow ([no, nim, no_plat, nama, jenis_ken])
        
        pilihan = input("Kembali ke menu admin? (y/n) ")
    if pilihan == "y":
        menu_admin()
    else:
        exit()

def read():
    os.system('cls')
    print("Read")
    print("=====")
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if len(row) >= 5:
             print("No: " + row[0])
             print("Nama: " + row[1])
             print("NIM: " + row[2])
             print("No Plat: " + row[3])
             print("Jenis Kendaraan: " + row[4])
             print("\n")

            else:
             print("SEMENTARA HANYA INI YANG BISA DITAMPILKAN")
             return True
    pilihan = input("Kembali ke menu admin? (y/n)")
    if pilihan == "y":
        menu_admin()
    else:
        exit()

def update():
    os.system('cls')
    print("Update")
    print("======")
    no = input("No: ")
    nama = input("Nama: ")
    nim = input("NIM: ")
    no_plat = "P"+" "+nim[8:12]+" "+"IF"
    jenis_ken = input("Jenis Kendaraan: ")
   
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[0] == no:
                row[0] = no
                row[1] = nim
                row[2] = no_plat
                row[3] = nama
                row[4] = jenis_ken
                print("Data berhasil di update")
        
            else:
                print("Data tidak ditemukan")
                return False

    pilihan = input("Kembali ke menu admin? (y/n) ")
    if pilihan == "y":
        menu_admin()
    else:
        exit()


def delete():
  
    os.system('cls')
    print("Delete")
    print("======")
    no= input("No: ")
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data_csv = list(csv_reader)
        for row in data_csv:
            if row[0] == no:
                data_csv.remove(row)
                print("Data berhasil di hapus")
            else:
                print("Data tidak ditemukan")
                return False
    


def daftar_admin():
    os.system('cls')
    print("Daftar Admin")
    print("============")
    with open('user.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if len(row) >= 3:
             print("Username: " + row[0])
             print("Password: " + row[1])
             print("Role: " + row[2])
             print("\n")
            else:
             pass
        
    pilihan = input("Kembali ke menu admin? (y/n)")
    if pilihan == "y":
        menu_admin()
    else:
        exit()
    return True
    
            
        
        
    

def tambah_admin():
    os.system('cls')
    print("Tambah Admin")
    print("============")
    username = input("Username: ")
    password = input("Password: ")
    role = input("Role: ")
    with open('user.csv', mode='a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow ([username, password, role])

    pilihan = input("Kembali ke menu admin? (y/n)")
    if pilihan == "y":
        menu_admin()
    else:
        exit()
    return True

def hapus_admin():
    os.system('cls')
    print("Hapus Admin")
    print("============")
    username = input("Username: ")
    found = False

    with open('user.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data_csv = list(csv_reader)

    with open('user.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')
        
        for row in data_csv:
            if row[0] == username:
                found = True
                print(f"Data {username} berhasil dihapus")
            else:
                csv_writer.writerow(row)

    if not found:
        print("Data tidak ditemukan")

    pilihan = input("Kembali ke menu admin? (y/n)")
    if pilihan.lower() == "y":
        menu_admin()
    else:
        exit()




def cari_nama():
    os.system('cls')
    print("Cari Data")
    print("============")
    nama = input("Cari berdasarkan nama: ")
    nama.upper()
    with open('data.csv', newline='') as csvfile:
        fieldnames = ['No', 'Nim', 'No Plat', 'Nama', 'Jenis Kendaraan']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            if row['Nama'] == nama:
             print("No: " + row['No'])
             print("Nama: " + row['Nama'])
             print("NIM: " + row['Nim'])
             print("No Plat: " + row['No Plat'])
             print("Jenis Kendaraan: " + row['Jenis Kendaraan'])
             print("\n")
             
             
        else:
             print("Baris tidak ditemukan")


    pilihan = input("Kembali ke menu admin? (y/n)")
    if pilihan == "y":
        menu_admin()
    else:
        exit()


def jenis_cari():
    os.system('cls')
    print("Cari Data")
    print("masukan cari berdasarkan")
    print("1. Nama")
    print("2. NIM")
    print("3. jenis kendaraan")
    print("4. kembali ke menu admin")

    menu = input("Pilih menu> ")
    if menu == "1":
        cari_nama()
    elif menu == "2":
        cari_nim()
    elif menu == "3":
        cari_jenis_ken()
    elif menu == "5":
        menu_admin()
    else:
        print("Menu tidak tersedia")

def cari_nim():
    os.system('cls')
    print("Cari Data")
    print("============")
    nim = input("Cari berdasarkan nim: ")
    with open('data.csv', newline='') as csvfile:
      os.system('cls')
    print("Cari Data")
    print("============")
    nim = input("Cari berdasarkan nim: ")
    with open('data.csv', newline='') as csvfile:
        fieldnames = ['No', 'Nim', 'No Plat', 'Nama', 'Jenis Kendaraan']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            if row['Nim'] == nim:
             print("No: " + row['No'])
             print("Nama: " + row['Nama'])
             print("NIM: " + row['Nim'])
             print("No Plat: " + row['No Plat'])
             print("Jenis Kendaraan: " + row['Jenis Kendaraan'])
             print("\n")
             return True
             
        else:
             print("Baris tidak ditemukan")


    pilihan = input("Kembali ke menu admin? (y/n)")
    if pilihan == "y":
        menu_admin()
    else:
        exit()


def cari_jenis_ken():
    os.system('cls')
    print("Cari Data")
    print("============")
    jenis_ken = input("Cari berdasarkan jenis kendaraan: ")
    with open('data.csv', newline='') as csvfile:
        fieldnames = ['No', 'Nama', 'NIM', 'No Plat', 'Jenis Kendaraan']
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        for row in reader:
            if row['Jenis Kendaraan'] == jenis_ken:
             print("No: " + row['No'])
             print("Nama: " + row['Nama'])
             print("NIM: " + row['NIM'])
             print("No Plat: " + row['No Plat'])
             print("Jenis Kendaraan: " + row['Jenis Kendaraan'])
             print("\n")

            else:  
                pass

        pilihan = input("Kembali ke menu admin? (y/n)")
        if pilihan == "y":
            menu_admin()
        else:
            exit()
    
         
    

def menu_admin():
    os.system('cls')
    print("Menu Admin")
    print("=====")
    print("============== MANAGE DATA ==============")
    print("1. Tambahkan Data")
    print("2. Tamplikan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("============== MANAGE ADMIN ==============")
    print
    print("5. Daftar Admin")
    print("6. Tambah admin")
    print("7. Hapus admin")
    print("============== KELUAR ==============")
    print("8. Cari Data")
    print("9. Keluar")

    menu = input("Pilih menu> ")
    if menu == "1":
        create()
    elif menu == "2":
        read()
    elif menu == "3":
        update()
    elif menu == "4":
        delete()
    elif menu == "5":
        daftar_admin()
    elif menu == "6":
        tambah_admin()
    elif menu == "7":
        hapus_admin()
    elif menu == "8":
        jenis_cari()
    elif menu == "9":
        exit()
    else:
        print("Menu tidak tersedia")

    
    




print("Selamat Datang!")
print("==============")

print("EASY TAX MAKE UR LIFE EASIER")
print("========")


print("1. admin")
print("2. user ")


menu = input("Pilih menu> ")
if menu == "1":
    login()
elif menu == "2":
    cek_plat()
else:
    print("Menu tidak tersedia")







