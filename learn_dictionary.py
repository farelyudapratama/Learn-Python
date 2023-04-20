MENU = {
    'D':{"nama":"Dada","Harga":2500},
    'P':{"nama":"Paha","Harga":2000},
    'S':{"nama":"Sayap","Harga":1500},
}
print('GEROBAK AYAM')
print('-----------------------------')
print('Kode   Jenis Potong    Harga')
print('-----------------------------')
for kode, jenis in MENU.items():
    print(f"{kode:<6} {jenis['nama']:<15} {jenis['Harga']:>5}") 
banyakjenis = int(input("Banyak Jenis: "))
pilihan =  []
for i in range(banyakjenis):
    print('Jenis ke - ',i+1)
    while True:
        kodepotong = input("Kode Potong [D/P/S]: ")
        if kodepotong.upper() in MENU:
            break
        else:
            print("Kode Salah")
    banyakpotong = int(input("Banyak potong: "))
    pilihan.append({'kode': kodepotong.upper(), 'banyak':banyakpotong})
print('------------------------------------------------------------------')
print('No.   Jenis Potong    Harga Satuan     Banyak Beli    Jumlah Harga')
print('------------------------------------------------------------------')
total = 0
for i, pilih in enumerate(pilihan):
    jenispotong = MENU[pilih['kode']] ['nama']
    hargasatuan = MENU[pilih['kode']] ['Harga']
    jumlahharga = hargasatuan * pilih['banyak']
    total += jumlahharga
    print(f"{i+1:<5} {jenispotong:<19} {hargasatuan:<19} {pilih['banyak']:<10} {jumlahharga:>4}")
print('------------------------------------------------------------------')
jumlahbayar = total
print(f'Jumlah Bayar: {jumlahbayar}')
pajak = jumlahbayar * 0.1
totalbayar = jumlahbayar + pajak
print(f"Pajak 10% Rp. {pajak}")
print(f"Total Bayar Rp. {totalbayar}")
pembayaran = int(input("Pembayaran: "))
while pembayaran < totalbayar:
    print("Uang Anda kurang!")
    pembayaran = int(input("Pembayaran: "))
kembalian = pembayaran - totalbayar
print(f"Kembalian Rp. {kembalian}")
