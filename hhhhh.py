susah = int(input('masukkan bilangan:'))
susah=susah%2==0 or susah%3==0 and susah%2==1 and susah%3==1 and (susah%2==1 and susah%3==0)
print(susah)