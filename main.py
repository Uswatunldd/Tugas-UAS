import texttable as tt
import getpass
from tugas.penilaian import nilai_mahasiswa
from tugas.pembayaran import pembayaran
from tugas.cal import hitung

def menu():
    print("\n===========================================================")
    print("--------------Program STT Pelita Bangsa 17.C1--------------")
    print("===========================================================")
    print("\t1. Penilaian Mahasiswa")
    print("\t2. Pembayaran Mahasiswa")
    print("\t3. Kalkulator")
    print("===========================================================")
    print("\tSilahkan pilih (1-3)")
    print(" ")
    pilih = input("\tMasukkan Pilihan : ")
    if pilih == '1':
        nilai_mahasiswa()
    elif pilih == '2':
        pembayaran()
    elif pilih == '3':
        hitung()
    else:
        exit 
    tanya()

def tanya():
    tanya = input("\nKembali ke menu (y/t)? ")
    if tanya == 'y':
        menu()
    elif tanya == 't':
        exit
    else:
        print ("\n\tSalah input .......!!!")

username = input("Username : ")
password = getpass.getpass()
print("===========================================================")

if username == "uswah" and password == "uswatun22":
    menu()
else :
    print ("Maaf password atau username anda salah .........!!!")


 

