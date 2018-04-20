import texttable as tt

def nilai_mahasiswa():
    nama = []
    nim = []
    n_tugas = []
    n_uts = []
    n_uas = []
    n_akhir = []

    x = [[]]

    jawab = 'y'

    tab = tt.Texttable()

    while (jawab == 'y'):
        print("============================================================")
        nama.append(input("\tMasukkan Nama : "))
        nim.append(input("\tMasukkan NIM  : "))
        tugas = int(input("\tNilai Tugas   : "))
        tugas = float(tugas)
        n_tugas.append(tugas)
        uts = int(input("\tNilai UTS     : "))
        uts = float(uts)
        n_uts.append(uts)
        uas = int(input("\tNilai UAS     : "))
        uas = float(uas)
        n_uas.append(uas)
        hasil = (tugas+uts+uas)/3
        n_akhir.append(hasil)
        jawab = input("\n\tTambah Data [y/t]? ")

    for i in nama :
        idx = nama.index(i)
        x.append([idx+1,nama[idx],nim[idx],n_tugas[idx],n_uts[idx],n_uas[idx],n_akhir[idx]])
    tab.add_rows(x)
    tab.set_cols_align(['l','l','l','r','r','r','r'])
    tab.header(['No','Nama','NIM','Nilai Tugas','Nilai UTS','Nilai UAS','Nilai Akhir'])
    print (tab.draw())
