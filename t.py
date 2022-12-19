class ling:
      def luasling(self, jari):
            self.jari = jari
            return 3.14 * (self.jari ** 2)

class segitiga:
  def inseg(self):
    print(' ')
    self.a = int(input('Masukkan alas: '))
    self.t = int(input('Masukkan tinggi: '))
  
  def luasseg(self):
    self.hasilseg = (self.a * self.t)/2

class trapesium:
  def intra(self):
    print(' ')
    self.s1 = int(input('Masukkan sisi 1: '))
    self.s2 = int(input('Masukkan sisi 2: '))
    self.t  = int(input('Masukkan tinggi: '))

  def luastra(self):
    self.hasiltra = ((self.s1 + self.s2) * self.t)/2
  
class jajar(segitiga):
  def luasjar(self):
    self.hasiljar = self.a * self.t

def menu():
  print("""
  ================ MENU ================
  1. Lingkaran
  2. Segitiga
  3. Trapesium
  4. Jajar Genjang
  """)
  
  pilih = int(input('Masukkan Pilihan Anda: '))
  print(' ')
  if pilih == 1:
    print('========== Menghitung Luas Lingkaran ==========')
    hasil1 = ling()
    jari = int(input('Masukkan Jari-Jari: '))
    print()
    print('Luas Lingkaran adalah: ', hasil1.luasling(jari))
    menu()
  
  elif pilih == 2:
    print('========= Menghitung Luas Segitiga ============')
    hasil2 = segitiga()
    hasil2.inseg()
    hasil2.luasseg()
    print()
    print('Luas Segitiga adalah: ', hasil2.hasilseg)
    menu()
  
  elif pilih == 3:
    print('========= Menghitung Luas Trapesium ===========')
    hasil3 = trapesium()
    hasil3.intra()
    hasil3.luastra()
    print()
    print('Luas Trapesium adalah: ', hasil3.hasiltra)
    menu()
  
  elif pilih == 4:
    print('======== Menghitung Luas Jajargenjang =========')
    hasil4 = jajar()
    hasil4.inseg()
    hasil4.luasjar()
    print()
    print('Luas Jajargenjang adalah: ', hasil4.hasiljar)
    menu()
  
  else:
    print('!!!! Masukkan Pilihan Yang Benar !!!!')
    menu()

nama = input('Masukkan Nama Anda: ')
print('Hai saya: ', nama)
menu()