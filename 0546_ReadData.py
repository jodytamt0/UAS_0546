import mysql.connector
from prettytable import PrettyTable

config = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_akademik_0546"
)

def select_all_data():
    cursor = config.cursor()
    sql = "SELECT * FROM tbl_students_0546"
    cursor.execute(sql)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("data tidak tersedia")
    else:
        tabelSiswa = PrettyTable(["No", "Nim", "Nama", "JK", "Jurusan", "Alamat"])
        for data in results:
            tabelSiswa.add_row(data)
        print(tabelSiswa)

def select_many_data():
    cursor = config.cursor(buffered=True)
    sql = "SELECT * FROM tbl_students_0546"
    cursor.execute(sql)
    many = int(input("Masukan Limit : "))
    results = cursor.fetchmany(many)

    if many == 0:
        tabelSiswa = PrettyTable(["No", "Nim", "Nama", "JK", "Jurusan", "Alamat"])
        print(tabelSiswa)
    else:
        tabelSiswa = PrettyTable(["No", "Nim", "Nama", "JK", "Jurusan", "Alamat"])
        for data in results:
            tabelSiswa.add_row(data)
        print(tabelSiswa)

def search_data():
    nim = input("Masukan NIM : ")
    cursor = config.cursor()
    sql = "SELECT * FROM tbl_students_0546 WHERE nim='"+nim+"'"
    cursor.execute(sql)
    results = cursor.fetchall()

    tabelSiswa = PrettyTable(["No", "Nim", "Nama", "JK", "Jurusan", "Alamat"])
    for data in results:
        tabelSiswa.add_row(data)
    print(tabelSiswa)
    
def menu():
    print("1. Tampilkan semua data")
    print("2. Tampilkan data berdasaarkan limit")
    print("3. Cari data berdasarkan nim")
    print("0. Keluar")

    option = input("Pilih Menu> ")

    if option == "1":
        select_all_data()
    elif option == "2":
        select_many_data()
    elif option == "3":
        search_data()
    elif option == "0":
        exit()
    else:
        print("Pilih Menu yang valid")

if __name__ == '__main__':
    while(True):
        menu()
