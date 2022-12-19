print("""
=================================================
-------------PEMBELIAN AKSESORIS LAPTOP----------
=================================================
""")
input('Nama Pembeli\t: ')
b1=input('Nama Barang 1\t: ')
b2=input('Nama Barang 2\t: ')
jml1=int(input('Jumlah Pembelian '+b1+'\t : '))
jml2=int(input('Jumlah Pembelian '+b2+'\t : '))
h1=int(input('Harga '+b1+'\t: Rp. '))
h2=int(input('Harga '+b2+'\t: Rp. '))
t1= int(jml1*h1)
t2= int(jml2*h2)
ts= t1+t2
print('Total Bayar \t: Rp.',ts)
Up=int(input('Uang Pembayaran\t: Rp. '))
print('Uang Kembalian \t: Rp. ',(Up-ts))
print("""
===============================================
-----------------TERIMAKASIH-------------------
===============================================
""")