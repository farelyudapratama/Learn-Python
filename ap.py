raw_input[]
def fibonacci(n):
    if n < 0:
        print ("Tidak ada bilangan yang bernilai negatif")
    if n==0 or n == 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

nilai = int(raw_input('masukkan :'))
hasil = fibonacci(nilai)
print ("fibonacci (&d) = %d" % (nilai,hasil))