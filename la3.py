def biodata():
    print('PROGRAM BIODATA')
    nama = input('Input Nama: ')
    kelas = input('Input Kelas: ')
    npm = input('Input NPM: ')
    print('================================')
    print('Biodata anda adalah: ')
    print('Nama: ' + nama)
    print('Kelas: ' + kelas)
    print('NPM: ' + npm)

def reamur(c):
    r = (4/5)*float(c)
    return r

def farenheit(c):
    f = (9/5) * float(c) + 32
    return f

def kelvin(c):
    k = float(c) + 273
    return k

def gbPersegi():
    n=int(input('Masukkan angka: '))
    for i in range(1,(n+3)):
        for j in range(1,(n+1)):
            print('* * ',end='')
        print()

def menu():
    print('----MENU----')
    print('1. Program Biodata')
    print('2. Konversi Suhu')
    print('3. Program Gambar persegi')
    print('4. Berhenti')
    pil=input('Pilih No Menu: ')
    print()
    if pil == '1':
        biodata()
        print()
    elif pil == '2':
        print('PROGRAM KONVERSI SUHU')
        c = int(input('Masukan Skala Celcius: '))
        print(f'Hasil suhu {c}°c adalah {reamur(c)}°r')
        print(f'Hasil suhu {c}°c adalah {farenheit(c)}°f')
        print(f'Hasil suhu {c}°c adalah {kelvin(c)}°k')
        print()
    elif pil == '3':
        print('PROGRAM GAMBAR PERSEGI')
        print('======================')
        gbPersegi()
        print()
    elif pil == '4':
        print('Program Berhenti')
        print()
        exit()
    else:
        print('Pilihan tersebut tidak ada')
        print()

while(True):
    menu()