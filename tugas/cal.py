def tambah ():
    print ("\t1. Penjumlahan")
    a = int(input("\tMasukkan nilai x = "))
    b = int(input("\tMasukkan nilai y = "))
    c = a + b
    print ("\tx + y = ",c)
    tanya()

def kurang ():
    print ("\t2. Pengurangan")
    a = int(input("\tMasukkan nilai x = "))
    b = int(input("\tMasukkan nilai y = "))
    c = a - b
    print ("\tx - y = ",c)
    tanya()

def bagi ():
    print ("\t3. Pembagian")
    a = int(input("\tMasukkan nilai x = "))
    b = int(input("\tMasukkan nilai y = "))
    c = a / b
    print ("\tx / y = ",c)
    tanya()

def kali ():
    print ("\t4. Perkalian")
    a = int(input("\tMasukkan nilai x = "))
    b = int(input("\tMasukkan nilai y = "))
    c = a * b
    print ("\tx * y = ",c)
    tanya()

def tanya ():
    tanya = input("\n\tKembali ke menu kalkulator (y/t)? ")
    if tanya == "y":
        hitung()
    elif tanya == "t":
        exit
    else:
        print ("\n\tSalah input .......!!!")

def hitung():
    print("==========================================================")
    print("Program Kalkulator Sederhana")
    print("==========================================================")
    print("\t1. Penjumlahan")
    print("\t2. Pengurangan")
    print("\t3. Pembagian")
    print("\t4. Perkalian")
    print("==========================================================")
    print("\tSilahkan pilih 1-4")
    print(" ")
    pil = input("Masukkan pilihan : ")
    if pil == '1':
        tambah()
    elif pil == '2':
        kurang()
    elif pil == '3':
        bagi()
    elif pil == '4':
        kali()
    else :
        print("Maaf, input yang Anda masukkan salah")
        print("Coba ulangi kembali...")
        tanya()

        





    
