loop=True
while(loop):
    print('       ACTIVITY 2     ')
    print('1. Program Nilai')
    print('2. Program Mengeluarkan Data Array')
    pil = input('Masukkan Pilihan Anda: ')
    print('')
    #Pilihan 1
    if pil == '1':
        print('    Program  Nilai')
        uts = float(input('Masukkan Nilai UTS = '))
        uas = float(input('Masukkan Nilai UAS = '))
        nr = uts*0.7+uas*0.3
        print('========================')
        if nr >= 90:
            g = "A"
        elif nr >= 80:
            g = "B"
        elif nr >= 70:
            g = "C"
        elif nr >= 60:
            g = "D"
        else:
            g = "E"
        print('')
        print('Anda Mendapatkan Grade',g,'Dengan Nilai :',str(nr))
        print('='*50)
    #Pilihan 2
    elif pil == '2':
        nama = ['Farel','Rudi','Yuda','Gusti','Rini']
        s=1
        for i in nama:
            print('Nama ke',str(s),':',i)
            s+=1
    #Salah pilih
    else:
        print('input salah')
    print('')
    #Mengulang Program
    ulang=input('Ingin mengulang program (y/n)? ')
    if ulang=='y':
        loop=True
    elif ulang=='n':
        loop=False