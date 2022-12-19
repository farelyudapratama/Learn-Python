# Import library random untuk mengacak pilihan AI
import random

# Buat dictionary yang berisi pilihan batu, gunting, dan kertas
pilihan = {1: "batu", 2: "gunting", 3: "kertas"}

# Buat perulangan untuk mengulangi permainan
while True:
    # Dapatkan input pilihan dari user
    user_choice = input("Masukkan pilihan Anda (batu/gunting/kertas): ")

    # Acak pilihan AI
    ai_choice = random.choice([1, 2, 3])

    # Cetak pilihan AI
    print(f"Pilihan AI: {pilihan[ai_choice]}")

    # Tentukan pemenang permainan
    if user_choice == pilihan[ai_choice]:
        print("Hasilnya seri!")
    elif user_choice == "batu" and ai_choice == 2:
        print("Anda menang!")
    elif user_choice == "gunting" and ai_choice == 3:
        print("Anda menang!")
    elif user_choice == "kertas" and ai_choice == 1:
        print("Anda menang!")
    else:
        print("Anda kalah!")

    # Tanya apakah user ingin bermain lagi
    again = input("Apakah Anda ingin bermain lagi (y/n)? ")
    if again == "n":
        break
