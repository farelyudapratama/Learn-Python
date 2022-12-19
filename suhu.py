#Farel Yuda Pratama 50421470
print('PROGRAM KONVERSI TEMPERATURE')
print('')

#celsius
c = input('Masukkan suhu dalam celcius : ')
print('Suhu adalah',c, 'celcius')

#reamur
r = (4//5)*float(c)
print('Suhu dalam reamur adalah =',r, 'Reamur')

#fahrenheit
f = (9/5) * float(c) + 32
print('Suhu dalam fahrenheit adalah =',f,'Fahrenheit')

#kelvin
k = float(c) + 273
print('Suhu dalam kelvin adalah =',k,'Kelvin')
