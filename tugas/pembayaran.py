def pembayaran():
    print("===========================================================")
    nama = input("\tMasukkan Nama = ")
    nim = input("\tMasukkan Nim = ")
    semester = input("\tMasukkan Semester saat ini = ")
    print("\n\t---Pilihan Pembayaran---")
    print("\t1. Pembayaran SPP")
    print("\t2. Pembayaran UTS")
    print("\t3. Pembayaran UAS")
    print("\t4. Pembayaran SPP & UTS")
    print("\t5. Pembayaran SPP & UAS")
    pilih = input("\n\tSilahkan Pilih : ")
    if pilih == '1':
        spp()
    elif pilih == '2':
        uts()
    elif pilih == '3':
        uas()
    elif pilih == '4':
        spp_uts()
    elif pilih == '5':
        spp_uas()
    else:
        exit
        tanya()

def spp():
    bulan = int(input("\n\tJumlah bulan yang dibayar = "))
    bulan = int(bulan)
    byr_spp = 350000 * bulan
    total = byr_spp + 5000
    print("\tTotal bayar spp Rp.350000 * ",bulan," = Rp.",byr_spp)
    print("\tBiaya tambahan server sebesar Rp.5000")
    print("===========================================================")
    print("\tTotal yang harus dibayar Rp.",total)

def uts():
    matkul_uts = int(input("\n\tJumlah mata kuliah = "))
    matkul_uts = int(matkul_uts)
    byr_uts = 25000 * matkul_uts
    total = byr_uts + 5000
    print("\tTotal bayar uts Rp.25000 * ",matkul_uts," = Rp.",byr_uts)
    print("\tBiaya tambahan server sebesar Rp.5000")
    print("===========================================================")
    print("\tTotal yang harus dibayar Rp.",total)

def uas():
    matkul_uas = int(input("\n\tJumlah mata kuliah = "))
    matkul_uas = int(matkul_uas)
    byr_uas = 50000 * matkul_uas
    total = byr_uas + 5000
    print("\tTotal bayar uas Rp.50000 * ",matkul_uas," = Rp.",byr_uas)
    print("\tBiaya tambahan server sebesar Rp.5000")
    print("===========================================================")
    print("\tTotal yang harus dibayar Rp.",total)
    

def spp_uts():
    bulan = int(input("\n\tJumlah bulan yang dibayar = "))
    matkul_uts = int(input("\n\tJumlah mata kuliah = "))
    matkul_uts = int(matkul_uts)
    bulan = int(bulan)
    total_spp = 350000 * bulan
    byr_uts = 25000 * matkul_uts
    total = total_spp + byr_uts + 5000
    print("\n\tTotal bayar spp Rp.350000 * ",bulan," = Rp.",total_spp)
    print("\tTotal bayar uts Rp.25000 * ",matkul_uts," = Rp.",byr_uts)
    print("\tBiaya tambahan server sebesar Rp.5000")
    print("===========================================================")
    print("\tTotal yang harus dibayar Rp.",total)

def spp_uas():
    bulan = int(input("\n\tJumlah bulan yang dibayar = "))
    matkul_uas = int(input("\n\tJumlah mata kuliah = "))
    matkul_uas = int(matkul_uas)
    bulan = int(bulan)
    total_spp = 350000 * bulan
    byr_uas = 50000 * matkul_uas
    total = total_spp + byr_uas + 5000
    print("\n\tTotal bayar spp Rp.350000 * ",bulan," = Rp.",total_spp)
    print("\tTotal bayar uts Rp.50000 * ",matkul_uas," = Rp.",byr_uas)
    print("\tBiaya tambahan server sebesar Rp.5000")
    print("===========================================================")
    print("\tTotal yang harus dibayar Rp.",total)
