def tugas1():
    print('tugas 1',end='\n')
    sewaph = 10000
    mulai = 6
    selesai = 23.5
    totalwaktu = selesai-mulai
    if(totalwaktu>=12):
        sisawaktu = totalwaktu-12
        if(sisawaktu>int(sisawaktu)):
            global hargapec
            hargapec = 100 * (sisawaktu-int(sisawaktu)) / 60 * sewaph
        harga = int(sisawaktu)*sewaph + hargapec
        global total
        total = harga + 200000
    print('total harga = ',total)

def tugas2():
    print('\ntugas 2',end='\n')
    jarak = 795
    jarakperliter = 12
    totalliterbensin = jarak/jarakperliter
    print('total bensin yg diperlukan adalah ',totalliterbensin)
    return totalliterbensin

def tugas3():
    print('\ntugas 3',end='\n')
    kapasitasperliter = 50
    singgah = tugas2()/kapasitasperliter
    print('pak budi harus mengisi bensin',singgah)

def tugas4():
    print('\ntugas 4',end='\n')
    mulai = 6
    AkeB = 125/62
    BkeC = 256/70
    sampai = mulai+AkeB+BkeC+.45
    print('pak amin sampai d kota c pukul ',int(sampai))

def tugas5():
    print('\ntugas 5',end='\n')
    jumlahlaki2 = 100
    jumlahperempuan = 150
    print('jumlah laki-laki : '+'\n'+'*'*jumlahlaki2)
    print('jumlah perempuan : '+'\n'+'*'*jumlahperempuan)

tugas1()
tugas2()
tugas3()
tugas4()
tugas5()
